# Full Scope Media SEO audit — September 12–13, 2026

> Deployment update, September 14, 2026: the reviewed patch is now deployed. See [deployment record](deployment-20260914.md). The domain/redirect observations below are historical; the owner confirmed the www/apex issue has since been fixed, and this deployment makes no host or canonical changes.

The priority is a focused improvement to `/studio/web-design`, preserving the site's recent gains. The supplied September 4–10 GSC figures show 354 of 405 impressions on this page, mostly outside page one. Zero clicks at an average position of 33.19 does not establish a snippet problem. The rise from approximately 37.1 to 27.6 in weighted position supports restraint. Malformed queries and queries ending in “total” did not inform any content changes.

**Scope and source baseline**

The current production tree is `/var/www/fullscope-media`, not the older `/root/FSM/FSM` checkout. It was on `f88ac1c` with existing uncommitted breadcrumb changes. Work is isolated in `/root/fullscope-seo-20260912`, branch `seo/gsc-20260912`. Commit `fb7faf0` snapshots those existing changes as the audit baseline; they are not new work from this audit. Production source, processes, Cloudflare, nginx and GTM configuration were not modified or deployed. No production environment secrets were copied; local builds used dummy SMTP values.

Evidence: [live baseline for every route](baseline.json), [post-change route checks](route-audit.json), and [live redirect chains](redirects.json). Screenshots, raw HTML and command logs are preserved locally in `/root/fullscope-seo-evidence-20260912/`. Live observations were collected across September 12–13 UTC. GSC numbers are supplied evidence, not a new export fetched during this task.

**Findings, ranked**

| Priority | Finding | Disposition |
| --- | --- | --- |
| Critical | No critical indexability fault found in the 29 public sitemap pages. | All returned 200 with one title, description, H1 and absolute self-canonical. |
| High — opportunity | Web Design has most of the site's impressions. Existing copy offers real services but explains SEO through competitive claims and a broad ranking statement instead of clarifying the work. | Improved the existing section, description and buyer guidance. Kept the title and primary intent. |
| Medium | The live browser recorded two `gtm.js` data-layer initialization events, with the ordinary GTM request, a first-party `/bm8l/` gateway request and a `gtg_health=1` request. | External measurement review needed. The source has one bootstrap; the local build records one initialization even after client navigation. Duplicate GA4 pageviews were not established. |
| Medium | HTTP `www` and combined host/trailing-slash variants take two or three permanent redirects. | Documented edge follow-up; canonical URLs themselves return 200 without chains. Application canonical work left alone. |
| Medium | Without JavaScript, the eye overlay obscured the homepage's intended fallback; real-estate `.reveal*` elements remained transparent. Content was in SSR HTML but not visibly usable. | Added a narrowly scoped `noscript` style fallback. Existing animated design remains intact with JavaScript. |
| Medium | Global CSS is 1,180,871 bytes uncompressed (build gzip approximately 104 kB). `app.css` imports the complete prebuilt DaisyUI stylesheet. | Deferred a separate CSS reduction with full visual coverage of both branches. Current live transfer was about 56 kB in this browser run; raw size is not network transfer size. |
| Medium | Natural-height photo grids in `/photos` and city pages do not reserve image dimensions. Other large heroes/carousels have explicit container height/aspect ratio. | Follow-up: record actual per-image dimensions before adding attributes. Do not assume every photo is landscape; one selected image is 1024×1536. No speculative image resizing or quality changes. |
| Low | Web Design's `.steps`/`.step` classes collide with DaisyUI and produce a second set of counters and connecting lines. | Renamed only these local classes/selectors. All four process steps and their copy are preserved. |
| Low | Studio contact service buttons showed selection visually without exposing toggle state. | Added `aria-pressed` and a named group. Form submission behavior is unchanged. |
| Low | About did not explain the Studio branch; Studio Photography lacked a contextual website-project link. | Added two short contextual passages. No global footer link expansion. |
| Low | Current AVIF assets exist, but `scripts/process-images.mjs` only regenerates JPEG/WebP. It also duplicates the selected-photo inventory. | Maintenance follow-up; existing photographs and image files were preserved. |
| Low | The Chillax preload is global although only the photo layout uses that font; all routes also share the Google Fonts request. | Record for a separate font-loading change. Existing font appearance and preconnects preserved. |
| No action / already correct | Metadata, robots, sitemap membership/hostname, real 404s, shared business identity, current breadcrumb output, journal schema and contextual service links. | Preserved; protected by rendered checks. |

**Implementation map, inspected before editing**

| Concern | Current implementation and audit result |
| --- | --- |
| Framework/routing | Svelte 5 + TypeScript, SvelteKit 2, Vite 8, adapter-node. Root gateway plus `(photo)` and `(studio)` route groups; groups do not appear in public URLs. Installed locked versions used for validation: Svelte 5.55.5, SvelteKit 2.59.1, Vite 8.0.10. |
| Rendering | SSR with client hydration; no `ssr=false`, `csr=false` or prerender override found. Dynamic city/property/journal `+page.ts` loaders use repository data and return real 404s for missing records. Main content and links exist in the server response. |
| Shared head | `$lib/Seo.svelte` owns the title, description, robots, canonical, Open Graph and Twitter tags. Individual routes supply metadata. Root layout renders the business and existing shared breadcrumb JSON-LD; route-group layouts supply chrome and one main landmark. |
| Canonical | `$lib/business.ts` exports `https://fullscope-media.com`; `Seo.svelte` combines it with the route pathname, excluding queries. Default trailing-slash normalization occurs before page rendering. All 29 canonical targets return 200. No duplicate tags or host-dependent canonical generation found. |
| Robots | Static `static/robots.txt`: allow public pages, disallow `/api/`, canonical sitemap reference. `Seo.svelte` emits `index, follow`; no conflicting meta or response-header noindex/nofollow on indexed routes. Error pages return 404 rather than a 200 empty page. |
| Sitemap | `src/routes/sitemap.xml/+server.ts`: 19 static URLs, 2 city pages, 5 property galleries and 3 articles, sourced from the same data inventories as pages. No redirected, noindexed or missing entries found; no fabricated request-time `lastmod`. |
| Structured data | Shared LocalBusiness `https://fullscope-media.com/#business`, service catalog/provider references, a Web Design Service, existing BreadcrumbList, BlogPosting on each article and existing FAQPage data on the two FAQ routes. Every emitted JSON-LD block parses. No rating/review schema found. |
| Social metadata | One `og:url` matching each canonical; absolute social images, shared readable brand name and Twitter large-image cards. External editorial image hosts are appropriate external URLs, not hostname inconsistencies. |
| Internal links | All 29 sitemap routes are reachable from `/` by normal anchors. `/studio/web-design` already has a direct homepage link, a real-estate landing-page link, Studio service-card/header/footer links, and FAQ links. It is one click deep, not orphaned. |
| Redirects/proxy | No host redirect in `hooks.server.ts`; that hook only appends a `describedby` header. PM2 binds Node to `127.0.0.1:3000` with canonical `ORIGIN`. nginx passes Host and forwarded headers. Its HTTPS server accepts both hosts; the public www redirect is at Cloudflare. nginx's HTTP rules retain `$host`, so edge and origin behavior must be considered together. |
| Analytics | One async GTM-N8RVSFDH bootstrap and its noscript iframe in `app.html`; no additional layout initializer, direct GA4 bootstrap or manual pageview dispatch found. SMTP/contact code runs on the server. Live Cloudflare additionally rewrites fonts, decodes emails, adds its beacon and loads the tag gateway. No CSP blocking appeared in the tested browser flow. |
| Images | `<picture>` AVIF/WebP/JPEG sources and 800/1400/2000 candidates; high-priority heroes are not lazy-loaded. Real-estate landing hero preload matches its AVIF source. Below-fold images generally lazy-load. All images have alt attributes; empty thumbnail alt text accompanies labeled controls. All 603 locally referenced image candidates exist and are not LFS pointers. |
| Fonts/assets | Self-hosted WOFF2 Chillax with `font-display: swap`; Google Fonts request uses `display=swap` with Google preconnects. The root EyeGate module is shared for its cross-route animation; no hydration-wide refactor was attempted. |

**What changed and why**

Paths below are relative to the repository root. GSC justifies prioritizing the website inquiry flow and adding useful explanations; it does not directly prove the accessibility or CSS defects, which were verified in source/browser output.

| File | Previous behavior | New behavior and rationale |
| --- | --- | --- |
| `src/routes/(studio)/studio/web-design/+page.svelte` — description | Accurate but generic description of responsive/performance-focused development. | 159-character description identifies hand-built work, both cities, small businesses and SEO foundations, and invites visitors to inspect inclusions/process. A concrete click reason for the dominant GSC landing page without a ranking promise. |
| Same file — SEO section | Competitive “selling reports” language and an unspecific statement about the site's rankings. | Explains crawlability, titles/metadata, appropriate structured data, indexing, customer questions, service-area information, Google Business Profile and continuing content/measurement work. Clarifies the service already offered in the FAQ, catalog and contact options. |
| Same file — deliverable bullet | “Location & service landing pages.” | “Useful service & local project pages.” Emphasizes real services/work, consistent with the existing local galleries rather than indiscriminate location-page creation. |
| Same file — buyer guidance | No concise explanation of project fit or the existing-site review decision on this page. | Adds one section explaining small-business fit, custom development, mobile/keyboard behavior, reviewing existing sites, and the hosting/maintenance/analytics conversation. Adds a natural contextual inquiry link. No prices, timelines, client counts or guarantees added. |
| Same file — process CSS | DaisyUI added redundant counters/lines through generic class names. | Uses scoped `project-steps`/`project-step` names. Browser confirms all four pseudo-counters are `none`; existing four-stage content remains. |
| `src/routes/(photo)/about/+page.svelte` | Entirely photo-oriented company introduction. | Adds one short paragraph linking Studio and Web Design, helping visitors understand the umbrella business. Keeps all existing real-estate copy, title, description and photography. |
| `src/routes/(studio)/studio/photography/+page.svelte` | Website use was mentioned without a contextual service link. | Adds a short website-and-shoot planning passage linking custom web design. The link serves a buyer need already described in the photography offering. |
| `src/routes/(studio)/studio/contact/+page.svelte` | Service chips had only visual selected styling; group label was unassociated. | Associates the label and exposes selected state with `aria-pressed`. Verified the selected SEO value still appears in FormData. |
| `src/app.html` | Existing homepage fallback and real-estate reveal content could be visually inaccessible without JavaScript. | A `noscript` stylesheet hides the eye overlay and makes reveal content visible. GTM scripts, noscript measurement iframe, fonts and normal animation behavior are unchanged. |
| `scripts/seo-check.py` | No rendered SEO regression suite. | Standard-library Python checks the production HTML of every sitemap page, unique metadata, canonical/social/schema URLs, robots, breadcrumb hierarchy, normal links/fragments, sitemap coverage, local image files, one source GTM bootstrap, query canonicals, slash redirects and unknown-route 404s. Fails nonzero on errors. |
| `scripts/test_seo_check.py` | No unit coverage of the regression tooling. | Six tests cover robots rule precedence/group selection, rendered text/metadata parsing, duplicate canonical detection and valid/invalid escaped JSON-LD. The robots precedence test prevents Python's first-match REP behavior from falsely flagging the existing correct robots file. |
| `package.json` | Only existing build/check/image scripts. | Adds `test:seo` and `test:seo:unit`. No package dependencies or lockfile changes. Python 3 is required only for these checks. |
| `docs/seo-20260912/` | No record of this audit. | This report plus before/after route inventories and the live redirect matrix. |

Title retained exactly (59 characters): `Web Design in Lansing & East Lansing, MI | Full Scope Media`.

New description: `Hand-built websites for Lansing & East Lansing small businesses, with fast pages and SEO foundations. See what's included, how we work, and how to get started.`

**Host and canonical conclusions**

HTTPS www → non-www is already correct: a permanent 301, preserving paths and query parameters. HTTP → HTTPS also works. These observations do **not** mean every variant is one hop:

| Requested variant | Observed sequence |
| --- | --- |
| HTTPS www homepage or normal service path | 301 → canonical HTTPS non-www → 200 |
| HTTP non-www homepage or normal service path | 301 → canonical HTTPS non-www → 200 |
| HTTP www | 301 → HTTPS www → 301 → HTTPS non-www → 200 |
| HTTPS www service path with trailing slash | 301 → HTTPS non-www with slash → 308 → slashless path → 200 |
| HTTP www service path with trailing slash | 301 → HTTPS www → 301 → HTTPS non-www with slash → 308 → slashless path → 200 |

Repeated `ref` parameters and encoded `a%2Fb` were preserved throughout the recorded chains. Canonicals correctly exclude tracking queries. Sitemap and all indexable self-canonicals already use the correct hostname, and Open Graph/structured-data business URLs match it. None of those implementations were changed. The four historical www impressions are not evidence that this cleanup failed. Google describes redirects and canonical links as signals that can work together; consistent current signals are the appropriate engineering check. [Google canonical guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

Initial requests with Python's default User-Agent received Cloudflare 1010/403 responses. Normal browser-UA requests and Chromium loaded the pages successfully. This is not evidence that Googlebot is blocked; actual Googlebot access requires verified crawler logs or Search Console URL inspection.

**Real-estate and Journal decisions**

Lansing and Okemos share a layout, not interchangeable body content. Lansing discusses its neighborhoods and links actual `1904-carvel-ct-lansing-mi-48910` work; Okemos discusses different local context and links `4442-greenwood-dr-okemos-mi-48864`. Both have unique titles/H1s, correct canonicals, inherited business/breadcrumb data, booking/pricing links and links to their complete local galleries. Shared photo navigation/footer already link photography, floor plans, 3D tours, portfolio and contact. No new city pages or city body-copy changes were justified.

The three Journal articles have unique metadata, one H1, coherent H2 sections, a visible business byline linking About, BlogPosting data, image dimensions, contents anchors and related commercial links. Preparation links to booking, photography and pricing; the floor-plan guide links to the service/example and pricing; the interiors guide links to portfolio, photography and booking. All appear in the Journal, sitemap and normal link graph. The instructional content contains no dated market statistics needing an update. No new articles or forced Studio links were added.

Publication dates are explicitly absent in the content model until actual dates are recorded. Adding guessed `datePublished`/`dateModified` would be worse than preserving that omission. Existing FAQ schema reflects visible questions; no FAQ rich-result expansion, review schema, AggregateRating, duplicate Organization, new location entity or speculative Service graph was added. The business's city-level address, phone, name and provider IDs are consistent with visible contact information; precise geo coordinates and the full claimed service-area list were not independently authenticated as business facts.

**Validation**

| Check | Exact final result |
| --- | --- |
| `pnpm check` | PASS — svelte-check: **0 errors, 0 warnings**. Includes TypeScript and Svelte accessibility diagnostics. |
| Existing formatter | Not configured; no formatter script/configuration found. Existing style was retained; `git diff --check` passes. |
| Existing linter | Not configured; no lint script/configuration found. Do not interpret this as an ESLint pass. |
| Existing unit/integration suites | None configured before this task. |
| `pnpm test:seo:unit` | PASS — **6 tests**, including seven robots subcases. |
| `pnpm test:seo --output …` against adapter-node build | PASS — **29 routes; 603 image assets; 0 failures**. |
| `pnpm build` | PASS — Vite production client/server build and adapter-node output complete, exit 0. Final server build stage 42.82 seconds. Vite reported plugin-timing warnings; these are build-speed warnings, not runtime/SEO errors. |
| Browser | PASS — desktop 1280×900 and mobile 390×844 Web Design, inquiry navigation, selected service state, one canonical/H1, no duplicate process counters, and no app errors in the completed local flow. Mobile document width equals viewport width (390 px). |
| Preserved routes | Browser checks of About, Studio Photography, both city pages, an article and the homepage; no loaded broken images reported. All 29 routes separately checked via SSR HTTP. |
| No JavaScript | Browser launch with script execution disabled: homepage shows meaningful main content and all three destination links; real-estate service content/links remain visible. |
| Analytics | Local build: one GTM initialization before and after inquiry navigation. Production: two initialization events as noted above; no GA4 `collect` requests observed in this session, so pageview delivery/deduplication is unverified. No valid inquiry or email was submitted. |

A single unthrottled local browser observation recorded an H1 LCP at 3,784 ms and observed layout-shift sum 0.00749. This is diagnostic evidence, not field Core Web Vitals, a Lighthouse score, or a before/after improvement claim. Local requests do not include the production Cloudflare font/CSS behavior. No reliable field INP measurement was available. Existing shared CSS/font loading, photo-grid dimensions and carousel loading deserve measured follow-up.

Environment notes: pnpm 11.24.0 was available in the local Corepack cache, not initially on PATH. The existing lockfile/dependencies were restored offline. The first concurrent check/build attempt hit pnpm's automatic installation race; validation was rerun serially with automatic dependency verification disabled after the offline install. A temporary server lifetime interrupted an early browser click; the completed run owns its server through the entire test. Neither failure required application changes. Final logs and the successful browser run are in the evidence directory.

To reproduce from the repository with pnpm 11.24.0 on PATH:

```sh
pnpm install --frozen-lockfile
SMTP_USER=test@example.com SMTP_PASS=dummy pnpm check
pnpm test:seo:unit
SMTP_USER=test@example.com SMTP_PASS=dummy pnpm build
HOST=127.0.0.1 PORT=4173 ORIGIN=http://127.0.0.1:4173 node build/index.js
# In another terminal, while that server stays running:
pnpm test:seo --output /tmp/fullscope-seo-results.json
git diff --check
```

The regression script validates the current site's public HTML and local assets; it is not a full schema eligibility validator, security scanner, field-performance monitor or replacement for testing edge redirects. The integration check covers rendered JSON-LD rather than rewriting the existing serializer.

**Deliberately left alone**

- Existing Web Design title, H1, hero copy, four process descriptions, real website proof link and FAQ destination.
- Canonical helper/host, sitemap generator and membership, robots.txt, existing breadcrumb cleanup, business schema and social URLs.
- Real-estate titles/descriptions and body copy on the ranking service and city pages. About only gains the contextual Studio paragraph.
- Photography files, quality, responsive format sources and LCP image preloads.
- GTM initialization and measurement attributes, SMTP behavior, Cloudflare and nginx configuration.
- Existing Journal articles and honest omission of unknown publication dates.
- No `/studio/seo`, extra location pages, exact-match query lists, malformed-query targeting, “total” keywords, invented prices/credentials/testimonials/case studies or rating schema.

**Remaining decisions and follow-up**

Business judgment:

1. Define whether standalone ongoing SEO has a distinct deliverable/process worth a separate page. The repository confirms SEO is offered, but does not provide enough nonduplicative scope or proof to build a useful standalone service page now.
2. Supply permissioned web-project examples with the actual brief, work performed and outcomes. Until then, the site's own build is the honest example; property galleries are not presented as client website case studies.
3. Confirm actual Journal publication dates and precise business geo/service-area facts before enriching those fields. Do not infer publication from a Git timestamp or replace the service-area business with a fabricated street address.
4. Future content should answer recurring client decisions, such as choosing an existing-site improvement versus a rebuild or preparing content/photos for a website project, using the business's actual process and examples.

Engineering/operations:

1. Review Cloudflare Google Tag Gateway and GTM settings together. Inspect whether automatic tag setup and the source bootstrap both start the container; use Tag Assistant/GA4 DebugView to verify one intended pageview per navigation before removing anything. The first-party request is consistent with gateway operation, which Cloudflare documents as serving Google scripts and measurement through the site's domain. This is an inference from the observed requests, not a read of the account configuration. [Cloudflare gateway documentation](https://developers.cloudflare.com/google-tag-gateway/)
2. Consolidate protocol+host normalization at the edge: for HTTP or www requests, return a permanent redirect directly to `https://fullscope-media.com` plus the original path and complete query. Test rule ordering against HTTPS enforcement. For known slashless page routes, combine trailing-slash normalization where safe; preserve static directories, encoded paths and queries. The recorded matrix is the acceptance baseline. Avoid adding an application-layer redirect that creates another hop behind Cloudflare.
3. Reduce CSS only after auditing the DaisyUI components actually used and verifying both branches in screenshots. Scope unused font preloads in the same measured performance follow-up, not by changing typography.
4. Generate real image-dimension metadata for the natural-height grids, preserve portrait ratios, verify truthful `srcset` widths when `withoutEnlargement` applies, and bring AVIF generation into the existing image pipeline. Do not regenerate/recompress the current gallery without visual comparison.
5. Schedule `pnpm test:seo` against the built server in existing CI if/when CI is introduced. Keep the captured edge checks separate because localhost cannot verify Cloudflare's redirect behavior.
6. After deploying the reviewed patch, verify live rendering once, record the deployment date, and compare equivalent GSC periods for this page's legitimate web-design/SEO queries. Segment malformed query noise; monitor the real-estate pages separately. Do not repeatedly rewrite the title during the current ranking test or claim page-one movement before observing it.

**Diff review**

Reviewed against `fb7faf0`, the snapshot of actual production source. No dependency/lockfile updates, global formatting, canonical refactor, duplicate service content or image changes. The only class rename fixes a demonstrated DaisyUI collision. Tests use the standard library; generated Python cache files were removed. `git apply --check` confirms the exported patch applies cleanly to the current `/var/www/fullscope-media` tree, preserving its pre-existing changes. The patch is saved at `/root/fullscope-seo-evidence-20260912/changes.patch`. It is ready for source review and deployment through the normal production workflow; no deployment was performed in this task.
