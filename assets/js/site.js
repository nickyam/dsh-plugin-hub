/* 首页筛选 / 本地搜索 / 分类吸顶 / 复制命令，零依赖 */
(function () {
  /* ── 详情页：复制安装命令（所有页面都跑，和首页搜索无关） ── */
  function bindCopy() {
    document.querySelectorAll('[data-copy]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var text = btn.getAttribute('data-copy') || '';
        var done = function () {
          var old = btn.textContent;
          btn.textContent = '已复制';
          btn.classList.add('is-done');
          setTimeout(function () { btn.textContent = old; btn.classList.remove('is-done'); }, 1600);
        };
        var fallback = function () {
          var ta = document.createElement('textarea');
          ta.value = text;
          ta.setAttribute('readonly', '');
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); done(); } catch (e) {}
          document.body.removeChild(ta);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, fallback);
        } else {
          fallback();
        }
      });
    });
  }
  bindCopy();

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

  /* 筛选 / 搜索 / 页码写回地址栏：以前刷新即丢，也没法把「桌宠这一类」发出去 */
  function syncUrl() {
    if (!window.history || !history.replaceState) return;
    var params = new URLSearchParams(location.search);
    if (active === 'all') params.delete('c'); else params.set('c', active);
    var q = input.value.trim();
    if (q) params.set('q', q); else params.delete('q');
    if (page > 1) params.set('p', String(page)); else params.delete('p');
    var qs = params.toString();
    var url = location.pathname + (qs ? '?' + qs : '') + location.hash;
    history.replaceState(null, '', url);
  }

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
    syncUrl();
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

  function setActive(id) {
    active = id;
    filters.forEach(function (b) {
      var on = b.getAttribute('data-filter') === id;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  filters.forEach(function (btn) {
    btn.setAttribute('aria-pressed', btn.classList.contains('is-active') ? 'true' : 'false');
    btn.addEventListener('click', function () {
      setActive(btn.getAttribute('data-filter'));
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

  // 初始状态：优先按地址栏里的 ?c= / ?q= / ?p= 还原（刷新、分享都能落回同一个视图）
  var params = new URLSearchParams(location.search);
  var initQ = params.get('q') || '';
  var initC = params.get('c') || 'all';
  var initP = parseInt(params.get('p') || '1', 10);
  if (initQ) input.value = initQ;
  if (initC !== 'all' && filters.some(function (b) { return b.getAttribute('data-filter') === initC; })) {
    setActive(initC);
  }
  page = initP > 0 ? initP : 1;
  apply(false);
})();
