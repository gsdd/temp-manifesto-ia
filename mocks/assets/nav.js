(function () {
  'use strict';

  var header = document.getElementById('siteHeader');
  var mega = document.getElementById('megaNav');
  var items = document.querySelectorAll('#primaryNav > li[data-menu]');
  var megaLi = document.querySelector('#primaryNav > li[data-menu="mega"]');
  var browser = document.getElementById('browser');
  var openTimer, closeTimer;
  var OPEN_DELAY = 150, CLOSE_DELAY = 300;
  if (!header || !mega || !megaLi) return;

  function setOpen(li, open) {
    var link = li.querySelector('.top-link');
    if (li.getAttribute('data-menu') === 'mega') {
      header.setAttribute('data-mega-open', open ? 'true' : 'false');
      if (browser) browser.setAttribute('data-mega-open', open ? 'true' : 'false');
    } else {
      li.setAttribute('data-open', open ? 'true' : 'false');
    }
    if (link) link.setAttribute('aria-expanded', open ? 'true' : 'false');
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
    li.addEventListener('mouseenter', function () {
      clearTimeout(closeTimer);
      openTimer = setTimeout(function () { openOnly(li); }, OPEN_DELAY);
    });
    li.addEventListener('mouseleave', function () {
      clearTimeout(openTimer);
      closeTimer = setTimeout(function () { setOpen(li, false); }, CLOSE_DELAY);
    });
    if (link) {
      link.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          openOnly(li);
          var first = (li.getAttribute('data-menu') === 'mega' ? mega : li).querySelector('a:not(.top-link)');
          if (first) first.focus();
        }
      });
    }
  });

  Array.prototype.forEach.call(document.querySelectorAll('#primaryNav > li:not([data-menu])'), function (li) {
    li.addEventListener('mouseenter', function () {
      clearTimeout(openTimer);
      closeTimer = setTimeout(closeAll, CLOSE_DELAY);
    });
  });

  mega.addEventListener('mouseenter', function () { clearTimeout(closeTimer); });
  mega.addEventListener('mouseleave', function () {
    closeTimer = setTimeout(function () { setOpen(megaLi, false); }, CLOSE_DELAY);
  });

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
