/* Shared fullscreen video player — pellegrinotti.com
 *
 * ⚠️ Two byte-identical copies exist, one per repo, because /zack/ is developed
 * standalone in ~/zack-site and rsync'd into jayl-studio. Change one, change the other:
 *   jayl-studio/assets/js/lightbox.js
 *   zack-site/assets/js/lightbox.js
 * Markup AND styles live in here so there is only one file to keep in sync.
 *
 * Usage:  openPlayer({ src: '…/clip.mp4', title: 'Episode 1 — The Masterpiece' })
 *
 * Sound is ON: every call originates from a user click, so autoplay with audio is
 * allowed. Native controls are kept — they carry the browser's own fullscreen
 * button, which works on iOS where the Fullscreen API does not.
 */
(function (w, d) {
  'use strict';

  var CSS =
    /* .94 alone let the page text bleed through behind the letterbox bars */
    '.lb{position:fixed;inset:0;z-index:9999;display:none;align-items:center;justify-content:center;' +
      'background:rgba(0,0,0,.96);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);' +
      'padding:max(16px,3vmin);opacity:0;transition:opacity .25s ease}' +
    '.lb.open{display:flex;opacity:1}' +
    /* contain, so 9:16 and 16:9 both letterbox cleanly without per-asset cases */
    '.lb-v{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;' +
      'background:#000;outline:none;border-radius:2px}' +
    '.lb-x{position:absolute;top:max(12px,2.4vmin);right:max(12px,2.4vmin);z-index:1;' +
      'width:44px;height:44px;border:0;border-radius:50%;cursor:pointer;' +
      'background:rgba(255,255,255,.1);color:#fff;font-size:26px;line-height:1;' +
      'display:grid;place-items:center;transition:background .2s ease}' +
    '.lb-x:hover{background:rgba(255,255,255,.22)}' +
    '.lb-x:focus-visible{outline:2px solid #fff;outline-offset:2px}' +
    '@media (prefers-reduced-motion:reduce){.lb{transition:none}}';

  var box = null, vid = null, closeBtn = null, lastFocus = null;

  function build() {
    var style = d.createElement('style');
    style.textContent = CSS;
    d.head.appendChild(style);

    box = d.createElement('div');
    box.className = 'lb';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.innerHTML =
      '<button class="lb-x" type="button" aria-label="Close video">&times;</button>' +
      '<video class="lb-v" controls playsinline preload="none"></video>';
    d.body.appendChild(box);

    vid = box.querySelector('.lb-v');
    closeBtn = box.querySelector('.lb-x');

    closeBtn.addEventListener('click', close);
    // Backdrop only — clicks on the video or its controls must not close it.
    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && box.classList.contains('open')) close();
    });
  }

  function open(opts) {
    if (!opts || !opts.src) return;
    if (!box) build();

    lastFocus = d.activeElement;
    box.setAttribute('aria-label', opts.title || 'Video');
    vid.src = opts.src;
    vid.muted = false;
    box.classList.add('open');
    d.body.style.overflow = 'hidden';
    closeBtn.focus();
    vid.play().catch(function () {
      // Blocked despite the user gesture (rare) — the controls are there for a manual start.
    });
  }

  function close() {
    if (!box) return;
    box.classList.remove('open');
    vid.pause();
    // Drop the buffer: lei-chi-e-web.mp4 alone is 22 MB.
    vid.removeAttribute('src');
    vid.load();
    d.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
    lastFocus = null;
  }

  w.openPlayer = open;
  w.closePlayer = close;
})(window, document);
