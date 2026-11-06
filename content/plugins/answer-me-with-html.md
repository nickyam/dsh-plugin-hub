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
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/answer-me-with-html/
  generated: true
---

一个 agent skill，用一页可交互的单文件 HTML 回答复杂问题：内含流程图、对比表格、交互图表，离线可打开、便于分享。
