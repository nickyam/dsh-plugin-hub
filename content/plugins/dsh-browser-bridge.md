---
title: dsh-browser-bridge（浏览器桥接扩展）
description: 把 DSH 接到你正在用的 Chrome / Firefox 标签页上的桥插件加 MV3 扩展：模型直接读取当前页面、点按输入、导航和管理标签页，复用已有登录态与 Cookie，侧栏即可对话；无需视觉能力即可操作浏览器。与本站已收的 dsh-browser（CJYLZS，每会话起一个隔离 Chrome 进程）是两套不同实现。
categories:
- tool
tags: []
weight: 1010
params:
  plugin:
    id: dsh-browser-bridge
    name: dsh-browser-bridge（浏览器桥接扩展）
    aliases:
    - dsh-brows
    - dsh-browser 浏览器助手
    - dsh 浏览器操作
    category: tool
    status: community
    repo: https://github.com/omdsh-dev/dsh-browser
    install: curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash
    summary: 把 DSH 接到你正在用的 Chrome / Firefox 标签页上的桥插件加 MV3 扩展：模型直接读取当前页面、点按输入、导航和管理标签页，复用已有登录态与 Cookie，侧栏即可对话；无需视觉能力即可操作浏览器。与本站已收的 dsh-browser（CJYLZS，每会话起一个隔离 Chrome 进程）是两套不同实现。
    features:
    - 连接现有标签页：不新起浏览器实例，保留登录态、会话与 Cookie；Chrome 本机免配置，Firefox 需在扩展设置里填 ~/.dsh/ext-bridge-token 的 bearer token
    - 结构化页面读取：browser_snapshot 给标题/URL/正文/带编号交互清单/表单字段，敏感值掩码；delta 只看变化，query 按文本/选择器/角色定位
    - 受控交互：按编号或选择器点击双击、输入（兼容 React/Vue 受控组件）、按键组合、滚动、剪贴板、文件上传；支持跨域 iframe
    - 标签页管理：列出/跟随/关闭/新开/前进后退刷新；截图需受控标签页在前台且窗口聚焦
    - 划选即引用：页面里划选的文字连同来源与不可信内容边界一起进下一条消息；失败可点「继续生成」
    - 侧栏内发图：宿主声明图片能力时可发 PNG/JPEG/WebP/GIF；受保护页面与扩展商店只读元数据，不碰 DOM
    flag: 安装脚本来自 Lum1104 旧仓（GitHub 已 301 到 omdsh-dev），与已收的 CJYLZS/dsh-browser 不是同一个项目，别装重了
    notes: 仓库 github.com/Lum1104/dsh-browser 在 GitHub API 里 full_name 已返回 omdsh-dev/dsh-browser（重定向），README 的安装脚本仍写 Lum1104 路径，故 install 按 README 原文保留。npm 上无 scope 的 dsh-browser 属另一个项目（即本站已收的 @cjylzs/dsh-browser），本仓库没发 npm 包，只能走安装器。前置 Node.js>=24.9.0、Corepack/pnpm、Chrome 125+ 或 Firefox 140+；工作区固定 DSH 0.2.2-rc.2，其他版本未声明支持。安装器打开 chrome://extensions 后需手动加载或重新加载扩展，dsh 正在运行要重启。README 附 2026-08-18 的 60 次配对评测（扩展 30/30 成功、平均 5.32s，对比 Playwright 6.67s）属作者口径，本站不采信为独立结论。
    repo_confirmed: true
    gh:
      stars: 1101
      forks: 87
      issues: 35
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-15T12:13:45Z'
      archived: false
      slug: omdsh-dev/dsh-browser
      stars_label: '1101'
      forks_label: '87'
      pushed_date: '2026-11-15'
      updated_label: 6 天前有提交
      updated_days: 6
      stale: false
    entry_updated: '2026-11-19'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-browser-bridge/
  generated: true
---

把 DSH 接到你正在用的 Chrome / Firefox 标签页上的桥插件加 MV3 扩展：模型直接读取当前页面、点按输入、导航和管理标签页，复用已有登录态与 Cookie，侧栏即可对话；无需视觉能力即可操作浏览器。与本站已收的 dsh-browser（CJYLZS，每会话起一个隔离 Chrome 进程）是两套不同实现。
