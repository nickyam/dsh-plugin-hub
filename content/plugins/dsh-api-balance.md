---
title: dsh-api-balance
description: 轻量的 DeepSeek 原生 API 余额与用量插件：在输入框下方常驻余额胶囊，提供详情弹窗、/balance 命令与 api_balance 工具，只依赖 DeepSeek 官方余额接口。
categories:
- billing
tags: &id001
- 余额
- 轻量
weight: 1010
params:
  plugin:
    id: dsh-api-balance
    name: dsh-api-balance
    category: billing
    status: community
    repo: https://github.com/Muzi1015/dsh-api-balance
    install: dsh plugin --profile web add dsh-api-balance-plugin
    summary: 轻量的 DeepSeek 原生 API 余额与用量插件：在输入框下方常驻余额胶囊，提供详情弹窗、/balance 命令与 api_balance 工具，只依赖 DeepSeek 官方余额接口。
    features:
    - 常驻余额胶囊：输入框下方常驻显示 DeepSeek 余额，自带刷新、无需点击
    - 详情弹窗：总额、充值、赠送、更新时间与用量明细、去充值链接
    - /balance 命令与 api_balance 工具：对话里直接查余额，不消耗 token
    - 两种凭据：登录态 DeepSeek 账号（钱包余额）或纯 DEEPSEEK_API_KEY，自动选可用的
    - 主题与语言感知：跟随界面主题与语言（内置中英），刷新节奏可在配置里调整
    tags: *id001
    flag: 存在多个同名社区实现，本条目以 Muzi1015 版（npm 包 dsh-api-balance-plugin）为准
    notes: 另有 Kihara777/dsh-api-balance（仅 GitHub 源码安装、无 npm 包，作者说明因视力障碍暂未发布 npm）等同类轻量实现；本条目以 Muzi1015 版为准。
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
    url: /plugins/dsh-api-balance/
  generated: true
---

轻量的 DeepSeek 原生 API 余额与用量插件：在输入框下方常驻余额胶囊，提供详情弹窗、/balance 命令与 api_balance 工具，只依赖 DeepSeek 官方余额接口。
