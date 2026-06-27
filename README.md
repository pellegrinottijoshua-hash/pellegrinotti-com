# JAYL Studio — landing (studio.jayl.store)

Landing statica single-page, bilingue IT/EN, identità JAYL. Lead-gen per commissioni video.

## Struttura
- `index.html` — tutta la pagina (HTML + CSS + JS inline, zero build).
- `assets/` — qui vanno i video e i poster.

## Cosa caricare in `assets/`
| File | Cosa |
|---|---|
| `lei-chi-e.mp4` | il film "lei chi è" (usato come hero loop + nel player). Metti una versione corta/ottimizzata per l'hero se pesa troppo. |
| `hero-poster.jpg` | fermo-immagine di copertina dell'hero (mentre carica il video) |
| `leichi-poster.jpg` | copertina del player "lei chi è" |
| `demo-ads.mp4` · `demo-music.mp4` · `demo-content.mp4` | i 3 video demo dei servizi (li farai poi) |
| `work-1.mp4 … work-6.mp4` | clip della gallery (lei chi è, The Rug, nuovi) |

> I posti dove inserirli sono già segnati con commenti `<!-- ... -->` dentro `index.html`. Per le card servizi e le tile gallery: sostituisci lo `<span>Demo coming soon / Add clip</span>` con `<video muted loop playsinline><source src="assets/NOME.mp4" type="video/mp4"></video>`.

## Da completare quando li hai
- **WhatsApp:** in `index.html`, sezione Contact, sostituisci lo `<span class="soon">WhatsApp…</span>` con `<a href="https://wa.me/39XXXXXXXXXX"><span>WhatsApp</span><span class="gold">Message me</span></a>`.
- **Instagram:** idem con `<a href="https://instagram.com/IL_TUO_HANDLE">…</a>`.
- Email già attiva: **jayl.video@gmail.com**.

## Deploy su Vercel + sottodominio
1. Da questa cartella: `vercel` (primo deploy) → poi `vercel --prod`. (È un sito statico: Vercel serve `index.html`, nessuna config necessaria.)
2. Nel progetto Vercel → **Settings → Domains** → aggiungi `studio.jayl.store`.
3. Sul DNS del dominio `jayl.store` aggiungi un record **CNAME**: `studio` → `cname.vercel-dns.com` (Vercel ti mostra il valore esatto). Propagazione ~minuti.
4. HTTPS automatico.

> Nota: è un progetto SEPARATO dallo shop (così non appesantisce jayl.store). Stessa identità visiva, due deploy distinti.

## Prezzi attuali in pagina
AI Ads & Product Films **From €350** · Music Videos & Visualizers **From €500** · Brand Content Engine **From €600/mo**. (Ritoccabili in `index.html`, sezioni Services e Pricing.)
