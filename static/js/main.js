/**
 * Uritani Laboratory - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function () {

  // ============================================================
  // Mobile Navigation Toggle
  // ============================================================
  const toggle = document.querySelector('.nav-toggle');
  const nav    = document.querySelector('.site-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', nav.classList.contains('is-open'));
    });

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', false);
      });
    });
  }

  // ============================================================
  // Active nav link highlight
  // ============================================================
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.site-nav a').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // ============================================================
  // Scroll Reveal
  // ============================================================
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length > 0 && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    // フォールバック: IntersectionObserver 未対応ブラウザ
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // ============================================================
  // Publication Filter
  // ============================================================
  var filterBtns = document.querySelectorAll('.filter-btn[data-filter]');
  if (filterBtns.length > 0) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var filter = btn.dataset.filter;

        filterBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');

        document.querySelectorAll('.publication-entry').forEach(function (entry) {
          if (filter === 'all') {
            entry.style.display = '';
          } else {
            entry.style.display = entry.querySelector('.entry-type.' + filter) ? '' : 'none';
          }
        });

        /* 空の年度セクションを非表示 */
        document.querySelectorAll('.publication-year').forEach(function (section) {
          var visible = section.querySelectorAll('.publication-entry:not([style*="none"])');
          section.style.display = visible.length > 0 ? '' : 'none';
        });
      });
    });
  }

});

