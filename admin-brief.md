# pellegrinotti.com — Admin panel: brief per nuova chat

Incolla questo intero file come primo messaggio in una nuova chat Claude Code (**Opus 4.8** — raccomandato: stessa capacità di Fable 5 per questo lavoro di implementazione, a metà del prezzo. Fable 5 costa $10/$50 per 1M token input/output contro $5/$25 di Opus 4.8; usalo solo se vuoi esplicitamente il massimo "intuito" su una decisione architetturale ambigua). cwd consigliata: `~/jayl-studio`.

## Cosa costruiamo

Un pannello admin per **pellegrinotti.com** (portfolio personale di Joshua Pellegrinotti, sub-brand JAYL), sul modello di quello già esistente per **jayl.store** (repo sorella `~/jayl-store`, vedi pattern da riusare sotto) ma più esteso: non solo gestione prodotti, anche una sezione "secondo cervello" per idee/progetti personali.

## Contesto tecnico attuale

- `~/jayl-studio` è un sito **statico puro**: un solo `index.html` (~450 righe, CSS+JS inline), niente build step, niente `package.json`, niente backend. Deploy: push su `main` → Vercel production immediato (no staging).
- Repo GitHub: `pellegrinottijoshua-hash/pellegrinotti-com`, **pubblico**.
- Vercel project: `jayl-studio` (id `prj_ZyhwfiMifVwTpqBWW3rLuCAM0tju`), team `pellegrinottijoshua-hashs-projects`.
- Oggi zero API/serverless functions — vanno introdotte da zero (pattern `api/*.js` come in jayl-store, vedi sotto).
- **R2 già configurato** (Cloudflare) per gli asset pesanti (video/immagini 2-20MB). Env var già su Vercel (Preview+Production): `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET_NAME`, `R2_PUBLIC_URL`. Bucket dedicato a pellegrinotti.com (non condiviso con jayl.store — token scoped al singolo bucket per principio del privilegio minimo, dato che questo repo è pubblico).
- Hero attuale (`index.html`): sistema di "flip" 3D fisso su N immagini JPG numerate (`assets/hero/01.jpg...25.jpg`, + pool mobile separato), ordine ormai **sequenziale** (non più random, appena sistemato), trigger su scroll-down (throttle 450ms) e su tap. **Questo sistema va generalizzato** — vedi sezione "Hero mista" sotto, è il pezzo più impegnativo.

## Pattern da riusare da jayl-store (stessa organizzazione Vercel/GitHub)

- **Auth**: `~/jayl-store/api/admin.js:16` (`ADMIN_PASSWORD` da env, mai nel client), `:387-391` (verifica password, azione `verify-password`). Client-side: POST a `/api/admin` con `{action:'verify-password', password}`, su 200 salva in `sessionStorage('jaylAdminPw')` — vedi `src/components/generate-assets/constants.js:3` (`getAdminPassword()`). Riusa lo stesso schema: 1 password condivisa via env Vercel (`ADMIN_PASSWORD` — **nuova env var separata per questo progetto**, non riusare quella di jayl.store).
- **AI content-assist**: `~/jayl-store/api/admin.js:1197` e `:1388` usano `ANTHROPIC_API_KEY` da env per generare SEO/testi. `~/jayl-store/api/ai.js:28` ha un registry multi-provider (`openai`, keyEnv `OPENAI_API_KEY`, modello `gpt-4o-mini`) con endpoint dedicati per generazione testo/immagini. Stesso schema qui.
- **Vercel serverless limit**: jayl.store consolida ~40 azioni admin in **un solo endpoint** `api/admin.js` con uno switch su `action`, proprio per stare sotto il limite di funzioni Vercel (Hobby/Pro hanno un tetto). Segui lo stesso schema qui: `api/admin.js` con switch-case, non un file per azione.

## Decisioni prese (dalle risposte di Joshua)

1. **Auth**: password unica condivisa (no username/ruoli), stesso schema di jayl-store.
2. **Jayl Art**: contenuti scritti a mano nel form (titolo, movimento artistico, ispirazione/credits, descrizione), ma con **tasto AI-assist** che aiuta a scrivere/migliorare il testo (usa Claude o GPT, stesso pattern del punto AI-assist sopra).
3-4. **Hero mista**: Joshua vuole una **sequenza ordinata di media misti** — video (personaggi che si muovono, parlano, si trasformano), immagini, GIF, in qualunque combinazione e ordine (es: video → immagine → video → gif). Questo è il cambio più grosso rispetto al sistema attuale: va sostituito il pool fisso di JPG numerati con un **array ordinato di media item** (`{type: 'video'|'image'|'gif', src, durata?}`), gestito dall'admin (drag-to-reorder, upload, elimina). Il flip 3D attuale funziona per immagini statiche — per i video probabilmente serve un trigger diverso (autoplay + skip al successivo al termine, o comunque va ridisegnata l'interazione scroll/tap per contenuti che hanno una loro durata).
5. **Flusso di pubblicazione**: upload diretto del file nell'admin (va su R2, non serve resize essendo su R2), poi tasto "SEO" separato che genera titolo/descrizione/etc via AI, poi tasto "pubblica" che rende live. Tre step distinti, non automatico.
6. **Compressione**: manuale, tasto "comprimi" opzionale dopo l'upload. **Rischio tecnico da validare in questa chat**: comprimere video via ffmpeg dentro una funzione serverless Vercel ha vincoli reali (timeout, memoria, dimensione del binario, e il tetto di funzioni totali del piano). Opzioni da valutare: (a) ffmpeg-static dentro una function Vercel con Fluid Compute se il video è abbastanza piccolo/veloce da restare sotto il timeout, (b) servizio esterno dedicato (Cloudflare Stream, Mux, o simili) che fa la transcodifica e poi si ripubblica l'URL risultante, (c) skip la compressione server-side e affidarsi solo a un encoding ragionevole fatto a monte da Joshua. Decidere con Joshua prima di implementare, non dare per scontata l'opzione (a).
7. **"Secondo cervello" — scope ampio, potenzialmente pubblico in futuro**: non una semplice lista idee, ma una struttura a **sezioni** (es: Jayl Store, Jayl Video, Pellegrinotti Brand, Investimenti, Crypto, Progetti...), ognuna con **sottosezioni riempibili** (idee, immagini, testo libero), e **tasti AI che aiutano a sviluppare l'idea** (assist scrittura/brainstorm, stesso pattern AI-assist del punto 2). È lo scope più grande e ambiguo dei sei — **vale la pena farlo passare per una sessione di brainstorming/design dedicata** (skill `superpowers:brainstorming` se disponibile) prima di implementare, non buttarsi diretti sul codice: la struttura dati (sezioni annidate + tipi di contenuto misti + eventuale pubblicazione futura) merita uno schema pensato bene dall'inizio per non doverlo migrare dopo.
8. **Testi editabili del sito**: lasciato aperto — "ciò che ha più senso". Punto di partenza ragionevole: kicker/lead delle 4 sezioni (Video/Code/Art/[Who am I quando torna]), email di contatto, link social (oggi placeholder `#` — vanno riempiti comunque, indipendentemente dall'admin). Copy lungo delle sezioni: da valutare se vale la pena renderlo editabile o lasciarlo hardcoded in `index.html` (più aggiornamenti = più superficie admin da mantenere).
9. **Device**: admin deve funzionare **sia desktop che mobile** (Joshua vuole poter caricare una foto/idea al volo da telefono) — responsive fin dall'inizio, non un ripensamento successivo.
10. **Cestino/undo**: serve un vero "cestino" dentro l'admin (soft-delete, non solo affidarsi alla cronologia git) per recuperare upload/testi cancellati per errore.

## Cosa manca ancora / cose da NON dare per scontate

- Il repo pellegrinotti-com **non ha mai avuto backend** — introdurre `api/*.js` è un cambio di natura del progetto (da "sito statico" a "statico + funzioni serverless"), verificare che `vercel.json` (se non esiste, va creato) instradi correttamente le rotte admin senza rompere il resto.
- I social link (Instagram/LinkedIn) sono ancora placeholder `#` nel nav/footer — non è compito dell'admin ma va segnalato a Joshua come task separato.
- "Who am I" è nascosto dal nav (deciso in sessione precedente, in attesa di contenuti reali) — non toccarlo salvo richiesta esplicita.
- `assets/iconaj2.svg` pesa 3.8MB (dovrebbe essere KB) — bug preesistente indipendente, non bloccante per l'admin ma da tenere a mente se emerge durante il lavoro sugli asset.

## Come procedere consigliato

1. Prima sessione: **brainstorming/design** (usa la skill `superpowers:brainstorming` se disponibile) per fissare lo schema dati di Jayl Art, Hero mista, e soprattutto "secondo cervello" — sono le tre cose con più ambiguità residua.
2. Poi piano di implementazione a fasi: (a) auth + skeleton admin, (b) upload R2 + gestione hero mista, (c) Jayl Art CRUD + AI-assist, (d) secondo cervello, (e) testi editabili base.
3. Verifica sempre in preview prima di considerare una fase "fatta" — questo progetto non ha staging, ogni push in main è live.
