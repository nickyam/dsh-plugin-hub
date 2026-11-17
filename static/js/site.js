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

  // 分类栏横向滚动提示：还有内容时显示渐隐 + 右箭头，滚到头自动隐藏
  var filtersWrap = document.querySelector('.filters-wrap');
  var filtersTrack = document.querySelector('.filters');
  var nextBtn = document.querySelector('.filters-next');
  if (filtersWrap && filtersTrack && nextBtn) {
    function syncMore() {
      var max = filtersTrack.scrollWidth - filtersTrack.clientWidth;
      // 留 8px 容差，避免在终点因亚像素误差反复闪烁
      filtersWrap.classList.toggle('has-more', max > 8 && filtersTrack.scrollLeft < max - 8);
    }
    nextBtn.addEventListener('click', function () {
      filtersTrack.scrollBy({ left: Math.max(filtersTrack.clientWidth - 80, 240), behavior: 'smooth' });
    });
    filtersTrack.addEventListener('scroll', syncMore, { passive: true });
    window.addEventListener('resize', syncMore);
    // 字体加载完成后文字宽度会变，重算一次避免初始判断偏差
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(syncMore);
    syncMore();
  }

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
