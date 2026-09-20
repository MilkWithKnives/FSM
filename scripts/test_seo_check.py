import importlib.util
import json
from pathlib import Path
import unittest
from urllib.robotparser import RobotFileParser


spec = importlib.util.spec_from_file_location("seo_check", Path(__file__).with_name("seo-check.py"))
seo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seo)


class SEOCheckTests(unittest.TestCase):
    def test_robots_longest_rule_and_allow_tie(self):
        cases = [
            (["Allow: /", "Disallow: /api/"], "/api/test", False),
            (["Allow: /", "Disallow: /api/"], "/studio/web-design", True),
            (["Disallow: /", "Allow: /studio"], "/studio/web-design", True),
            (["Disallow: /studio", "Allow: /studio"], "/studio", True),
            (["Disallow: /private/*"], "/private/test", False),
            (["Disallow: /test$"], "/test-more", True),
            (["Disallow: /test$"], "/test", False),
        ]
        for rules, path, allowed in cases:
            with self.subTest(rules=rules, path=path):
                robots = RobotFileParser()
                robots.parse(["User-agent: *", *rules])
                self.assertEqual(seo.googlebot_allowed(robots, seo.CANONICAL + path), allowed)

    def test_googlebot_specific_group(self):
        robots = RobotFileParser()
        robots.parse(["User-agent: Googlebot", "Disallow: /studio", "", "User-agent: *", "Allow: /"])
        self.assertFalse(seo.googlebot_allowed(robots, seo.CANONICAL + "/studio"))

    def test_rendered_metadata_and_content(self):
        doc = seo.Document('<title>Design &amp; build</title><meta name="description" content="A custom website"><main><h1>Design</h1><p>Useful content</p><script>invisible()</script></main>')
        self.assertEqual(doc.content("title"), "Design & build")
        self.assertEqual(doc.content("main"), "Design Useful content")
        self.assertEqual(len(doc.attrs("h1")), 1)
        self.assertEqual(doc.attrs("meta", name="description")[0]["content"], "A custom website")

    def test_duplicate_canonical_is_not_silently_deduplicated(self):
        doc = seo.Document('<link rel="canonical" href="https://fullscope-media.com/"><link rel="canonical" href="https://www.fullscope-media.com/">')
        self.assertEqual(len(doc.attrs("link", rel="canonical")), 2)

    def test_escaped_json_ld_remains_data(self):
        payload = {"name": "A </script> & B"}
        serialized = json.dumps(payload).replace("<", "\\u003c")
        doc = seo.Document(f'<script type="application/ld+json">{serialized}</script>')
        self.assertEqual(doc.schemas, [payload])
        self.assertEqual(len(doc.attrs("script")), 1)

    def test_linked_images_are_assets_not_sitemap_pages(self):
        self.assertTrue(seo.is_image_asset('/floor-plans/example.jpg'))
        self.assertTrue(seo.is_image_asset('/photos/EXAMPLE.JPG?v=2'))
        self.assertFalse(seo.is_image_asset('/floor-plans'))
        self.assertFalse(seo.is_image_asset('/journal/photo-jpg'))

    def test_invalid_json_ld_fails(self):
        with self.assertRaises(json.JSONDecodeError):
            seo.Document('<script type="application/ld+json">{"bad":}</script>')


if __name__ == "__main__":
    unittest.main()
