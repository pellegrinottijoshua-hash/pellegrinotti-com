# Master prompt — versioni mobile 9:16 (Nano Banana / image-to-image)

Usa questo prompt **una immagine alla volta**: dai in input la versione landscape (`01.jpg … 25.jpg`)
e ottieni la verticale. Salva gli output come `assets/hero/mobile/01.jpg … 25.jpg`
(stesso numero della landscape → così il sito abbina in automatico).

---

## PROMPT (copia-incolla)

> Reframe this image into a vertical **9:16 portrait** for a mobile website hero.
> Keep the **exact same subject** (same face, same hair, same likeness) and the **exact same art style,
> color palette, lighting and mood** — do NOT restyle, do NOT change the character.
> Recompose for vertical: subject **centered**, head in the **upper third** with comfortable headroom
> (never crop the top of the head), framed roughly from **top of head to mid-torso**.
> **Naturally extend / outpaint** the existing background above and below to fill the 9:16 frame,
> keeping it a **dark, near-black, uncluttered backdrop** that fades to black at the edges so it blends
> into a black website. Preserve fine detail and texture.
> **No text, no watermark, no borders, no new objects.** Output a clean **1080×1920** portrait.

---

## Note pratiche
- Sfondo **scuro / near-black** è importante: la foto deve fondersi col nero del sito.
- **Non tagliare la testa**: lascia aria sopra.
- Se un soggetto è molto laterale nell'originale, aggiungi: *"move the subject toward the center".*
- Se l'outpaint inventa dettagli strani ai bordi, aggiungi: *"keep the extended areas simple and dark".*
- Formato/nome file: `NN.jpg` (2 cifre) dentro `assets/hero/mobile/`.

## Cosa ho già predisposto nel codice
- Su schermi ≤ 640px il sito carica `assets/hero/mobile/NN.jpg`.
- Se il file mobile non c'è ancora, **fallback automatico** alla landscape `assets/hero/NN.jpg`
  (quindi il sito funziona già ora, e migliora appena carichi le verticali).
