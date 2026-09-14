#!/usr/bin/env python3
"""Check rendered SEO without browser dependencies; run against a production build."""

import argparse
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


CANONICAL = "https://fullscope-media.com"
ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "Mozilla/5.0 (compatible; FullScopeSEOCheck/1.0)"
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.text = []
        self.stack = []
        self.schemas = []
        self.ld = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag not in VOID_TAGS:
            self.stack.append(tag)
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.ld = ""

    def handle_endtag(self, tag):
        if tag == "script" and self.ld is not None:
            self.schemas.append(json.loads(self.ld))
            self.ld = None
        if tag in self.stack:
            self.stack = self.stack[:len(self.stack) - 1 - self.stack[::-1].index(tag)]

    def handle_data(self, data):
        if self.ld is not None:
            self.ld += data
        if not any(tag in self.stack for tag in ("script", "style")):
            self.text.append((self.stack.copy(), data))

    def content(self, tag):
        return " ".join(" ".join(text for stack, text in self.text if tag in stack).split())

    def attrs(self, tag, **filters):
        return [attrs for name, attrs in self.tags if name == tag and all(attrs.get(k) == v for k, v in filters.items())]


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None


def fetch(url):
    try:
        response = build_opener(NoRedirect).open(Request(url, headers={"User-Agent": USER_AGENT}), timeout=20)
    except HTTPError as error:
        response = error
    with response:
        return response.status, response.headers, response.read().decode("utf-8")


def values(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from values(child)
    elif isinstance(value, list):
        for child in value:
            yield from values(child)
    elif isinstance(value, str):
        yield value


def googlebot_allowed(robots, url):
    # RobotFileParser uses first-match rules; Google uses the longest match.
    entry = next((entry for entry in robots.entries if entry.applies_to("Googlebot")), robots.default_entry)
    if entry is None:
        return True
    path = urlsplit(url).path
    matches = []
    for rule in entry.rulelines:
        rule_path = unquote(rule.path)
        pattern = re.escape(rule_path).replace(r"\*", ".*").replace(r"\$", "$")
        if re.match(pattern, path):
            matches.append((len(rule_path.rstrip("$")), rule.allowance))
    return max(matches)[1] if matches else True


def run(base, output):
    failures = []

    def check(condition, message):
        if not condition:
            failures.append(message)

    status, _, xml = fetch(base + "/sitemap.xml")
    check(status == 200, f"sitemap status {status}")
    urls = [node.text for node in ET.fromstring(xml).findall("{*}url/{*}loc")]
    check(bool(urls) and len(urls) == len(set(urls)), "empty/duplicate sitemap URLs")
    for url in urls:
        parsed = urlsplit(url)
        check(parsed.scheme == "https" and parsed.netloc == "fullscope-media.com", f"noncanonical sitemap URL: {url}")
        check(not parsed.query and not parsed.fragment, f"sitemap query/fragment: {url}")
    paths = {urlsplit(url).path for url in urls}
    for file in (ROOT / "src/routes").rglob("+page.svelte"):
        parts = file.relative_to(ROOT / "src/routes").parts[:-1]
        if not any("[" in part for part in parts):
            route = "/" + "/".join(part for part in parts if not part.startswith("("))
            check(route in paths, f"static page omitted from sitemap: {route}")

    status, _, robots_text = fetch(base + "/robots.txt")
    check(status == 200, f"robots status {status}")
    robots = RobotFileParser()
    robots.parse(robots_text.splitlines())
    check(robots.site_maps() == [CANONICAL + "/sitemap.xml"], "robots sitemap hostname")
    check(not googlebot_allowed(robots, CANONICAL + "/api/test"), "API robots exclusion lost")

    def read_page(path):
        status, headers, html = fetch(base + path)
        return path, status, headers, html, Document(html)

    with ThreadPoolExecutor(max_workers=4) as pool:
        pages = list(pool.map(read_page, sorted(paths)))
    documents = {path: doc for path, _, _, _, doc in pages}
    rows, graph, assets = [], {}, set()
    for path, status, headers, html, doc in pages:
        expected = CANONICAL + path
        check(status == 200, f"{path}: status {status} (redirects are not followed)")
        check("text/html" in headers.get("Content-Type", ""), f"{path}: not HTML")
        for tag in ("title", "h1", "main"):
            check(len(doc.attrs(tag)) == 1 and bool(doc.content(tag)), f"{path}: expected one nonempty {tag}")
        descriptions = doc.attrs("meta", name="description")
        check(len(descriptions) == 1 and bool(descriptions[0].get("content")), f"{path}: description")
        check([a.get("href") for a in doc.attrs("link", rel="canonical")] == [expected], f"{path}: canonical")
        check([a.get("content") for a in doc.attrs("meta", property="og:url")] == [expected], f"{path}: og:url")
        for key, value in (("property", "og:image"), ("name", "twitter:image")):
            images = doc.attrs("meta", **{key: value})
            check(len(images) == 1 and images[0].get("content", "").startswith("https://"), f"{path}: absolute {value}")
        directives = " ".join(a.get("content", "") for a in doc.attrs("meta") if a.get("name", "").lower() in ("robots", "googlebot"))
        directives += " " + headers.get("X-Robots-Tag", "")
        check(not re.search(r"\b(noindex|nofollow|none)\b", directives, re.I), f"{path}: conflicting robots directives")
        check(googlebot_allowed(robots, expected), f"{path}: blocked by robots.txt")
        check(html.count("})(window,document,'script','dataLayer','GTM-N8RVSFDH')") == 1, f"{path}: GTM bootstrap count")
        check(bool(doc.schemas), f"{path}: missing JSON-LD")
        business = [schema for schema in doc.schemas if schema.get("@id") == CANONICAL + "/#business"]
        check(len(business) == 1 and business[0].get("name") == "Full Scope Media LLC", f"{path}: business identity")
        for value in values(doc.schemas):
            parsed = urlsplit(value)
            if parsed.hostname in ("fullscope-media.com", "www.fullscope-media.com"):
                check(parsed.scheme == "https" and parsed.netloc == "fullscope-media.com", f"{path}: schema URL {value}")
        breadcrumbs = [schema for schema in doc.schemas if schema.get("@type") == "BreadcrumbList"]
        check(len(breadcrumbs) == (0 if path == "/" else 1), f"{path}: breadcrumb count")
        for schema in breadcrumbs:
            trail = schema["itemListElement"]
            check(trail[-1]["item"] == expected, f"{path}: breadcrumb leaf")
            check([item["position"] for item in trail] == list(range(1, len(trail) + 1)), f"{path}: breadcrumb positions")
            check(all(urlsplit(item["item"]).path in paths for item in trail), f"{path}: broken breadcrumb ancestor")

        graph[path] = set()
        for link in doc.attrs("a"):
            target = urlsplit(urljoin(expected, link.get("href", "")))
            if target.netloc != "fullscope-media.com" or target.path.startswith("/cdn-cgi/"):
                continue
            check(target.path in paths, f"{path}: internal link outside sitemap: {target.path}")
            graph[path].add(target.path)
            if target.fragment and target.path in documents:
                ids = {a.get("id") for _, a in documents[target.path].tags}
                check(unquote(target.fragment) in ids, f"{path}: broken fragment {target.path}#{target.fragment}")
        for image in doc.attrs("img"):
            check("alt" in image, f"{path}: missing image alt attribute")
            check(not (image.get("fetchpriority") == "high" and image.get("loading") == "lazy"), f"{path}: lazy high-priority image")
        for tag in ("img", "source"):
            for image in doc.attrs(tag):
                candidates = [image.get("src", "")]
                candidates += [part.strip().split()[0] for part in image.get("srcset", "").split(",") if part.strip()]
                assets.update(candidate for candidate in candidates if candidate.startswith("/") and not candidate.startswith("//"))
        rows.append({"path": path, "status": status, "title": doc.content("title"), "description": descriptions[0].get("content") if descriptions else "", "canonical": expected, "h1": doc.content("h1"), "main_words": len(doc.content("main").split())})

    for field in ("title", "description"):
        check(all(count == 1 for count in Counter(row[field] for row in rows).values()), f"duplicate {field}")
    seen, queue = set(), deque(["/"])
    while queue:
        path = queue.popleft()
        if path not in seen:
            seen.add(path)
            queue.extend(graph.get(path, set()) - seen)
    check(paths <= seen, f"orphaned pages: {sorted(paths - seen)}")
    for asset in sorted(assets):
        # Vite's hashed imports are checked in build output, public images in static/.
        directory = ROOT / ("build/client" if asset.startswith("/_app/") else "static")
        file = directory / unquote(urlsplit(asset).path).lstrip("/")
        check(file.is_file() and not file.read_bytes().startswith(b"version https://git-lfs.github.com/spec/v1"), f"missing image or LFS pointer: {asset}")

    query = "/studio/web-design?utm_source=seo-check&ref=a%2Fb"
    _, status, _, _, doc = read_page(query)
    check(status == 200 and [a.get("href") for a in doc.attrs("link", rel="canonical")] == [CANONICAL + "/studio/web-design"], "query-string canonical")
    status, headers, _ = fetch(base + query.replace("?", "/?"))
    check(status in (301, 308) and urljoin(base, headers.get("Location", "")) == base + query, "trailing-slash redirect must preserve query in one hop")
    for path in ("/seo-check-missing", "/journal/seo-check-missing", "/portfolio/seo-check-missing", "/real-estate-photographer/seo-check-missing"):
        check(fetch(base + path)[0] == 404, f"{path}: expected real 404")

    if output:
        Path(output).write_text(json.dumps({"base": base, "routes": rows, "image_assets": len(assets), "failures": failures}, indent=2) + "\n")
    for failure in failures:
        print("FAIL:", failure)
    print(f"{len(rows)} routes; {len(assets)} image assets; {len(failures)} failures")
    return bool(failures)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="http://127.0.0.1:4173")
    parser.add_argument("--output", help="Write the route inventory and failures as JSON")
    args = parser.parse_args()
    try:
        sys.exit(run(args.base.rstrip("/"), args.output))
    except Exception as error:
        print(f"SEO check could not complete: {error}", file=sys.stderr)
        sys.exit(1)
