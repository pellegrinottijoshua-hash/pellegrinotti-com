# pellegrinotti.com — Services-first IA + shared video player

**Date:** 2026-08-07
**Repos touched:** `jayl-studio` (home + deployed sub-sites), `zack-site` (source of `/zack/`)
**Status:** shipped 2026-08-07 — `jayl-studio` cccc425…3eb7f08, `zack-site` e47f494

### Deltas from the design, decided during implementation

- **GSAP removed.** The detail overlay was its only consumer, so deleting the overlay left a
  ~70 kB render-blocking CDN script doing nothing on every page load. Not foreseen in the design.
- **Zack cards became keyboard-operable** (`role="button"`, `tabindex=0`, Enter/Space, preview on
  focus). The click is now the only route to an episode, so mouse-only would have been a regression.
- **The rsync excludes `*.md`.** Without it the sub-site's `README.md` and `ASSET_PROMPTS.md`
  landed in the deployed folder.
- **Backdrop `.96` + 14 px blur** instead of `.94`: at `.94` the page text showed through the
  letterbox bars.
- **The play marker is a circled triangle sized off the row.** As an em of `.ipname` it computed
  to ~8 px and read as a stray glyph.
- A CSS comment that contained literal markup was rewritten — it made greps for the removed
  Dinos element return false positives twice during verification.

---

## Why

The home reads as a showreel. A DTC brand with a €2–6k budget lands on it and cannot tell,
in one screen, that Joshua sells video production — the offer is buried three clicks deep
inside a "Jayl Video" overlay that mixes paid work with original IP experiments.

Two consequences:

1. **The services are invisible.** The only commercial gancio in the whole page is one CTA
   at the bottom of the "AI Ads" group, inside an overlay nobody opens.
2. **The IPs and the services compete.** They speak to different audiences (fans vs. buyers)
   but share one flat list, so neither gets a clear frame.

This change splits the two explicitly and makes the offer the first thing on the list.

Positioning source of truth: `../../../pellegrinotti-services.md`.

## Scope

In:

- Rename and re-behave row 01: `Jayl Video` → `Jayl Services`, now an inline dropdown.
- Rename row 02: `Jayl IPs` → `Jayl Original IPs`, and drop its subtitle.
- Hide `Dinos & Mages` from the Original IPs dropdown.
- Delete the detail-overlay machinery the change orphans (including the *One Shots* group).
- Add a shared fullscreen video player, used by the Services dropdown and by `/zack/`.

Out:

- Row 03 `Jayl Store` — untouched.
- `/therug/` clips keep the current muted hover-loop. `~/therug-site` has unsynced local work,
  so it is not touched in this pass; the player is built so adding it later is a wiring job.
- Social links. Owner is handling those separately.
- `duel.mp4` on R2 and its line in `scripts/upload-to-r2.sh` become orphaned once *One Shots*
  goes. Flagged, not changed.

## Current state (verified 2026-08-07)

`index.html` (495 lines, inline CSS + JS, no build step):

| Row | Markup | Behaviour |
|---|---|---|
| 01 | `.row[data-target="video"]` | `openDetail('video')` → full-page overlay built by `videoBody()` |
| 02 | `.brandwrap` → static `.row` + always-open `.branddrop` | 3 `<a class="ip">` → `/therug/`, `/zack/`, `/dinos/` |
| 03 | `.row[data-target="store"]` | `window.open('https://jayl.store')` |

`videoBody()` renders 5 groups: *Lei chi è*, *The Rug* (3 chapters), *One Shots*,
*Zack the Duck* (3 clips), *AI Ads* (fermentati). Each `.vmedia` plays muted on hover and
unmutes in place on click — it never goes fullscreen.

CSS facts that constrain the design:

- `.row .idx { display:none }` is global — the `01/02/03` spans are already invisible dead markup.
- `.row .cat { display:none }` lives inside `@media(max-width:640px)` — subtitles show on desktop only.
- `.row` is `display:flex; justify-content:space-between`, so removing a `.cat` leaves the label
  alone on the left with no layout break.

Media inventory (ffprobe):

| Asset | Resolution | Duration | Size | Audio |
|---|---|---|---|---|
| `fermentati-ad.mp4` | 720×1280 (9:16) | 10.1s | 9.4 MB | aac 2ch |
| `lei-chi-e-web.mp4` | 1280×720 (16:9) | 156.0s | 22.3 MB | aac 2ch |
| `zack e1/e2/e3.mp4` | 720×1280 (9:16) | 8–14s | 2.8–3.4 MB | aac 2ch |

All videos are served from `MEDIA_BASE = https://media.pellegrinotti.com`, except the `/zack/`
episode clips, which ship locally inside the sub-site (`zack/assets/clips/`).

## Design

### 1. Nav

`01/02/03` below are positional references for this document only — the `.idx` spans are
`display:none` and no number is ever rendered.

```
01  Jayl Services        Product films · social ads · music videos
      AI videos for:
      → your brand       Product films and social ads that look like cinema, not catalogue.
                         [play] → fermentati ad, fullscreen + sound     [Get a video for your brand ↗]
      → your song        Music videos built frame by frame around your track.
                         [play] → Lei chi è, fullscreen + sound         [Get a video for your song ↗]

02  Jayl Original IPs    (no subtitle)
      → The Rug          A lazy superhero saga
      → Zack the Duck    Art finds a way

03  Jayl Store           Wearable-art brand
```

Row 01 stops being a link into an overlay and becomes a `.brandwrap` + `.branddrop` pair,
reusing the Original IPs markup and CSS verbatim. One interaction model on the page, no new
CSS surface, and the dropdown is always-open like the IP one — nothing to discover.

**The `Jayl` hover-reveal is preserved on every row.** `.rowtext .jayl` starts at `max-width:0`
and expands on `.row:hover`, so the label reads `Services` at rest and `Jayl Services` on hover.
The rule is keyed on `.row`, not on `a.row`, so it keeps working once row 01 becomes a static
label inside `.brandwrap` — same as row 02 does today.

Consequence for the JS: `document.querySelectorAll('.row[data-target]')` now matches only the
store row, and the mobile two-tap `.rev` dance (first tap reveals `Jayl`, second navigates)
applies only there. Rows 01 and 02 lose their `data-target` and are no longer click targets
themselves — their dropdown children are.

CTA targets:

| Line | mailto |
|---|---|
| your brand | `pellegrinottijoshua@gmail.com?subject=AI%20video%20for%20my%20brand` |
| your song | `pellegrinottijoshua@gmail.com?subject=AI%20video%20for%20my%20song` |

**`your brand` outranks `your song`.** It comes first and carries the heavier visual weight.
`pellegrinotti-services.md` classes music videos as portfolio-only, not income; giving the two
equal billing would tell a paying brand that this is a hobby practice.

The Services dropdown is built from a **data array**, so adding the social-ad-pack line later
is one object literal, not a refactor. It is not added now: there is no second brand asset to
show, and an offer without a sample is an empty promise.

### 2. Deletions

With row 01 no longer opening an overlay and row 03 opening an external tab, nothing calls the
detail router. Remove:

- `#curtain`, `#detail` markup and their CSS
- `DATA`, `fill()`, `openDetail()`, `closeDetail()`, the `#back` listener
- `videoBody()` and all 5 groups, plus `.vlist`/`.vgroup`/`.vmedia`/`.pbtn` CSS
- `go()` collapses to the store case only

This also removes the *One Shots* group, and with it the two dead `href="#"` social links.

Leaving the overlay in place would mean shipping ~80 lines of JS plus its CSS that no code path
can reach — and a second, inconsistent way of showing video.

### 3. Shared player — `assets/js/lightbox.js`

One component, one behaviour, everywhere.

API:

```js
openPlayer({ src, title })   // title is used for the aria-label only
```

Behaviour:

- Full-viewport overlay above everything; a single reused `<video controls autoplay playsinline>`.
- **Not muted.** Autoplay with sound is allowed because the call always originates from a user click.
- `object-fit: contain`, centred, capped to the viewport — 9:16 and 16:9 both letterbox cleanly
  without per-asset special-casing.
- `preload="none"`; the `src` is set on open. *Lei chi è* is 22 MB, so it must never load for
  someone who merely visits the home.
- Close on **ESC**, backdrop click, or the × button. On close: pause, clear `src` (releases the
  buffer), restore body scroll, return focus to the element that opened it.
- Focus moves to the × on open. Body scroll locked while open.
- Native `controls` are kept deliberately: they include the browser's own fullscreen button, so
  true fullscreen stays available without relying on the Fullscreen API, which is unreliable on
  iOS Safari for non-video elements.

Why an overlay rather than `requestFullscreen()` on the video: consistent chrome across
browsers, works on iOS, and keeps the CTA reachable when the viewer closes the video.

### 4. `/zack/`

`~/zack-site/index.html`, then rsync into `jayl-studio/zack/`.

The muted hover-loop preview on the `.ep-card`s **stays** — it is the best thing about that page.
Only the click changes: instead of `card.classList.add('playing')` and an in-place unmute, it
calls `openPlayer()` with the episode clip.

Sources come from the existing `data-video` attributes; the `title` passed to `openPlayer` is
the poster's `alt` (`Episode 1 — The Masterpiece`, `Episode 2 — The Quill`,
`Episode 3 — En Garde`), which becomes the overlay's `aria-label`.

### 5. The two-repo constraint

`/zack/` is not editable in `jayl-studio` — the source is `~/zack-site` and the deployed folder is
an rsync target. There is no build step and no way to share a file across the two repos, so
`lightbox.js` exists as **two byte-identical copies**:

- `jayl-studio/assets/js/lightbox.js`
- `zack-site/assets/js/lightbox.js`

Both CLAUDE.md files get a line saying the two must be kept in sync. The alternative — having
`zack/index.html` reference the parent site's `/assets/js/lightbox.js` — would break standalone
preview of `~/zack-site`, which is where that page is actually developed. Introducing a bundler
to a 495-line static site to deduplicate 50 lines is not worth it.

## Verification

Local (`preview_start` on both `jayl-studio` and `~/zack-site`), then production after deploy:

1. Services dropdown opens; `your brand` and `your song` each open the player with audible sound.
2. Player: ESC / backdrop / × all close it; `src` is cleared after close; body scroll returns.
3. Both a 9:16 and a 16:9 asset display fully, uncropped, on desktop and at 375px width.
4. Network: `lei-chi-e-web.mp4` is **not** requested on home load, and **is** requested on open.
5. `/zack/`: hover still previews muted; click opens the player with sound on all three episodes.
6. `Dinos & Mages` absent from the dropdown; `https://pellegrinotti.com/dinos/` still returns 200.
7. Row 02 shows no subtitle; rows 01 and 03 keep theirs; no layout shift at 640px.
8. No console errors on the home or on `/zack/`.
9. Nothing references the removed overlay: grep for `openDetail`, `videoBody`, `curtain`, `One Shots`.

## Follow-ups (not in this pass)

- Third Services line (social ad pack) when a second brand asset exists.
- `/therug/` clips onto the shared player.
- `duel.mp4`: drop from `scripts/upload-to-r2.sh` and R2.
- Dead `.idx` spans in the row markup.
- Hero rotation still caps at `var N=11` while 25 images per pool sit on disk.
