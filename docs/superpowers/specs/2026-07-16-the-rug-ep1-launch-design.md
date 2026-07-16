# THE RUG — EP.1 Launch Design
Data: 2026-07-16 · IP: The Rug (brand Jayl) · Stato: approvato in brainstorming

## Obiettivo
Lanciare l'IP The Rug con 4 clip verticali su Instagram/TikTok, seguiti dall'episodio 1 completo (~2 min). L'episodio mantiene la struttura esistente (25 shot, doc `THE_RUG_EP1_PROMPTS.docx`); si riscrivono i prompt con la skill higgsfield-seedance-prompt e si fa un punch-up leggero dei dialoghi.

## Decisioni chiave
1. **Prodotto**: i clip social sono il prodotto di lancio; l'episodio completo è il montaggio che esce dopo il clip 4.
2. **Formato**: tutto si genera UNA volta in **16:9 @ 720p** (risparmio crediti). Nessuna rigenerazione nativa 9:16 (eventuale test su un solo shot solo se i dati lo chiedono).
3. **Export social**: canvas 9:16 in CapCut, 16:9 centrato, bande brandizzate — logo THE RUG neon in alto, sottotitoli grandi in basso. Il letterbox è brand identity: "questo è un film".
4. **Modelli**: immagini = **Nano Banana Pro (nano_banana_2)**, prompt in ITALIANO. Video = **Seedance 2.0**, prompt in INGLESE, **Quality mode** per close-up/dialoghi/espressioni, Fast solo per wide semplici. Soul Cinema / GPT Image 2 solo sporadici. Montaggio CapCut, musica Suno.
5. **Reference**: dichiarate prima di ogni prompt, max 3-4 per shot Seedance, mai citate con numeri dentro il prompt.

## I 4 clip di lancio (ordine di pubblicazione)
| # | Clip | Shot | Durata | Hook (sec 0) | Chiusura |
|---|------|------|--------|--------------|----------|
| 1 | THE SLAP | 7–13 | ~15s | mostro si gira, baffo rivelato | Kahlúa vola in mano, beve |
| 2 | COMMUTING | 5A–5B | ~15s | uomo su tappeto sopra LA golden hour | drink in faccia + overlay "I knew it wouldn't work" |
| 3 | THE RETURN | 14–16 | ~12s | ECU occhi che salgono 15° mentre beve | posa il collo di bottiglia con cura |
| 4 | THE FIVE | 17–25 | ~15s | portale si apre | freeze frame Boss + titolo neon |

L'episodio completo esce dopo THE FIVE.

## Dialoghi — punch-up approvato
- "Uh... Fine." — invariata.
- "Excuse me" — invariata, ma detta MENTRE si sistema i capelli (non dopo).
- "Nice moustache." — sincera, invariata. Nuovo beat: il mostro si lusinga per mezzo secondo e abbassa la guardia → lo schiaffo parte in quel momento.
- Battuta finale: **"Wtf… why do you all have moustaches?"** (sostituisce la versione precedente sgrammaticata).
- Mostri Ep.1 non verbali (grugniti). Prima voce aliena della serie = il Boss, dall'Ep.2.

## Workflow riscrittura prompt
1. Skill **higgsfield-seedance-prompt** per ogni shot (Seedance EN, NBP IT).
2. Integrare le soluzioni ai problemi noti: no head-turn ("head never turns, not even 1 degree"), logo solo su tessuto vestaglia, meccanica fisica dei liquidi esplicita, "Fixed 50mm lens" contro zoom indesiderati, "buildings scroll continuously rightward" per il volo.
3. Ordine di lavorazione: **THE SLAP** (manifesto dell'IP, frame mostro già approvati) → **COMMUTING** (shot 5A/5B, problemi Seedance aperti) → THE RETURN → THE FIVE → shot rimanenti dell'episodio (Shot 1, atterraggio 6A-6C).
4. The Rug non deve mai somigliare ad attori famosi; negative sempre con "no celebrity likeness".

## Asset esistenti
- Cartella `~/Desktop/the rug`: character sheet protagonista (costume, vestaglia), 6 antagonisti, 2 loghi, frame approvati (Shot 1, 5A, 5B, mostro MCU, lampione, ECU baffo), 4 video di test.
- Doc di riferimento: `~/Downloads/THE_RUG_KNOWLEDGE_TRANSFER_1.docx` (bible), `~/Desktop/THE_RUG_EP1_PROMPTS.docx` (prompt v1 da riscrivere).

## Fuori scope (per dopo)
- Sito web The Rug e asset video del sito.
- Coordinamento con le altre IP Jayl (Zack, Dinos & Mages).
- Gag del Boss sui baffi ("we studied your culture") → episodio futuro.
