---
title: dsh-market
description: DSH 内置的插件市场应用：在「插件」页提供一个「市场」标签页，浏览、搜索、筛选、一键安装与切换版本。列表来自官方维护的 awesome-dsh-plugin 精选 Registry（4200+ 插件），支持评论、收藏、分组、备份恢复与更新。
categories:
- market
tags: &id001
- 必装
- 一键安装
- 入口
weight: 1110
params:
  plugin:
    id: dsh-market
    name: dsh-market
    aliases:
    - 插件市场
    - dshmarket
    category: market
    status: community
    repo: https://github.com/dsh-market/dsh-market
    install: dsh plugin --profile web add dshmarket
    summary: DSH 内置的插件市场应用：在「插件」页提供一个「市场」标签页，浏览、搜索、筛选、一键安装与切换版本。列表来自官方维护的 awesome-dsh-plugin 精选 Registry（4200+ 插件），支持评论、收藏、分组、备份恢复与更新。
    features:
    - 浏览 / 搜索 / 一键安装：接入官方 curated Registry，卡片带分类、星标、双语描述
    - 宿主感知发现：卡片标注所需 DSH 版本，自动过滤确认不兼容项
    - 主题中心、收藏夹、分组开关、备份恢复（WebDAV / Gist 同步）
    - 更新管理、热禁用 / 卸载（写 cordis.patch.yml，~1s HMR 重组成）；安全策略拒绝非 Registry 来源
    tags: *id001
    flag: 安装写法有多种，以仓库 README 为准
    notes: dsh 0.2.1+ 市场是「插件」页的一个标签页；旧版在「设置 → 插件市场」打开，需 dsh web 0.1.0-rc.6+。注意：在装了 DSH Desktop 的机器上用命令行 add 可能装进 profiles/web 而非 Desktop 实际使用的 profile，桌面端请在应用内 Settings → Plugins 安装。
    repo_confirmed: true
    gh:
      stars: 12882
      forks: 491
      issues: 117
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-18T20:53:09Z'
      archived: false
      slug: dsh-market/dsh-market
      stars_label: 12.9k
      forks_label: '491'
      pushed_date: '2026-11-18'
    category_label: 插件市场与发现
    status_label: 社区
    weight: 1110
    url: /plugins/dsh-market/
  generated: true
---

DSH 内置的插件市场应用：在「插件」页提供一个「市场」标签页，浏览、搜索、筛选、一键安装与切换版本。列表来自官方维护的 awesome-dsh-plugin 精选 Registry（4200+ 插件），支持评论、收藏、分组、备份恢复与更新。
