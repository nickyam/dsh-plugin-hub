---
title: dsh-guizang-design
description: 把「歸藏」的内容生产 skill 装进 DSH，提供网页 PPT、图文卡片、网页排版、去 AI 味，外加学你写作语气的语气档案，共用一套设计系统。
categories:
- visual
tags: &id001
- 设计
- PPT
- 排版
- 去AI味
- 语气档案
weight: 1010
params:
  plugin:
    id: dsh-guizang-design
    name: dsh-guizang-design
    aliases:
    - 歸藏设计
    category: visual
    status: community
    repo: https://github.com/op7418/dsh-guizang-design
    install: dsh plugin --profile web add dsh-guizang-design
    summary: 把「歸藏」的内容生产 skill 装进 DSH，提供网页 PPT、图文卡片、网页排版、去 AI 味，外加学你写作语气的语气档案，共用一套设计系统。
    features:
    - 五个 skill：网页 PPT（/guizang-ppt-skill）、图文卡片（/guizang-social-card-skill）、网页排版（/guizang-page-skill）、去 AI 味（/humanizer-zh）、语气档案（/guizang-voice）
    - 一套设计系统：PPT、卡片、网页共用 token，6 套杂志风与 4 套瑞士风主题，支持品牌色按 OKLCH 约束生成、字体子集化内嵌
    - 插件页面：概览、我的作品、内容生产工作流、语气档案、官方示例，作品自动登记进作品库、可一键「做同款」
    - 跨 skill 工作流：一篇文章三种出口、先去 AI 味再排版、演讲回收、品牌套件、封面矩阵、中英双版本
    - 语气档案：从本机 DSH 会话与你写过的文章学出写作习惯，每条特征需至少两处证据，去 AI 味与代写时复用
    tags: *id001
    notes: 社区项目（作者 op7418，非 DeepSeek 官方）。需 DSH 0.2.1-rc.2 及以上、0.3.0 以下；包名即 dsh-guizang-design，也支持 github:op7418/dsh-guizang-design 指定版本。卡片出图依赖 Playwright Chromium，网页导出 PDF 与长图依赖本机 Chrome。文章（wx-feishu）称其「一篇文章变网页、图文卡片或封面」与此一致。
    refs:
    - id: wx-feishu
      title: 3.5 万个插件里，DeepSeek 官方为什么只挑了这 4 个?
      url: https://mp.weixin.qq.com/s/pdJ8cQW1Ua_jhtRR7wR8iQ
      kind_label: 公众号
      publisher: 飞叔（公众号：飞叔 AI赋能推客）
    source_count: 1
    repo_confirmed: true
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-guizang-design/
  generated: true
---

把「歸藏」的内容生产 skill 装进 DSH，提供网页 PPT、图文卡片、网页排版、去 AI 味，外加学你写作语气的语气档案，共用一套设计系统。
