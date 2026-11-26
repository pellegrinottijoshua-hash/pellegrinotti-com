# jayl-studio — CLAUDE.md

Portfolio of Joshua Pellegrinotti (pellegrinotti.com). Static site, **no build step**.

## Deploy
- Push to `main` → Vercel deploys production **immediately**. There is no staging: every commit is live in ~1 minute.
- After any push, verify the live site before declaring done (fetch https://pellegrinotti.com and check the change).

## Files
- **`index.html` è la home** (inline CSS + JS, ~830 lines).
- **Sottositi IP** (statici, un index.html + assets ciascuno): `/therug/`, `/zack/`, `/dinos/` → live su pellegrinotti.com/therug ecc.
  - ⚠️ **Dal 26/11/2026 `zack/` e `therug/` si modificano QUI** (ramo `home-v3`). I vecchi laboratori `~/zack-site` e `~/therug-site` sono rimasti indietro: **non fare più rsync da lì**, cancellerebbe le schede nuove. `~/dinos-site` resta com'era.
  - **Zack v3:** si apre con gli occhi vivi (`zack/occhi/` è una copia di `zack the duck/motion-lab/home-occhi/`; se cambia lì, ricopiarla). Poi premessa con la linea d'oro che si disegna allo scroll, collezione arte e cibo che scorre di lato, cast di 6 (tartaruga compresa), gag a nastro, libro Art for Kids, merch. Font Montserrat (quello di Zack). Canone: Zack non fa versi.
  - **The Rug v3:** targa sul tramonto con polvere dorata, il protagonista (poltrona, sheet, primo piano), la città che scorre di lato, il film dell'EP1 (invariato), lo schiaffo guidato dallo scroll (6 frame, lampo al contatto), gli invasori coi nomi di canone (Boss, Right, Left, Gag, Rock, A1 morto), i poster.
  - Immagini nuove in `zack/assets/v3/` e `therug/assets/v3/`, ricompresse da `scripts/prepara-asset-v3.py` (`/usr/bin/python3 scripts/prepara-asset-v3.py`) (lato lungo 720-2000 px, JPEG q80).
- **Home v3 (25-26/11/2026, ramo `home-v3`)** — niente più servizi né prefisso "Jayl". Le facce dei brand (decise da Joshua):
  - **JP** = Joshua: in alto a sinistra, nella scritta che scorre e nel fondo pagina. È una maschera CSS (`.jp`, file `assets/logos/jp.svg`). Il logo JP è **ancora in studio** (`~/Desktop/Jayl brand/loghi/JP/`): quando è scelto si sostituisce quel file (e il rapporto 1021/500 in `.jp`). Ora c'è la v4 scelta (`jp4.SCELTA`: 4 basi, J-P ½, piede 2, braccio 2½), file da `loghi/JP/jp4.py`.
  - **Cinque righe in `.projs`, solo icona tonda + titolo, niente descrizioni** (Joshua 26/11): Zack the Duck (icona simbolo, scritta di Zack su una riga `assets/logos/zack-scritta-riga.svg` ricomposta dai tracciati originali), Italy's Protagonists (IP nel cerchio ↔ P "faccia" su acqua al passaggio del mouse; scritta ufficiale `assets/logos/protagonists.svg`; riga senza link finché il loro sito non è pubblico), The Rug (logo in pelle nel cerchio, titolo come prima), Jayl Studios (J-play, apre Instagram @jayl_studios), jayl.store (scritta jayl, apre lo store). Icone in `assets/coins/`.
  - In fondo il contatto con mail, Instagram, YouTube @jayl. `assets/js/lightbox.js` non è più incluso dalla home. Dinos resta in pausa.
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
