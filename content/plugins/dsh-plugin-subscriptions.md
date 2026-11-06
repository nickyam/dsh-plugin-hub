---
title: dsh-plugin-subscriptions
description: 把已有的 ChatGPT (Codex)、Claude、Grok (X Premium)、GitHub Copilot、Google Antigravity 订阅通过 OAuth 接进 DSH，复用同一批模型，无需申请或填写 API Key。
categories:
- model
tags: &id001
- 订阅复用
- OAuth
- 免Key
weight: 1010
params:
  plugin:
    id: dsh-plugin-subscriptions
    name: dsh-plugin-subscriptions
    category: model
    status: community
    repo: https://github.com/V1ki/dsh-plugin-subscriptions
    install: dsh plugin --profile web add dsh-plugin-subscriptions
    summary: 把已有的 ChatGPT (Codex)、Claude、Grok (X Premium)、GitHub Copilot、Google Antigravity 订阅通过 OAuth 接进 DSH，复用同一批模型，无需申请或填写 API Key。
    features:
    - 多订阅商无缝接入：五大订阅源经 OAuth / 设备流登录，自动刷新令牌，登录后才出现在模型选择器
    - 多账户与模型池智能路由：同提供商 ≥2 账户时展示模型并集，按配额消耗与重置时间做粘性路由与故障转移
    - 原生工具集成：随提供商启用 web_search、x_search、image_generate、video_generate 等，结果在对话内联渲染
    - 用量监控与精细模型管理：设置页可编辑模型可见性、上下文窗口、默认推理力度与独立工具开关
    - 凭证安全：Token 存于 ~/.dsh/plugins/subscriptions/auth.json（权限 0600）并自动刷新
    tags: *id001
    flag: 第三方接入，使用前先看清各服务条款
    notes: 从 GitHub 源码安装写作 dsh plugin --profile web add github:V1ki/dsh-plugin-subscriptions。Claude 若本地有 Claude Code 会话可直接导入凭证，否则走浏览器 OAuth。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 免费模型与接入
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-plugin-subscriptions/
  generated: true
---

把已有的 ChatGPT (Codex)、Claude、Grok (X Premium)、GitHub Copilot、Google Antigravity 订阅通过 OAuth 接进 DSH，复用同一批模型，无需申请或填写 API Key。
