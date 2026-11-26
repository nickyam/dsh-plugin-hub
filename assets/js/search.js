/* 全站搜索浮层：数据来自 static/search.json（首次打开才下载，当前约 76KB gzip） */
(function () {
  var dlg = document.getElementById('site-search');
  if (!dlg || typeof dlg.showModal !== 'function') return;

  var input = document.getElementById('site-search-input');
  var list = document.getElementById('site-search-results');
  var empty = document.getElementById('site-search-empty');
  var hint = document.getElementById('site-search-hint');
  var more = document.getElementById('site-search-more');
  var moreLink = document.getElementById('site-search-more-link');
  var base = (document.documentElement.getAttribute('data-base') || '/');
  var data = null;
  var loading = false;
  var results = [];
  var cursor = -1;

  function href(url) {
    // search.json 里的 url 是站点根相对路径（/plugins/xxx/），要拼上子目录前缀
    return base + String(url || '').replace(/^\//, '');
  }

  function load(cb) {
    if (data) { cb(); return; }
    if (loading) return;
    loading = true;
    fetch(base + 'search.json', { credentials: 'same-origin' })
      .then(function (r) { return r.json(); })
      .then(function (json) {
        data = json || [];
        loading = false;
        cb();
      })
      .catch(function () {
        loading = false;
        if (hint) hint.textContent = '搜索索引没加载下来，刷新一次试试。';
      });
  }

  function esc(s) {
    return String(s || '').replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  function mark(text, q) {
    if (!q) return esc(text);
    var src = String(text || '');
    var lower = src.toLowerCase();
    var at = lower.indexOf(q);
    if (at < 0) return esc(src);
    return esc(src.slice(0, at)) + '<mark>' + esc(src.slice(at, at + q.length)) + '</mark>' + esc(src.slice(at + q.length));
  }

  function score(item, q) {
    var s = 0;
    var name = String(item.name || '').toLowerCase();
    var aliases = (item.aliases || []).map(function (a) { return String(a).toLowerCase(); });
    var tags = (item.tags || []).map(function (t) { return String(t).toLowerCase(); });
    if (name === q) s += 120;
    else if (name.indexOf(q) === 0) s += 90;
    else if (name.indexOf(q) > -1) s += 65;
    for (var i = 0; i < aliases.length; i++) {
      if (aliases[i] === q) { s += 80; break; }
      if (aliases[i].indexOf(q) > -1) s += 45;
    }
    for (var j = 0; j < tags.length; j++) {
      if (tags[j].indexOf(q) > -1) s += 30;
    }
    if (String(item.summary || '').toLowerCase().indexOf(q) > -1) s += 18;
    if ((item.features || []).join(' ').toLowerCase().indexOf(q) > -1) s += 12;
    if (String(item.notes || '').toLowerCase().indexOf(q) > -1) s += 8;
    if (String(item.install || '').toLowerCase().indexOf(q) > -1) s += 6;
    if (String(item.category_label || '').toLowerCase().indexOf(q) > -1) s += 6;
    return s;
  }

  function render(q) {
    if (!list) return;
    list.textContent = '';
    cursor = -1;
    if (more) more.hidden = true;
    if (!q) {
      if (hint) hint.textContent = '按名字、别名、标签、功能亮点搜；↑↓ 选择，回车打开。';
      if (empty) empty.hidden = true;
      return;
    }
    var matched = (data || [])
      .map(function (item) { return { item: item, s: score(item, q) }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (a, b) { return b.s - a.s; });
    results = matched.slice(0, 12).map(function (x) { return x.item; });

    if (!results.length) {
      if (hint) hint.textContent = '没有命中。';
      if (empty) {
        empty.hidden = false;
        empty.innerHTML = '没找到「<b>' + esc(q) + '</b>」相关的插件。试试别名（「全家桶」「桌宠」），或者少打两个字。';
      }
      return;
    }
    if (empty) empty.hidden = true;
    if (hint) {
      hint.textContent = matched.length > results.length
        ? '共 ' + matched.length + ' 条，这里先给前 ' + results.length + ' 条。'
        : '找到 ' + results.length + ' 条，↑↓ 选择，回车打开。';
    }
    // 结果被 12 条上限截断时，给一个通往插件库的出口（那边按 ?q= 接着筛）
    if (more && moreLink) {
      if (matched.length > results.length) {
        moreLink.href = base + '?q=' + encodeURIComponent((input && input.value.trim()) || q);
        more.hidden = false;
      } else {
        more.hidden = true;
      }
    }

    results.forEach(function (item, idx) {
      var li = document.createElement('li');
      li.className = 'search-item';
      li.setAttribute('role', 'option');
      li.id = 'search-opt-' + idx;
      var a = document.createElement('a');
      a.href = href(item.url);
      a.innerHTML =
        '<span class="search-item-top">' +
          '<span class="search-item-name">' + mark(item.name, q) + '</span>' +
          '<span class="search-item-cat">' + esc(item.category_label) +
            (item.stars_label ? ' ｜ ★ ' + esc(item.stars_label) : '') + '</span>' +
        '</span>' +
        '<p class="search-item-sum">' + mark(item.summary, q) + '</p>';
      li.appendChild(a);
      list.appendChild(li);
    });
    setCursor(0);
  }

  function setCursor(i) {
    var items = list ? list.querySelectorAll('.search-item') : [];
    if (!items.length) return;
    if (i < 0) i = items.length - 1;
    if (i >= items.length) i = 0;
    cursor = i;
    items.forEach(function (el, idx) {
      el.classList.toggle('is-active', idx === i);
      el.setAttribute('aria-selected', idx === i ? 'true' : 'false');
    });
    if (input) input.setAttribute('aria-activedescendant', 'search-opt-' + i);
    var active = items[i];
    if (active && active.scrollIntoView) active.scrollIntoView({ block: 'nearest' });
  }

  function open() {
    if (!dlg.open) dlg.showModal();
    document.body.style.overflow = 'hidden';
    load(function () {
      if (!input.value) render('');
      input.focus();
      input.select();
    });
  }

  function close() {
    if (dlg.open) dlg.close();
    document.body.style.overflow = '';
  }

  document.querySelectorAll('[data-search-open]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      open();
    });
  });
  document.querySelectorAll('[data-search-close]').forEach(function (btn) {
    btn.addEventListener('click', close);
  });
  dlg.addEventListener('click', function (e) {
    if (e.target === dlg) close();
  });
  dlg.addEventListener('close', function () { document.body.style.overflow = ''; });

  if (input) {
    var timer = null;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      clearTimeout(timer);
      timer = setTimeout(function () { render(q); }, 60);
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); setCursor(cursor + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setCursor(cursor - 1); }
      else if (e.key === 'Enter') {
        var items = list.querySelectorAll('.search-item a');
        if (items[cursor]) { e.preventDefault(); items[cursor].click(); close(); }
      }
    });
  }

  document.addEventListener('keydown', function (e) {
    var tag = (document.activeElement && document.activeElement.tagName) || '';
    var typing = /^(INPUT|TEXTAREA|SELECT)$/.test(tag);
    // ⌘K / Ctrl+K：任何页面都唤起
    if ((e.metaKey || e.ctrlKey) && String(e.key).toLowerCase() === 'k') {
      e.preventDefault();
      if (dlg.open) close(); else open();
      return;
    }
    // “/”：首页留给行内搜索框（即时筛卡片），其它页面唤起浮层
    if (e.key === '/' && !typing && !document.getElementById('q')) {
      e.preventDefault();
      open();
    }
  });
})();
