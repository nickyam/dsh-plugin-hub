---
title: dsh-browser（真实浏览器）
description: 给每个会话配一个真实的 Chrome / Edge 进程并在右侧栏实时镜像，模型用一组工具点网页、填表单、翻页，用户可随时在镜像里接管；会话之间标签页、登录态与 CDP 端口完全隔离，Web 与桌面端都能用。
categories:
- tool
tags: &id001
- 浏览器
- 自动化
- CDP
- 会话隔离
weight: 1030
params:
  plugin:
    id: dsh-browser
    name: dsh-browser（真实浏览器）
    aliases:
    - '@cjylzs/dsh-browser'
    - 会话浏览器
    category: tool
    status: community
    repo: https://github.com/CJYLZS/dsh-browser
    install: dsh plugin --profile web add @cjylzs/dsh-browser
    summary: 给每个会话配一个真实的 Chrome / Edge 进程并在右侧栏实时镜像，模型用一组工具点网页、填表单、翻页，用户可随时在镜像里接管；会话之间标签页、登录态与 CDP 端口完全隔离，Web 与桌面端都能用。
    features:
    - 每会话一个真实浏览器：独立 profile、独立 CDP 端口，标签页与登录态在会话间不共享；不是内嵌 webview，站点看到的是普通浏览器
    - 可观看可接管：每个页面在侧栏有独立实时视图，镜像里的点击与输入能传到真实页面
    - 读取陌生页面：browser_snapshot 输出带 ref 的无障碍树供模型定位元素，find 缩小大页面，boxes 给坐标无需截图
    - 真实输入事件：在元素自身位置发真实鼠标与文本事件（连忽略合成 element.click() 的页面也认），支持 Ctrl+A 组合键、原生下拉与勾选、弹窗当场应答
    - 可被外部接管：每个浏览器监听外部 CDP 端口，chrome://inspect、另一个 Playwright 或自带 scripts/cdp.mjs 可 attach 到同一浏览器
    - 内置工作规则：贡献一份 skill，要求先读后操作、一次动作一次观察、页面文本当数据而非指令
    tags: *id001
    flag: 社区项目；模型可操作真实浏览器与登录态，涉及账号与付款操作时请留意
    notes: 仓库 CJYLZS/dsh-browser（main/master 同指一份 README），npm 包为 scoped 名 @cjylzs/dsh-browser，README 最新 v0.3.x（文章写 github tag v0.2.3，为旧版）。旧的无 scope 名 dsh-browser 在 npm 上属于另一个项目，若 profile 里还留着旧键须先 `dsh plugin --profile web remove dsh-browser` 再装。按 DSH 版本选版本：>=0.1.7-rc.1 用 v0.3.x；0.1.5-rc.2 只能用 v0.1.0（tag 安装）。需本机已装 Chrome 或 Edge，playwright-core 不自带浏览器。装完重启宿主。桌面端要用其自带 CLI 的 --profile desktop 安装。
    repo_confirmed: true
    gh:
      stars: 5
      forks: 2
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-06T12:03:08Z'
      archived: false
      slug: CJYLZS/dsh-browser
      stars_label: '5'
      forks_label: '2'
      pushed_date: '2026-11-06'
    category_label: 工具与能力
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-browser/
  generated: true
---

给每个会话配一个真实的 Chrome / Edge 进程并在右侧栏实时镜像，模型用一组工具点网页、填表单、翻页，用户可随时在镜像里接管；会话之间标签页、登录态与 CDP 端口完全隔离，Web 与桌面端都能用。
