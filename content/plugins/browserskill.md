---
title: BrowserSkill
description: 让 AI Agent 连上你真实已登录的 Chrome / Edge 浏览器，复用已有登录态去读页面、填表单、截图；任务跑在独立可见的 Agent Window，需要人工介入的（验证码 / 登录 / 确认）由你接管后继续。
categories:
- tool
tags: &id001
- 浏览器
- 自动化
- 腾讯
weight: 1010
params:
  plugin:
    id: browserskill
    name: BrowserSkill
    aliases:
    - 浏览器技能
    category: tool
    status: community
    repo: https://github.com/Tencent/BrowserSkill
    install: dsh plugin --profile web add @wxg-prc-cpg/browser-skill-dsh-plugin
    summary: 让 AI Agent 连上你真实已登录的 Chrome / Edge 浏览器，复用已有登录态去读页面、填表单、截图；任务跑在独立可见的 Agent Window，需要人工介入的（验证码 / 登录 / 确认）由你接管后继续。
    features:
    - 复用真实浏览器的已登录会话，无需另开测试账号
    - 任务在独立、可见的 Agent Window 执行；需要时显式借用已有标签页，用完归还
    - 验证码 / 登录 / 确认等人机步骤由你接管，完成后 Agent 继续任务
    - DSH 插件注入原生 bsk_* 工具与实时 Web UI 覆盖
    - 官方仅支持 Chrome 与 Microsoft Edge（其他 Chromium 可能可用）
    tags: *id001
    notes: 由腾讯维护的社区项目（与 DeepSeek 无隶属关系）；安装前需先装 bsk CLI 与浏览器扩展，并让 bsk 在 DSH 启用的 PATH 上可用。
    repo_confirmed: true
    gh:
      stars: 10758
      forks: 789
      issues: 103
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-26T07:10:06Z'
      archived: false
      slug: Tencent/BrowserSkill
      stars_label: 10.8k
      forks_label: '789'
      pushed_date: '2026-11-26'
      updated_label: 今天有提交
      updated_days: 0
      stale: false
    entry_updated: '2026-11-06'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/browserskill/
  generated: true
lastmod: '2026-11-06'
---

让 AI Agent 连上你真实已登录的 Chrome / Edge 浏览器，复用已有登录态去读页面、填表单、截图；任务跑在独立可见的 Agent Window，需要人工介入的（验证码 / 登录 / 确认）由你接管后继续。
