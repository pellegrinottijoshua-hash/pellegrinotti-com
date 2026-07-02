# pellegrinotti.com — project brief (for a fresh Claude Code chat)

Paste-ready context for working on **pellegrinotti.com**. Open the new chat with cwd = `~/jayl-studio`.

## What it is
**Joshua Pellegrinotti's personal-brand portfolio** — developer + director from Venice. AI films, code, and ads. **JAYL** ([jayl.store](https://jayl.store)) is his sub-brand, shown in the "Code" section.

## Stack & hosting
- **Pure static single `index.html`** — no build step, no `package.json`, no framework. Vanilla HTML/CSS/JS in one file (inline `<style>` + `<script>`). Three.js / interactive bits via CDN or hand-rolled canvas.
- **Repo:** `github.com/pellegrinottijoshua-hash/pellegrinotti-com` (**public**). **Vercel project `jayl-studio`** (legacy name) → **pellegrinotti.com** (apex) + `www`→apex 308 redirect. Auto-deploys on push to `main`.
- **Source folder:** `~/jayl-studio`. Edit `index.html` directly.
- **Assets:** `~/jayl-studio/assets/` — videos `lei-chi-e-web.mp4`, `therug1-3.mp4`, `demo-music.mp4`, `brandcontentengineex.mp4`, `duel.mp4`; `logo-light.svg`; `/favicon.png`. (`assets/lei-chi-e.mp4` is a 52MB master, git-ignored + vercel-ignored.)

## ⚠️ Local preview gotcha
A `python -m http.server` preview **doesn't support HTTP Range requests**, so the videos render **black locally** (Chrome needs ranges for media). They autoplay fine on Vercel. Use the **Chrome MCP** against the localhost server for reliable scrolled screenshots; the in-panel preview can wedge its viewport to width 1.

## Current design (v2) — the brief to preserve
**Hybrid of Aristide Benoist (minimal black) + Bruno Simon (a bit of interactivity).** Rules:
- **Minimal, near-black** background (`--bg:#050505`), off-white text, refined.
- **Gold (`--gold:#c9a24b`) ONLY on interaction** — hovers, the custom cursor, dots near the cursor. Default state is monochrome.
- **Interactive dot-grid hero** (canvas 2D): faint white dots; dots near the cursor brighten → gold and get pushed. Plus **custom gold cursor**, **magnetic buttons**, scroll-reveal.
- Type: **Archivo** (display + body), **JetBrains Mono** (labels/kickers). Bilingual **EN/IT** via `data-en`/`data-it` + a small toggle.

## Sections (6)
1. **Films** — `lei chi è` (featured) + The Rug I–III (uses the videos).
2. **Code** — editorial project list (Aristide/Snellenberg row-hover). Real: `jayl.store`, `pellegrinotti.com`. Placeholder row "More projects".
3. **AI Ads** — `brandcontentengineex.mp4` + copy.
4. **Who am I?** — 3 placeholder cards for **AI portraits of Joshua + a short story each** (TO FILL).
5. **My Ideas** — placeholder rows for upcoming projects (TO FILL).
6. **Your Ideas** — Snellenberg-style "Let's work together" + email **`pellegrinottijoshua@gmail.com`**.

## Placeholders to fill (need content from Joshua)
- **Who am I?** AI photos (files) + caption/story per photo.
- **Code** more site links: name · URL · 1-line desc · status.
- **My Ideas** upcoming projects: name · description · status.
- **Socials**: Instagram, LinkedIn URLs (currently `#` in nav/footer).

## Design references (for inspiration)
Bruno Simon, Aristide Benoist, Dennis Snellenberg, Lusion, Active Theory — plus more interactive sites the user is collecting. Direction = minimal-black-with-interaction, NOT maximalist.

## Editing notes
- Everything is in `index.html`. Colours are CSS variables in `:root`. i18n strings use `data-en`/`data-it` (the JS swaps `innerHTML`).
- To verify: serve the folder and screenshot via Chrome MCP; force-reveal sections with `document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))` before screenshots.
- **Deploy:** `git add index.html && git commit && git push origin main` → auto-deploy.

## History
Was "JAYL Studio — AI Video Artist & Director" (Venice art house, with prices). Rebuilt 2026-06-29 as the personal portfolio (prices removed). v1 was dark-cinematic + Fraunces + gold throughout; v2 (current) is the minimal-black Aristide×Bruno-Simon direction above.
