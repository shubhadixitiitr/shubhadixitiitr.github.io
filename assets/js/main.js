/* Shubha Dixit — site behaviour
   Kept deliberately small: no build step, no dependencies. */

(function () {
  'use strict';

  /* ── sticky header ─────────────────────────────────── */
  var header = document.getElementById('siteHeader');
  function onScroll() {
    header.classList.toggle('is-stuck', window.scrollY > 40);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── mobile menu ───────────────────────────────────── */
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('primaryNav');

  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });

  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  /* ── reveal on scroll ──────────────────────────────── */
  var revealables = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.12 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ── Research dropdown ─────────────────────────────── */
  var groups = Array.prototype.slice.call(nav.querySelectorAll('.has-sub'));

  groups.forEach(function (group) {
    var button = group.querySelector('.sub-toggle');
    if (!button) return;

    button.addEventListener('click', function (e) {
      e.preventDefault();
      var open = !group.classList.contains('is-open');
      groups.forEach(function (g) {
        g.classList.remove('is-open');
        var b = g.querySelector('.sub-toggle');
        if (b) b.setAttribute('aria-expanded', 'false');
      });
      if (open) {
        group.classList.add('is-open');
        button.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // click away, or press Escape, to close
  document.addEventListener('click', function (e) {
    groups.forEach(function (g) {
      if (g.contains(e.target)) return;
      g.classList.remove('is-open');
      var b = g.querySelector('.sub-toggle');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    groups.forEach(function (g) {
      g.classList.remove('is-open');
      var b = g.querySelector('.sub-toggle');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  });

  /* ── latest-publications carousel ──────────────────── */
  var carousel = document.getElementById('pubCarousel');
  if (carousel) {
    var slides = carousel.querySelectorAll('.pub-slide');
    var dots = carousel.querySelectorAll('.pub-dots button');
    var index = 0;
    var timer;

    function show(i) {
      index = (i + slides.length) % slides.length;
      slides.forEach(function (s, n) { s.classList.toggle('is-active', n === index); });
      dots.forEach(function (d, n) {
        d.classList.toggle('is-active', n === index);
        d.setAttribute('aria-selected', String(n === index));
      });
    }

    function start() { timer = setInterval(function () { show(index + 1); }, 6000); }
    function stop() { clearInterval(timer); }

    dots.forEach(function (dot, n) {
      dot.addEventListener('click', function () { stop(); show(n); start(); });
    });

    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);

    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) start();
  }

  /* ── footer year ───────────────────────────────────── */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

})();
