# Project Context

## Stack
- **SvelteKit** (minimal template) with **Svelte 5**
- **TypeScript**
- **Vite** as bundler

## Setup Notes
- Dependencies are installed (`node_modules` exists)
- `npm` is available in the user's interactive terminal via corepack shims at `/usr/share/nodejs/corepack/shims`
- The Bash tool shell does **not** have `npm` in PATH — use the full path `/usr/share/nodejs/corepack/shims/npm` for any tool-executed npm commands

## Dev Commands
```bash
npm run dev       # start dev server
npm run build     # production build
npm run preview   # preview production build
npm run check     # type-check with svelte-check
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
