# Production deployment — September 14, 2026

The reviewed SEO patch was deployed to `https://fullscope-media.com` at **01:27:58 UTC** after explicit approval to deploy and push to GitHub.

The owner's recent www/apex fix was preserved. Host, redirect, canonical, sitemap, DNS, nginx, Cloudflare and GTM configuration were not changed. The September 12–13 redirect observations in the original audit are historical, not a claim about the corrected setup.

The deployment includes the Web Design description/content improvements, contextual links from About and Studio Photography, accessible service selection, the no-JavaScript content fallback, the process-counter styling correction, SEO regression tooling and audit documentation. Existing production breadcrumb work is recorded separately in commit `c8b8127`.

Validation before activation:

- Production environment and existing locked dependencies used in a separate build directory; no package upgrades.
- Typecheck: zero errors and zero warnings.
- Regression-tool unit tests: six passed.
- Production build: passed; adapter-node output completed.
- Staged HTTP regression: 29 routes, 603 referenced local image assets, zero failures.
- Browser: mobile layout and website-to-contact navigation passed; selecting SEO exposes the selected state and retains the form value. No inquiry was submitted.

Activation used a directory swap followed by restarting the existing `fullscope-media` PM2 process. Previous hashed client assets were retained so already-open pages can continue loading their assets. Origin health checks confirmed the new page content, and PM2 reported the application online.

Post-deployment checks:

- Public-domain regression: 29 routes, 603 referenced local image assets, zero failures.
- The live browser showed the new Web Design content and correct existing title.
- Live mobile rendering and client navigation from Web Design to Studio Contact passed without reported app errors.

Deployment logs, screenshots, before/after build backups and live regression results are in `/tmp/fullscope-deploy-20260914/`. The original complete build is retained in `previous-build/` and the replaced live build in `replaced-build/` there. The deployment did not exercise production email delivery or alter analytics settings.
