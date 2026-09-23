# jayl-studio — CLAUDE.md

Portfolio of Joshua Pellegrinotti (pellegrinotti.com). Static site, **no build step**.

## Deploy
- Push to `main` → Vercel deploys production **immediately**. There is no staging: every commit is live in ~1 minute.
- After any push, verify the live site before declaring done (fetch https://pellegrinotti.com and check the change).

## Files
- **`index.html` è la home** (inline CSS + JS, ~830 lines).
- **Sottositi IP** (statici, un index.html + assets ciascuno): `/therug/`, `/zack/`, `/dinos/` → live su pellegrinotti.com/therug ecc. I laboratori sorgente sono `~/therug-site`, `~/zack-site`, `~/dinos-site` (repo git separati): si lavora lì, poi si rsync-a qui per il deploy. **Escludere i `.md`** dal rsync: sono doc del repo sorgente, non file del sito.
  ```
  rsync -a --delete --exclude '.git' --exclude '.DS_Store' --exclude '*.md' ~/zack-site/ zack/
  ```
- **Nav home** — tre righe in `<section class="list">`, tutte con il reveal di `Jayl` in hover (la regola CSS è su `.row`, non su `a.row`, quindi vale anche per le righe statiche):
  1. `Jayl Services` — etichetta statica + `.branddrop` sempre aperta con "your brand" (spot fermentati) e "your song" (Lei chi è). I due `<button class="svc-open">` chiamano `openPlayer()`. **`your brand` viene prima ed è più grande**: i video musicali sono portfolio, non reddito (vedi `pellegrinotti-services.md`). Aggiungere un terzo servizio = un altro blocco `.svc`.
  2. `Jayl Original IPs` — etichetta statica senza sottotitolo + tendina con The Rug e Zack. **Dinos & Mages è in pausa**: la riga `<a class="ip ipdinos">` è tolta ma il CSS e `/dinos/` restano, quindi si ripristina con una riga di markup.
  3. `Jayl Store` — unica riga cliccabile (`data-target="store"`), apre jayl.store.
- **Player video condiviso** — `assets/js/lightbox.js`, API `openPlayer({src,title})`: overlay a tutto schermo, audio ON, `preload="none"`, chiusura con ESC/backdrop/×, `src` svuotato alla chiusura (Lei chi è pesa 22 MB). Markup e CSS sono dentro il JS. ⚠️ **Ne esistono due copie identiche**, una per repo (`jayl-studio/assets/js/` e `zack-site/assets/js/`), perché i due siti si sviluppano separati e non c'è build step: se ne modifichi una, allinea l'altra.
- **Niente GSAP**: rimosso quando è sparito l'overlay `detail` che era l'unico a usarlo. Non reintrodurlo senza motivo.
- `HANDOFF-fable5.md` documents architecture, assets, gotchas, TODOs — read it before big changes.
- `pellegrinotti-brief.md` — brand/content brief.

## Type scale
- Every size, tracking and display leading on the home page comes from tokens in `:root` (`--t-micro … --t-xl`, `--tr-caps`/`--tr-mono`, `--tr-tight`/`--tr-tighter`, `--lh-display`/`--lh-hero`). **Don't add a bare `font-size` or `letter-spacing` to the home page** — pick a step, or add one.
- Two deliberate exceptions: the marquee (`.mtrack span`) is a motion band, not a heading, and the `.jbadge` SVG circular text. Zodiak keeps its own `-.005em` because serif tracking doesn't follow the sans steps.
- `--muted`/`--faint` are chosen against two backgrounds: bare `--bg` **and** the worst frame the fixed reel can put behind them. Lightening the veil means re-checking them.

## The stage (fixed video backdrop)
- The hero clips live in `<div class="stage">`, the **first element in `<body>` and outside `.hero`** — as a hero child they were clipped to the first viewport and scrolled away. Everything else sits on `z-index:1`.
- Two knobs, both on `.stage`: `--p` (0→1 over the first viewport, ramps `.stage-veil`) and the `.deep` class (blurs + dims the footage past the hero, with hysteresis). `--dim`/`--veil` are set per viewport — phones keep the footage present, desktop pulls it back.
- The blur is a **class toggle, not a calc() off `--p`**: animating a filter value per scroll frame forces a shader recompile per frame on mobile.
- The backdrop is **one merged reel** (`hero/reel.mp4` on R2, 720×1280, 38 s, 0.4 s crossfades, audio kept for the Sound toggle) that loops — not eleven clips swapped by JS.

## Hero reel
- Built with ffmpeg from `assets/hero/mobile-video-src/01–11.mp4` (`xfade` + `acrossfade`, 0.4 s). Local copy: `assets/hero/reel.mp4` + `reel-poster.jpg`; uploaded by `scripts/upload-to-r2.sh`.
- **Re-cutting the reel means bumping `REEL_V` in index.html** — R2 objects are `immutable`, a same-name re-upload is served stale otherwise.
- The old per-clip files (`hero/mobile-video/NN.mp4`) and desktop stills (`hero/NN.jpg`) stay on R2 but the page no longer reads them (except `hero/01.jpg` for og:image).

## The Rug episode film
- `therug/assets/story/ep1-film.mp4` is the seven former shots (s01–s07) merged into one 40 s film (1100×618, 0.5 s crossfades, 2.33:1 shots letterboxed in the page's leather colour). One `<figure class="film">` plays muted while in view. It replaced seven stacked 100svh scenes.
- Lives in `therug/` (ships with the site). The source lab is `~/therug-site`: **rsync from here will not overwrite it, but copy the new page/film back there or the next rsync will resurrect the seven scenes.**

## Media
- **Every video is served from Cloudflare R2**, not from this repo: `MEDIA_BASE = https://media.pellegrinotti.com` (index.html). Upload with `scripts/upload-to-r2.sh`.
- `assets/*.mp4` are local staging copies before upload — `.vercelignore`d, so they never ship. Don't reference them from HTML; point at `MEDIA_BASE` instead.
- The sub-sites (`therug/`, `zack/`, `dinos/`) DO ship their own local clips under their own `assets/` — those are not ignored.

## Pending content (placeholders live in production)
- Social links (Instagram/LinkedIn) are `href="#"`.
