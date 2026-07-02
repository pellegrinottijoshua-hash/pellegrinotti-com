# pellegrinotti.com — handoff (per nuova chat / Fable 5)

Brief operativo per continuare il sito **pellegrinotti.com** (portfolio di Joshua Pellegrinotti, alter‑ego **JAYL**).
Apri la nuova chat con **cwd = `~/jayl-studio`**.

## Cos'è
Portfolio personale, nero, editoriale‑interattivo stile **Snellenberg / Cuberto / Aristide**.
Joshua = developer + director + brand designer da Venezia. **JAYL** è il suo brand/alter‑ego
(store: https://jayl.store), rivelato al hover sul nome.

## Stack & deploy
- **Un solo file: `index.html`** (statico, niente build, niente package.json). CSS inline + JS inline.
- Librerie via CDN: **GSAP** (transizioni tenda). Font: **Satoshi** + **JetBrains Mono** (Fontshare).
- Repo: `github.com/pellegrinottijoshua-hash/pellegrinotti-com`. Vercel project **jayl-studio** → **pellegrinotti.com**.
- **Auto‑deploy su push a `main`.** `index.html` è la home live. `proto.html` è una copia di lavoro identica.

## Asset
- `assets/hero/01..25.jpg` — 25 ritratti AI in stili diversi (desktop, landscape 1400×594).
- `assets/hero/mobile/01..31.jpg` — 31 ritratti verticali (mobile, 1080×1935).
- `assets/hero/MOBILE-PROMPT.md` — master prompt per generare nuove versioni mobile (Nano Banana).
- `assets/iconaj2.svg` — faccia di Joshua per il badge contatto (SVG, ~4MB).
- `assets/logo-light.svg` — logo JAYL. ⚠️ **è NERO**: nel CSS va usato con `filter:invert(1)` per renderlo bianco.
- `assets/*.mp4` — video (lei‑chi‑e‑web, therug1‑3, duel, brandcontentengine, demo‑music). `lei-chi-e.mp4` (52MB) è git/vercel‑ignored.

## Stato attuale — HOME completa e live
- **Hero**: foto random a schermo intero. **Flip carta 3D (rotateY)** verso un'altra foto random al **scroll‑giù** (si ri‑arma tornando in cima) e al **tap/click**. Immagini device‑aware (25 desktop / 31 mobile) con fallback mobile→desktop.
- **Mark top‑left** `Joshua Pellegrinotti` (oro) → hover(desktop)/click(mobile) fa **dissolvenza semplice nel logo JAYL** bianco, centrato sopra la larghezza del nome. (Niente più glitch RGB.)
- **3 ruoli** `AI Director / Developer / Brand Designer` (center‑left). Nome bianco gigante che **scorre** (marquee), ridotto su mobile.
- **Lista 4 righe**: Video / Code / Store / Who am I?. Hover → testo scivola a destra e compare **`Jayl` in oro** (es. "Jayl Video"). "Who am I?" → *"I am Joshua Pellegrinotti, but you can call me Jayl."* Su mobile: primo tap rivela, secondo naviga.
- Click riga → **transizione tenda nera + lampo oro** (GSAP) verso la pagina di dettaglio.
- **Work Together**: ultima sezione grande stile Snellenberg (faccia + "Get in touch" oro + email/jayl.store).
- **Badge contatto** bottom‑right: `iconaj2.svg` + "contact • contact" che ruota (SVG) → scrolla a #wt.
- **Cursore Aristide** (dot + ring) su desktop.

## Pagine dettaglio (predisposte)
- **Video** (`videoBody`): lista verticale video, B/N sfocato → colore all'hover → play al click, con descrizioni ("how it started → how it's going"). Usa i .mp4 esistenti. **Da arricchire con i video reali mancanti** (one‑shot, "venuti male").
- **Code** (`codeBody`): griglia servizi (siti, app, brand, AI tooling) + CTA. Testo migliorabile.
- **Store** (`storeBody`): **STUB** — importare filosofia brand + immagini prodotto da https://jayl.store, aggiungere griglia drop.
- **Who am I** (`whoBody`): **STUB** — foto (scegliere da `jayl versions`) + storia.

## Prossimi passi (TODO)
1. **Store**: contenuti reali da jayl.store (filosofia + immagini).
2. **Video**: aggiungere i video mancanti + descrizioni.
3. **Who am I**: foto + racconto.
4. Rifinire testi **Code** (renderlo vendibile) e social reali (Instagram/LinkedIn = `#`).
5. Eventuale ripulitura: rimuovere codice WebGL morto nel blocco hero (dopo `return;`), rimuovere `sphere-lab.html`/`proto.html` se non servono.

## Gotcha / note tecniche
- **Preview headless (pannello Launch) CONGELA `requestAnimationFrame` e le transizioni CSS** dopo 1 frame: il flip e le animazioni NON si vedono lì → **verificare sempre su browser reale** (`http://localhost:<porta>/` o il sito live). I `setTimeout` invece girano (usati per lo swap del flip).
- `logo-light.svg` è nero → `invert(1)`.
- Immagini pesanti: ottimizzate con `sips` (desktop `-Z 1400`, mobile `--resampleWidth 1080`, JPEG q74).
- Il pannello preview a volte incastra il viewport a width 1 → fare `preview_resize` esplicito.

## Come lavorare
- Edita **`index.html`** (colori = CSS variables in `:root`; oro `--gold:#c9a24b`).
- Deploy: `git add … && git commit && git push origin main` → auto‑deploy Vercel.
