/* 首页筛选与本地搜索，零依赖 */
(function () {
  var input = document.getElementById('q');
  if (!input) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('#cards .card'));
  var filters = Array.prototype.slice.call(document.querySelectorAll('.filter'));
  var count = document.getElementById('result-count');
  var noResult = document.getElementById('no-result');
  var active = 'all';

  function apply() {
    var q = input.value.trim().toLowerCase();
    var n = 0;
    cards.forEach(function (card) {
      var okCat = active === 'all' || card.getAttribute('data-category') === active;
      var okQuery = !q || (card.getAttribute('data-hay') || '').indexOf(q) !== -1;
      var show = okCat && okQuery;
      card.hidden = !show;
      if (show) n++;
    });
    if (count) count.textContent = n + ' 个插件';
    if (noResult) noResult.hidden = n !== 0;
  }

  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filters.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      active = btn.getAttribute('data-filter');
      apply();
    });
  });

  input.addEventListener('input', apply);

  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input &&
        !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
      e.preventDefault();
      input.focus();
      input.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }
    if (e.key === 'Escape' && document.activeElement === input) {
      input.value = '';
      apply();
      input.blur();
    }
  });

  // 从其它页带 #catalog 回来时，把光标直接放进搜索框
  if (location.hash === '#catalog' || /[?&]q=/.test(location.search)) {
    var m = location.search.match(/[?&]q=([^&]+)/);
    if (m) { input.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); apply(); }
  }
})();
