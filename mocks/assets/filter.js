/* Our thinking listing filters. Wireframe-only, vanilla JS, no framework.
   Tabs filter by type, pills by tag; both only hide and show cards that are
   always present in the HTML, so crawlers see everything. Deep links
   (?type=reports or #reports) open the matching state on load. */
(function () {
  'use strict';

  var grid = document.querySelector('[data-filter-grid]');
  if (!grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll('[data-type]'));
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.type-tabs [data-type]'));
  var pills = Array.prototype.slice.call(document.querySelectorAll('.filters [data-tag]'));
  var empty = document.querySelector('[data-filter-empty]');
  var type = 'all';
  var tag = '';

  var known = tabs.map(function (b) { return b.getAttribute('data-type'); });
  var LEGACY = { news: 'news-events', events: 'news-events', article: 'articles', report: 'reports' };

  function slug(text) {
    return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
  }

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
    tabs.forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-type') === type); });
    pills.forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-tag') === tag); });
    if (empty) empty.style.display = shown ? 'none' : '';
    var q = type === 'all' ? '' : '?type=' + type;
    try { history.replaceState(null, '', location.pathname + q); } catch (e) { /* file:// */ }
  }

  function setType(next) {
    next = LEGACY[next] || next;
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

  /* Tags on the cards drive the same tag filter, where a matching pill exists.
     The card itself stays a whole-card link; a tag click does not navigate. */
  grid.addEventListener('click', function (e) {
    var t = e.target;
    if (!t.classList) return;
    if (!(t.classList.contains('tl-pill') || (t.tagName === 'EM' && t.closest('.tl-tags')))) return;
    var next = slug(t.textContent);
    var match = pills.some(function (b) { return b.getAttribute('data-tag') === next; });
    if (!match) return;
    e.preventDefault();
    e.stopPropagation();
    tag = (tag === next) ? '' : next;
    apply();
  });

  if (empty) {
    var clear = empty.querySelector('.btn');
    if (clear) {
      clear.addEventListener('click', function (e) {
        e.preventDefault();
        type = 'all';
        tag = '';
        apply();
      });
    }
  }

  var fromQuery = (location.search.match(/[?&]type=([a-z-]+)/) || [])[1];
  var fromHash = location.hash ? location.hash.slice(1) : '';
  setType(fromQuery || fromHash || 'all');
  apply();
})();
