/* 首页筛选与本地搜索，零依赖 */
(function () {
  var input = document.getElementById('q');
  if (!input) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('#cards .card'));
  var filters = Array.prototype.slice.call(document.querySelectorAll('.filter'));
  var count = document.getElementById('result-count');
  var noResult = document.getElementById('no-result');
  var pager = document.getElementById('pager');
  var pagerPages = document.getElementById('pager-pages');
  var active = 'all';
  var PAGE_SIZE = 24;
  var filtersWrap = document.querySelector('.filters-wrap');
  var headerEl = document.querySelector('.site-header');
  function headerH() { return headerEl ? headerEl.offsetHeight : 64; }
  var page = 1;
  var visible = []; // 当前筛选下命中的卡片（按页面顺序）

  function renderPager(totalPages) {
    if (!pager || !pagerPages) return;
    pager.hidden = totalPages <= 1;
    pagerPages.textContent = '';
    function addNum(p) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'pager-num' + (p === page ? ' is-current' : '');
      b.textContent = String(p);
      b.setAttribute('aria-label', '第 ' + p + ' 页');
      if (p === page) b.setAttribute('aria-current', 'page');
      b.addEventListener('click', function () { goto(p); });
      pagerPages.appendChild(b);
    }
    function addEllipsis() {
      var s = document.createElement('span');
      s.className = 'pager-ellipsis';
      s.textContent = '…';
      pagerPages.appendChild(s);
    }
    // 页数不多时全列；多了只显示首尾与当前页附近，中间用省略号
    if (totalPages <= 9) {
      for (var i = 1; i <= totalPages; i++) addNum(i);
    } else {
      addNum(1);
      var from = Math.max(2, page - 2);
      var to = Math.min(totalPages - 1, page + 2);
      if (from > 2) addEllipsis();
      for (var j = from; j <= to; j++) addNum(j);
      if (to < totalPages - 1) addEllipsis();
      addNum(totalPages);
    }
    var prev = pager.querySelector('[data-page="prev"]');
    var next = pager.querySelector('[data-page="next"]');
    if (prev) prev.disabled = page <= 1;
    if (next) next.disabled = page >= totalPages;
  }

  function apply(resetPage) {
    if (resetPage) page = 1;
    var q = input.value.trim().toLowerCase();
    visible = [];
    cards.forEach(function (card) {
      var okCat = active === 'all' || card.getAttribute('data-category') === active;
      var okQuery = !q || (card.getAttribute('data-hay') || '').indexOf(q) !== -1;
      card.hidden = true;
      if (okCat && okQuery) visible.push(card);
    });
    var totalPages = Math.max(1, Math.ceil(visible.length / PAGE_SIZE));
    if (page > totalPages) page = totalPages;
    var start = (page - 1) * PAGE_SIZE;
    visible.slice(start, start + PAGE_SIZE).forEach(function (card) { card.hidden = false; });
    if (count) count.textContent = visible.length + ' 个插件' + (totalPages > 1 ? '（第 ' + page + '/' + totalPages + ' 页）' : '');
    if (noResult) noResult.hidden = visible.length !== 0;
    renderPager(totalPages);
  }

  // 翻页后回到卡片区顶部，并让开头避开吸顶的 header + 分类栏
  function scrollToCardsTop() {
    var el = document.getElementById('cards');
    if (!el) return;
    var barH = filtersWrap ? filtersWrap.offsetHeight : 0;
    var y = el.getBoundingClientRect().top + window.pageYOffset - headerH() - barH - 8;
    window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
  }

  function goto(p) {
    var totalPages = Math.max(1, Math.ceil(visible.length / PAGE_SIZE));
    var target = p === 'prev' ? page - 1 : p === 'next' ? page + 1 : p;
    if (target < 1 || target > totalPages || target === page) return;
    page = target;
    apply(false);
    scrollToCardsTop();
  }

  if (pager) {
    pager.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-page]');
      if (btn) goto(btn.getAttribute('data-page'));
    });
  }

  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filters.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      active = btn.getAttribute('data-filter');
      apply(true);
    });
  });

  input.addEventListener('input', function () { apply(true); });

  // 分类栏横向滚动提示：还有内容时显示渐隐 + 右箭头，滚到头自动隐藏
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

  // 分类栏吸顶：滚过搜索框后固定在 header 下方，加一道分隔线提示已吸附
  if (filtersWrap) {
    // 移动端 --header-h 是 auto（header 会折行），calc 会失效，这里把实测高度写进变量
    function syncHeaderVar() {
      document.documentElement.style.setProperty('--header-real-h', headerH() + 'px');
    }
    function syncStuck() {
      filtersWrap.classList.toggle('is-stuck', filtersWrap.getBoundingClientRect().top <= headerH() + 0.5);
    }
    var stuckRaf = false;
    window.addEventListener('scroll', function () {
      if (stuckRaf) return;
      stuckRaf = true;
      requestAnimationFrame(function () { stuckRaf = false; syncStuck(); });
    }, { passive: true });
    window.addEventListener('resize', function () { syncHeaderVar(); syncStuck(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(syncStuck);
    syncHeaderVar();
    syncStuck();
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
      apply(true);
      input.blur();
    }
  });

  // 从其它页带 #catalog 回来时，把光标直接放进搜索框
  if (location.hash === '#catalog' || /[?&]q=/.test(location.search)) {
    var m = location.search.match(/[?&]q=([^&]+)/);
    if (m) { input.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); apply(true); }
  }

  // 初始渲染：HTML 里卡片默认全显示，这里收窄到第一页（幂等，URL 带 q 时已调用过也无妨）
  apply(true);
})();
