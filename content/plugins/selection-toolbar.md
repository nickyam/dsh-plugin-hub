---
title: 划词工具条
description: 在 DSH 会话里划选文本，选区上方浮现浮动工具栏（复制 / 引用 / 询问 / 解释 / 翻译 / 总结 //btw）；AI 动作默认就地弹窗，可一键「转到主线」把回答发进当前对话。
categories:
- ui
tags: &id001
- 划词
- 交互
weight: 1010
params:
  plugin:
    id: selection-toolbar
    name: 划词工具条
    category: ui
    status: unknown
    repo: https://github.com/suiyideali/dsh-selection-toolbar
    install: dsh plugin --profile web add github:suiyideali/dsh-selection-toolbar
    summary: 在 DSH 会话里划选文本，选区上方浮现浮动工具栏（复制 / 引用 / 询问 / 解释 / 翻译 / 总结 //btw）；AI 动作默认就地弹窗，可一键「转到主线」把回答发进当前对话。
    features:
    - 选区上方浮动工具栏：复制 / 引用 / 询问 / 解释 / 翻译 / 总结 //btw
    - /btw 侧问：答案只显示在弹窗，不进对话、不打断主任务
    - 答案去向三路（就地弹窗 / 进对话 //btw）可逐动作切换
    - 设置卡片可调弹出延时、逐按钮开关，并写回 profile 配置
    - AI 动作复用当前会话，划选内容作为素材以 Markdown 引用块注入
    tags: *id001
    notes: 本插件只经 git 分发，不发布到 npm；桌面端请在应用内「插件 → 添加插件」填同一地址。装完后刷新页面即可（仅改动 host 半端时才需重启 dsh web / 桌面应用）。
    refs:
    - id: wx-dabaihua
      title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      kind_label: 公众号
      publisher: 微信公众号（原文署名待补）
    source_count: 1
    repo_confirmed: true
    category_label: 界面与体验
    status_label: 原文未说明
    weight: 1010
    url: /plugins/selection-toolbar/
  generated: true
---

在 DSH 会话里划选文本，选区上方浮现浮动工具栏（复制 / 引用 / 询问 / 解释 / 翻译 / 总结 //btw）；AI 动作默认就地弹窗，可一键「转到主线」把回答发进当前对话。
