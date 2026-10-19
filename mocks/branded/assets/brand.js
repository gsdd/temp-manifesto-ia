/* Manifesto Growth Architects: branded preview behaviours.
   Vanilla JS, no framework. Everything here is progressive enhancement over
   plain links and visible content, so nothing is hidden from search and the
   pages still work without JS. Preview exploration, not production code. */
(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. Sticky condensing header --------------------------------------- */
  var header = document.getElementById('siteHeader');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-condensed', window.scrollY > 24);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- 2. Mega-nav and dropdowns ------------------------------------------
     Hover intent on desktop, click to toggle (touch and keyboard), ArrowDown
     into the panel, Escape closes and returns focus, outside click closes. */
  (function () {
    var mega = document.getElementById('megaNav');
    var items = document.querySelectorAll('#primaryNav > li[data-menu]');
    var megaLi = document.querySelector('#primaryNav > li[data-menu="mega"]');
    if (!header || !items.length) return;
    var openTimer, closeTimer;
    var OPEN_DELAY = 120, CLOSE_DELAY = 280;
    var hoverable = window.matchMedia('(hover: hover)').matches;

    function setOpen(li, open) {
      var link = li.querySelector('.top-link');
      if (li.getAttribute('data-menu') === 'mega') {
        header.setAttribute('data-mega-open', open ? 'true' : 'false');
        document.body.setAttribute('data-mega-open', open ? 'true' : 'false');
      } else {
        li.setAttribute('data-open', open ? 'true' : 'false');
      }
      if (link) link.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    function isOpen(li) {
      var link = li.querySelector('.top-link');
      return link && link.getAttribute('aria-expanded') === 'true';
    }
    function closeAll() {
      Array.prototype.forEach.call(items, function (li) { setOpen(li, false); });
    }
    function openOnly(li) {
      Array.prototype.forEach.call(items, function (o) { if (o !== li) setOpen(o, false); });
      setOpen(li, true);
    }

    Array.prototype.forEach.call(items, function (li) {
      var link = li.querySelector('.top-link');
      if (hoverable) {
        li.addEventListener('mouseenter', function () {
          clearTimeout(closeTimer);
          openTimer = setTimeout(function () { openOnly(li); }, OPEN_DELAY);
        });
        li.addEventListener('mouseleave', function () {
          clearTimeout(openTimer);
          closeTimer = setTimeout(function () { setOpen(li, false); }, CLOSE_DELAY);
        });
      }
      if (link) {
        /* First tap or Enter opens; second follows the link. */
        link.addEventListener('click', function (e) {
          if (!isOpen(li)) {
            e.preventDefault();
            openOnly(li);
          }
        });
        link.addEventListener('keydown', function (e) {
          if (e.key === 'ArrowDown') {
            e.preventDefault();
            openOnly(li);
            var panel = li.getAttribute('data-menu') === 'mega' ? mega : li;
            var first = panel && panel.querySelector('a:not(.top-link)');
            if (first) first.focus();
          }
        });
      }
      /* Keep open while focus is inside; close when it leaves. */
      var panel = li.getAttribute('data-menu') === 'mega' ? mega : li;
      if (panel) {
        panel.addEventListener('focusout', function (e) {
          if (!panel.contains(e.relatedTarget) && !li.contains(e.relatedTarget)) setOpen(li, false);
        });
      }
    });

    if (mega && megaLi && hoverable) {
      mega.addEventListener('mouseenter', function () { clearTimeout(closeTimer); });
      mega.addEventListener('mouseleave', function () {
        closeTimer = setTimeout(function () { setOpen(megaLi, false); }, CLOSE_DELAY);
      });
    }

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        var openLink = document.querySelector('#primaryNav .top-link[aria-expanded="true"]');
        closeAll();
        if (openLink) openLink.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('#primaryNav') && !e.target.closest('#megaNav')) closeAll();
    });
  })();

  /* ---- 3. Mobile menu ------------------------------------------------------ */
  (function () {
    var toggle = document.getElementById('navToggle');
    var menu = document.getElementById('mobileMenu');
    if (!toggle || !menu) return;

    function setMenu(open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.setAttribute('data-mobile-open', open ? 'true' : 'false');
      if (open) {
        var first = menu.querySelector('a, button');
        if (first) first.focus();
      }
    }
    function isOpen() { return toggle.getAttribute('aria-expanded') === 'true'; }

    toggle.addEventListener('click', function () { setMenu(!isOpen()); });

    /* Accordions for the mega-nav groups and dropdowns */
    Array.prototype.forEach.call(menu.querySelectorAll('.m-top[aria-expanded]'), function (btn) {
      btn.addEventListener('click', function () {
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      });
    });

    /* Escape closes; simple focus trap while open */
    document.addEventListener('keydown', function (e) {
      if (!isOpen()) return;
      if (e.key === 'Escape') {
        setMenu(false);
        toggle.focus();
        return;
      }
      if (e.key === 'Tab') {
        var focusables = menu.querySelectorAll('a, button:not([aria-expanded="false"] ~ * *)');
        focusables = menu.querySelectorAll('a, button');
        var list = [toggle].concat(Array.prototype.slice.call(focusables).filter(function (el) {
          return el.offsetParent !== null;
        }));
        var first = list[0], last = list[list.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });

    /* Close when resizing up to desktop */
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080 && isOpen()) setMenu(false);
    });
  })();

  /* ---- 4. Cookie bar ------------------------------------------------------- */
  (function () {
    var bar = document.getElementById('cookieBar');
    if (!bar) return;
    try {
      if (sessionStorage.getItem('mga-cookies') === 'accepted') { bar.hidden = true; return; }
    } catch (e) { /* storage unavailable */ }
    var btn = bar.querySelector('[data-cookie-accept]');
    if (btn) btn.addEventListener('click', function () {
      bar.hidden = true;
      try { sessionStorage.setItem('mga-cookies', 'accepted'); } catch (e) { /* no-op */ }
    });
  })();

  /* ---- 5. Logo band: seamless loop ----------------------------------------
     The CSS animates the track; JS duplicates the logos once so -50% lands on
     an identical frame. Skipped under reduced motion (band stays static). */
  Array.prototype.forEach.call(document.querySelectorAll('.logo-band .band-track'), function (track) {
    if (REDUCED) return;
    var clone = track.cloneNode(true);
    Array.prototype.forEach.call(clone.children, function (c) {
      c.classList.add('dup');
      c.setAttribute('aria-hidden', 'true');
      track.appendChild(c.cloneNode(true));
    });
  });

  /* ---- 6. Thinking hub filters: type tabs plus tag pills -------------------
     Cards stay in the HTML; filters only hide and show. Deep links
     (?type=reports or #reports) open the matching state. */
  (function () {
    var grid = document.querySelector('[data-filter-grid]');
    if (!grid) return;
    var cards = Array.prototype.slice.call(grid.querySelectorAll('[data-type]'));
    var tabs = Array.prototype.slice.call(document.querySelectorAll('.type-tabs [data-type]'));
    var pills = Array.prototype.slice.call(document.querySelectorAll('.filters [data-tag]'));
    var empty = document.querySelector('[data-filter-empty]');
    var type = 'all', tag = '';
    var known = tabs.map(function (b) { return b.getAttribute('data-type'); });

    function apply() {
      var shown = 0;
      cards.forEach(function (card) {
        var okType = type === 'all' || card.getAttribute('data-type') === type;
        var tags = ' ' + (card.getAttribute('data-tags') || '') + ' ';
        var okTag = !tag || tags.indexOf(' ' + tag + ' ') !== -1;
        var show = okType && okTag;
        card.style.display = show ? '' : 'none';
        if (show) shown += 1;
      });
      tabs.forEach(function (b) {
        b.classList.toggle('on', b.getAttribute('data-type') === type);
        b.setAttribute('aria-pressed', b.getAttribute('data-type') === type ? 'true' : 'false');
      });
      pills.forEach(function (b) {
        b.classList.toggle('on', b.getAttribute('data-tag') === tag);
        b.setAttribute('aria-pressed', b.getAttribute('data-tag') === tag ? 'true' : 'false');
      });
      if (empty) empty.style.display = shown ? 'none' : '';
      var q = type === 'all' ? '' : '?type=' + type;
      try { history.replaceState(null, '', location.pathname + q); } catch (e) { /* file:// */ }
    }
    function setType(next) {
      if (known.indexOf(next) === -1) return;
      type = next;
      apply();
    }
    tabs.forEach(function (b) {
      b.addEventListener('click', function () { setType(b.getAttribute('data-type')); });
    });
    pills.forEach(function (b) {
      b.addEventListener('click', function () {
        var next = b.getAttribute('data-tag');
        tag = (tag === next) ? '' : next;
        apply();
      });
    });
    if (empty) {
      var clear = empty.querySelector('.btn');
      if (clear) clear.addEventListener('click', function (e) {
        e.preventDefault();
        type = 'all'; tag = '';
        apply();
      });
    }
    var fromQuery = (location.search.match(/[?&]type=([a-z-]+)/) || [])[1];
    var fromHash = location.hash ? location.hash.slice(1) : '';
    var LEGACY = { news: 'news-events', events: 'news-events', article: 'articles', report: 'reports' };
    var start = LEGACY[fromQuery || fromHash] || fromQuery || fromHash || 'all';
    if (known.indexOf(start) !== -1) type = start;
    apply();
  })();

  /* ---- 7. Work hub filters: industry and service groups -------------------- */
  (function () {
    var grid = document.querySelector('[data-work-grid]');
    if (!grid) return;
    var cards = Array.prototype.slice.call(grid.children);
    var empty = document.querySelector('[data-filter-empty]');
    var state = { industry: '', service: '' };

    function apply() {
      var shown = 0;
      cards.forEach(function (card) {
        var ok = ['industry', 'service'].every(function (dim) {
          if (!state[dim]) return true;
          var val = ' ' + (card.getAttribute('data-' + dim) || '') + ' ';
          return val.indexOf(' ' + state[dim] + ' ') !== -1;
        });
        card.style.display = ok ? '' : 'none';
        if (ok) shown += 1;
      });
      ['industry', 'service'].forEach(function (dim) {
        Array.prototype.forEach.call(document.querySelectorAll('[data-filter-' + dim + ']'), function (b) {
          var on = b.getAttribute('data-filter-' + dim) === state[dim] ||
                   (!state[dim] && b.getAttribute('data-filter-' + dim) === '');
          b.classList.toggle('on', on);
          b.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
      });
      if (empty) empty.style.display = shown ? 'none' : '';
    }
    ['industry', 'service'].forEach(function (dim) {
      Array.prototype.forEach.call(document.querySelectorAll('[data-filter-' + dim + ']'), function (b) {
        b.addEventListener('click', function () {
          state[dim] = b.getAttribute('data-filter-' + dim);
          apply();
        });
      });
    });
    if (empty) {
      var clear = empty.querySelector('.btn');
      if (clear) clear.addEventListener('click', function (e) {
        e.preventDefault();
        state.industry = ''; state.service = '';
        apply();
      });
    }
    apply();
  })();

  /* ---- 8. Careers role toggle ---------------------------------------------- */
  (function () {
    var wrap = document.querySelector('[data-role-list]');
    if (!wrap) return;
    var buttons = document.querySelectorAll('[data-role-filter]');
    function apply(mode) {
      Array.prototype.forEach.call(wrap.children, function (card) {
        var open = card.getAttribute('data-hiring') === 'true';
        card.style.display = (mode === 'all' || open) ? '' : 'none';
      });
      Array.prototype.forEach.call(buttons, function (b) {
        var on = b.getAttribute('data-role-filter') === mode;
        b.classList.toggle('on', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
    }
    Array.prototype.forEach.call(buttons, function (b) {
      b.addEventListener('click', function () { apply(b.getAttribute('data-role-filter')); });
    });
    apply('open');
  })();

  /* ---- 9. Profile pop-up: accessible dialog --------------------------------
     Opened from a Person card button. Native <dialog> gives focus trapping,
     Escape and backdrop close; focus returns to the opener. The full profile
     page URL stays a plain link for search and no-JS. */
  (function () {
    var dialog = document.getElementById('profileDialog');
    if (!dialog || typeof dialog.showModal !== 'function') return;
    var nameEl = dialog.querySelector('[data-d-name]');
    var roleEl = dialog.querySelector('[data-d-role]');
    var bioEl = dialog.querySelector('[data-d-bio]');
    var opener = null;

    Array.prototype.forEach.call(document.querySelectorAll('[data-profile-trigger]'), function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        opener = btn;
        if (nameEl) nameEl.textContent = btn.getAttribute('data-name') || 'Name';
        if (roleEl) roleEl.textContent = btn.getAttribute('data-role') || '';
        if (bioEl) bioEl.textContent = btn.getAttribute('data-bio') || '';
        dialog.showModal();
      });
    });
    dialog.addEventListener('close', function () {
      if (opener) opener.focus();
    });
    dialog.addEventListener('click', function (e) {
      if (e.target === dialog) dialog.close();
    });
    var closeBtn = dialog.querySelector('.dialog-close');
    if (closeBtn) closeBtn.addEventListener('click', function () { dialog.close(); });
  })();

  /* ---- 10. Carousel: controls plus gentle auto-advance ---------------------
     Scroll-snap does the layout; buttons page by one card; auto-advance every
     five seconds, pausing on hover or focus, off under reduced motion. */
  Array.prototype.forEach.call(document.querySelectorAll('[data-carousel]'), function (root) {
    var track = root.querySelector('.carousel-track');
    var prev = root.querySelector('[data-prev]');
    var next = root.querySelector('[data-next]');
    if (!track || !prev || !next) return;

    function step() {
      var card = track.firstElementChild;
      if (!card) return 320;
      var gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap) || 24;
      return card.getBoundingClientRect().width + gap;
    }
    function update() {
      var max = track.scrollWidth - track.clientWidth - 2;
      prev.disabled = track.scrollLeft <= 2;
      next.disabled = track.scrollLeft >= max;
    }
    prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: REDUCED ? 'auto' : 'smooth' }); });
    next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: REDUCED ? 'auto' : 'smooth' }); });
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();

    if (!REDUCED) {
      var paused = false;
      root.addEventListener('mouseenter', function () { paused = true; });
      root.addEventListener('mouseleave', function () { paused = false; });
      root.addEventListener('focusin', function () { paused = true; });
      root.addEventListener('focusout', function () { paused = false; });
      setInterval(function () {
        if (paused || document.hidden) return;
        var max = track.scrollWidth - track.clientWidth - 2;
        if (track.scrollLeft >= max) track.scrollTo({ left: 0, behavior: 'smooth' });
        else track.scrollBy({ left: step(), behavior: 'smooth' });
      }, 5000);
    }
  });

  /* ---- 11. Report gate ------------------------------------------------------
     Submitting the form reveals the on-page body. No backend in this preview;
     whether the report is gated at all is an open decision (FINDINGS). */
  (function () {
    var form = document.getElementById('gateForm');
    var body = document.getElementById('gatedBody');
    if (!form || !body) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.querySelector('input[type="email"]');
      var field = email && email.closest('.field');
      var msg = form.querySelector('.field-msg');
      if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.value)) {
        if (field) field.classList.add('is-error');
        if (msg) msg.hidden = false;
        email.focus();
        return;
      }
      body.hidden = false;
      form.closest('.gate').hidden = true;
      body.setAttribute('tabindex', '-1');
      body.focus();
    });
  })();
})();
