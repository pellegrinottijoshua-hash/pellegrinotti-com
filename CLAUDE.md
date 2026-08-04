# jayl-studio — CLAUDE.md

Portfolio of Joshua Pellegrinotti (pellegrinotti.com). Static site, **no build step**.

## Deploy
- Push to `main` → Vercel deploys production **immediately**. There is no staging: every commit is live in ~1 minute.
- After any push, verify the live site before declaring done (fetch https://pellegrinotti.com and check the change).

## Files
- **`index.html` è la home** (inline CSS + JS, ~500 lines).
- **Sottositi IP** (statici, un index.html + assets ciascuno): `/therug/`, `/zack/`, `/dinos/` → live su pellegrinotti.com/therug ecc. I laboratori sorgente sono `~/therug-site`, `~/zack-site`, `~/dinos-site` (repo git separati): si lavora lì, poi si rsync-a qui per il deploy.
- La nav home: la voce "Code" all'hover/tap diventa "Jayl Brand" e apre la tendina coi 3 IP (la vecchia pagina Jayl Code non esiste più).
- `HANDOFF-fable5.md` documents architecture, assets, gotchas, TODOs — read it before big changes.
- `pellegrinotti-brief.md` — brand/content brief.

## Hero image system
- Desktop pool: `assets/hero/01.jpg … 25.jpg`; mobile pool: `assets/hero/mobile/01.jpg …`.
- The flip logic caps at `var N=11` (index.html:339). **Adding hero images requires bumping N**; images beyond N are dead weight.
- ⚠️ 25 images per pool are on disk but N is still 11, so `12.jpg … 25.jpg` (6.5 MB across both pools) never display. Bump N to 25 if they were meant to be in rotation.
- Images are referenced dynamically (`'assets/hero/'+pad(n)+'.jpg'`) — a grep for filenames will falsely mark them unused.

## Media
- **Every video is served from Cloudflare R2**, not from this repo: `MEDIA_BASE = https://media.pellegrinotti.com` (index.html). Upload with `scripts/upload-to-r2.sh`.
- `assets/*.mp4` are local staging copies before upload — `.vercelignore`d, so they never ship. Don't reference them from HTML; point at `MEDIA_BASE` instead.
- The sub-sites (`therug/`, `zack/`, `dinos/`) DO ship their own local clips under their own `assets/` — those are not ignored.

## Pending content (placeholders live in production)
- Social links (Instagram/LinkedIn) are `href="#"`.
