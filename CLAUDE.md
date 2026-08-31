# Project Context

## Stack
- **SvelteKit** (minimal template) with **Svelte 5**
- **TypeScript**
- **Vite** as bundler

## Setup Notes
- Package manager is **pnpm**, pinned via `packageManager` in `package.json`. Don't use
  npm here — it would create a `package-lock.json` that drifts from `pnpm-lock.yaml`
- Dependencies are installed (`node_modules` exists)
- `pnpm` is at `/opt/homebrew/bin/pnpm` and is on PATH for both the user's interactive
  terminal and the Bash tool (there is no corepack on this machine)
- pnpm blocks dependency install/build scripts by default. Approved ones are listed
  under `allowBuilds` in `pnpm-workspace.yaml` — currently `sharp`, which needs its
  install script to fetch a native libvips binary. If a new dep needs one, pnpm prints
  `ERR_PNPM_IGNORED_BUILDS`; add it there rather than disabling the check
- pnpm does not hoist, so anything imported must be a *declared* dependency. Packages
  that npm happened to hoist into place will fail here (this is why `@types/node` is an
  explicit devDependency)

## Dev Commands
```bash
pnpm dev       # start dev server
pnpm build     # production build
pnpm preview   # preview production build
pnpm check     # type-check with svelte-check
```
`build` and `check` need `SMTP_USER` / `SMTP_PASS` set (see `.env.example`) because the
contact routes import them from `$env/static/private`. Dummy values are fine when email
isn't being exercised:
```bash
SMTP_USER=test@example.com SMTP_PASS=dummy pnpm build
```

## Project Structure
```
src/
  app.html          — HTML shell
  routes/
    +page.svelte    — home page
static/             — static assets
svelte.config.js
vite.config.ts
tsconfig.json
```
