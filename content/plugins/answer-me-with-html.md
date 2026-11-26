---
title: answer-me-with-html
description: 一个 agent skill，用一页可交互的单文件 HTML 回答复杂问题：内含流程图、对比表格、交互图表，离线可打开、便于分享。
categories:
- workflow
tags: &id001
- HTML
- 可视化回答
- 分享
weight: 1010
params:
  plugin:
    id: answer-me-with-html
    name: answer-me-with-html
    category: workflow
    status: community
    repo: https://github.com/QingYunA/answer-me-with-html
    install: dsh plugin --profile web add github:QingYunA/answer-me-with-html
    summary: 一个 agent skill，用一页可交互的单文件 HTML 回答复杂问题：内含流程图、对比表格、交互图表，离线可打开、便于分享。
    features:
    - 代码布局：面板摆放与图表坐标由代码计算，标签不被截断、网格无空隙
    - 单文件无依赖：每个页面是单个 .html，无 CDN 链接或网络字体，离线打开、易分享
    - 三种主题：blueprint（工程图）、shadcn（简洁卡片）、paper（长文阅读），均支持明 / 暗模式
    - 写作检查：草稿按改编自 ASD-STE100 的规则（长句、冗词、被动语态）检查，默认仅警告
    - 自动修正错误：草稿出错时 CLI 返回行号、组件名与正确示例，代理通常一次修复
    tags: *id001
    repo_confirmed: true
    gh:
      stars: 6531
      forks: 442
      issues: 15
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-18T19:55:16Z'
      archived: false
      slug: QingYunA/answer-me-with-html
      stars_label: '6531'
      forks_label: '442'
      pushed_date: '2026-11-18'
      updated_label: 7 天前有提交
      updated_days: 7
      stale: false
    entry_updated: '2026-11-06'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/answer-me-with-html/
  generated: true
---

一个 agent skill，用一页可交互的单文件 HTML 回答复杂问题：内含流程图、对比表格、交互图表，离线可打开、便于分享。
