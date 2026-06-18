# Agent Readiness Log

Working notes for making **fullscope-media.com** discoverable/usable by AI agents,
driven by the checks at [isitagentready.com](https://isitagentready.com)
(`POST https://isitagentready.com/api/scan` with `{"url": "https://fullscope-media.com"}`).

Each check has a skill spec at
`https://isitagentready.com/.well-known/agent-skills/<check>/SKILL.md`.

Guiding principle: **advertise honest, real machine-readable resources.** These are
content/marketing pages with no API or agent backend, so we point agents at genuine
structured data (schema.org `LocalBusiness`) rather than fabricating an API catalog or
an agent endpoint that doesn't exist.

---

## ✅ Link response headers (RFC 8288) — DONE

**Check:** `checks.discoverability.linkHeaders` · skill: `link-headers`
**Issue:** Link headers were present (SvelteKit's own `modulepreload`/`preload`) but
carried no agent-useful relation types.

**Fix:** every HTML response now also advertises a machine-readable profile via a
`describedby` Link header pointing to a standalone schema.org document.

### Files
- `src/lib/business.ts` — **single source of truth** for the schema.org `LocalBusiness`
  object (`businessJsonLd`). Previously this object was inlined in the layout; extracted
  here so the same data feeds both the inline JSON-LD and the standalone resource.
- `src/routes/business.jsonld/+server.ts` — serves that object at `/business.jsonld`
  as `Content-Type: application/ld+json`.
- `src/hooks.server.ts` — `handle` hook that **appends** (never sets) this to HTML responses:
  ```
  Link: </business.jsonld>; rel="describedby"; type="application/ld+json"
  ```
  Appending preserves SvelteKit's existing preload Link headers. Gated on
  `content-type: text/html` so assets/data endpoints aren't tagged.
- `src/routes/+layout.svelte` — now imports `businessJsonLd` from `$lib/business.ts`
  instead of duplicating the object inline (removed the local `siteUrl` /
  `defaultDescription` / `defaultImage` consts, which were JSON-LD-only).

### Why `describedby` (and not `api-catalog`)
`api-catalog` (RFC 9727) advertises a list of APIs. This site has none, so pointing at a
fabricated catalog would be dishonest. `describedby` → real JSON-LD is the correct,
honest relation type and satisfies the skill (it accepts any of `api-catalog`,
`service-desc`, `service-doc`, `describedby`).

### Verification (the gotcha that matters)
Must be tested against a **production build**, not `npm run dev`. With `adapter-node`,
prerendered pages are served before `hooks.server.ts` runs — dev never prerenders and
always runs hooks, so dev can give a false pass. (Confirmed nothing in this project sets
`prerender`, so the hook does run for the homepage.)

```bash
# build needs dummy SMTP creds (see "build blocker" note below)
SMTP_USER=test@example.com SMTP_PASS=dummy npm run build
SMTP_USER=test@example.com SMTP_PASS=dummy PORT=4173 node build/index.js &
curl -sD - -o /dev/null http://localhost:4173/ | grep -i '^link:'
curl -sD - -o /dev/null http://localhost:4173/business.jsonld | grep -i content-type
```

**Result:** homepage Link header includes
`</business.jsonld>; rel="describedby"; type="application/ld+json"` appended after the
preload headers, and `/business.jsonld` returns `200` / `application/ld+json`. ✅

> Use `curl -sD -` (full GET, dump headers), not `-I` — HEAD can be handled differently.

---

## ⏳ DNS for AI Discovery (DNS-AID) — PENDING (infra, not repo)

**Check:** `checks.discoverability.dnsAid` · skill: `dns-aid`
**Spec:** [draft-mozleywilliams-dnsop-dnsaid](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/)
+ [RFC 9460 (SVCB/HTTPS)](https://www.rfc-editor.org/rfc/rfc9460)
**Issue:** no `_agents` well-known SVCB entrypoint records found.

This **cannot be done from the repo** — the records live in DNS and DNSSEC needs a
registrar action. It requires account access we don't have in this environment.

### Current DNS facts (via `dig` / `whois`)
| | |
|---|---|
| DNS host | **Cloudflare** (`arturo.ns.cloudflare.com`, `michelle.ns.cloudflare.com`) |
| Registrar | **GoDaddy** |
| DNSSEC | **OFF** (no DS at parent, no DNSKEY) |
| `_agents` records | none |
| Apex | Cloudflare-proxied (104.21.x / 172.67.x) |

### Plan
1. **Publish the entrypoint SVCB record** in Cloudflare (DNS-only):
   ```
   _index._agents.fullscope-media.com. 3600 IN SVCB 1 fullscope-media.com. alpn="h2" port=443 mandatory=alpn,port
   ```
   Cloudflare fields → Type `SVCB`, Name `_index._agents`, Priority `1`,
   Target `fullscope-media.com`, Value `alpn="h2" port=443`.
   - Honest target: points at the real website host with `alpn="h2"` (what's actually
     served), **not** the spec's `alpn="a2a"` example — we run no A2A/MCP agent.
     Swap to a real agent target/alpn if one is ever deployed.
   - Only registered SvcParams used (`alpn`, `port`, `mandatory`). The draft's
     `well-known` / `cap` / `policy` aren't IANA-registered, so they'd need
     experimental `keyNNNNN` numbers that most providers (incl. Cloudflare) reject.
2. **Enable DNSSEC:** Cloudflare → DNS → Settings → Enable DNSSEC → copy the DS record
   (Key Tag, Algorithm, Digest Type, Digest) → add it at **GoDaddy** → DNSSEC.
3. **Verify:**
   ```bash
   dig SVCB _index._agents.fullscope-media.com +short
   dig DS   fullscope-media.com +short          # appears after GoDaddy publishes
   dig +dnssec SVCB _index._agents.fullscope-media.com   # expect RRSIG + AD flag
   ```

### Optional repo follow-up (to make the entrypoint truthful)
Serve a real machine-readable agent index (e.g. `/.well-known/agents/index.json`)
listing the `/business.jsonld` profile, so the DNS entrypoint points at something that
actually responds. Not required for the scanner (DNS-only check), but honest.

---

## Build blocker note
`npm run build` fails type-check/build without `SMTP_USER` / `SMTP_PASS` because
`src/routes/contact/+page.server.ts` imports them from `$env/static/private`. The user
runs the real build with these set in `.env`; for header-only verification, dummy values
are fine (email isn't exercised).
