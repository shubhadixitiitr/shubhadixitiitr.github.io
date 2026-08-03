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

  /* ── highlight the section you are reading ─────────── */
  var navLinks = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]'));
  var sections = navLinks
    .map(function (a) { return document.querySelector(a.getAttribute('href')); })
    .filter(Boolean);

  if ('IntersectionObserver' in window && sections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (a) {
          a.classList.toggle('is-current', a.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

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
