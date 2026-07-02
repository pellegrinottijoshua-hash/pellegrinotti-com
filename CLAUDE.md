# jayl-studio — CLAUDE.md

Portfolio of Joshua Pellegrinotti (pellegrinotti.com). Static site, **no build step**.

## Deploy
- Push to `main` → Vercel deploys production **immediately**. There is no staging: every commit is live in ~1 minute.
- After any push, verify the live site before declaring done (fetch https://pellegrinotti.com and check the change).

## Files
- **`index.html` is the entire live site** (inline CSS + JS, ~450 lines). Edit this file only.
- `HANDOFF-fable5.md` documents architecture, assets, gotchas, TODOs — read it before big changes.
- `pellegrinotti-brief.md` — brand/content brief.

## Hero image system
- Desktop pool: `assets/hero/01.jpg … 25.jpg`; mobile pool: `assets/hero/mobile/01.jpg …`.
- The flip logic caps at `var N=25` (in index.html). **Adding hero images requires bumping N**; images beyond N are dead weight.
- Images are referenced dynamically (`'assets/hero/'+pad(n)+'.jpg'`) — a grep for filenames will falsely mark them unused.

## Pending content (placeholders live in production)
- `storeBody()` and `whoBody()` render Italian scaffolding text — real content (Store from jayl.store, Who am I) still to be written.
- Social links (Instagram/LinkedIn) are `href="#"`.

## Known follow-ups
- `assets/iconaj2.svg` (contact badge) is ~3.8MB — needs SVGO/rasterization.
- `assets/work/lei-chi-e-web.mp4` is 22MB — needs re-encoding (master 52MB is `.vercelignore`d).
