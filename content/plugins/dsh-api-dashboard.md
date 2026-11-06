---
title: dsh-api-dashboard
description: 在 Web GUI 输入框下方实时显示各平台 API 余额与本会话/子代理的 token 消耗估算，覆盖多家国内外平台；未开放余额接口的如实显示「未开放」、不伪造数字。
categories:
- billing
tags: &id001
- 余额
- 用量
- 多家平台
weight: 1010
params:
  plugin:
    id: dsh-api-dashboard
    name: dsh-api-dashboard
    category: billing
    status: community
    repo: https://github.com/133563825as-ai/dsh-api-dashboard
    install: dsh plugin --profile web add dsh-api-dashboard
    summary: 在 Web GUI 输入框下方实时显示各平台 API 余额与本会话/子代理的 token 消耗估算，覆盖多家国内外平台；未开放余额接口的如实显示「未开放」、不伪造数字。
    features:
    - 多平台余额：DeepSeek / 智谱 GLM / Kimi / MiniMax / OpenRouter 等，未开放余额接口的如实显示「未开放」、不伪造数字
    - 本会话与子代理消耗估算：按模型单价折算，混合币种分两段显示、不做汇率合并
    - 三层 UI：输入框下方的余额状态条 → 点开看板抽屉 → 点卡片看平台详情
    - 峰谷趣味计费与三色阈值灯：可自定义阈值，余额首次跌破预警线自动推送通知
    - 可选「大肥鱼」桌宠挂件（移植自鲸鱼挂件）与一键自更新
    tags: *id001
    notes: 深度绑定 DSH 客户端与宿主 API，只能在 DSH 里运行；未开放余额接口的平台如实显示「未开放」，不伪造数字。安装或维护前建议先读仓库 AGENTS.md。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 模型与计费
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-api-dashboard/
  generated: true
---

在 Web GUI 输入框下方实时显示各平台 API 余额与本会话/子代理的 token 消耗估算，覆盖多家国内外平台；未开放余额接口的如实显示「未开放」、不伪造数字。
