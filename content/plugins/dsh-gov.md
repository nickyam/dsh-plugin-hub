---
title: dsh-gov
description: Agent 治理套件（企业配套）：基于策略的工具门控（允许/拒绝/询问）、只追加的结构化 JSONL 审计日志，以及按 agent 的 token 配额与周期预算，状态持久化在 $DSH_HOME/gov/。
categories:
- security
tags: &id001
- 权限
- 治理
weight: 1010
params:
  plugin:
    id: dsh-gov
    name: dsh-gov
    category: security
    status: community
    repo: https://github.com/863683348/dsh-gov
    install: dsh plugin --profile web add dsh-gov
    summary: Agent 治理套件（企业配套）：基于策略的工具门控（允许/拒绝/询问）、只追加的结构化 JSONL 审计日志，以及按 agent 的 token 配额与周期预算，状态持久化在 $DSH_HOME/gov/。
    features:
    - 策略门禁：按工具/agent/工作区配置 allow / deny / ask 规则，支持通配符与优先级，平局 fail-closed（deny > ask > allow）
    - 结构化审计日志：每次工具调用的决定与结果写入只追加的 JSONL（audit.jsonl），可查询可导出，刻意不记参数
    - 按 agent 的 token 配额：日/周/月/总周期预算，超限向上下文注入警告，可一键重置
    - 单一 gov 工具：status / policy_* / audit_* / quota_* 一整套动作，跨工作区全局一致
    - fail-safe 设计：计量或持久化失败绝不阻塞 agent，纯逻辑分层、零依赖、可单测
    tags: *id001
    notes: 默认 posture 为 allow（与 DSH 一致）；审计日志只记工具名/agent/工作区/决定/理由/结果，不含参数内容。计量或持久化失败不阻塞 agent。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 安全与治理
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-gov/
  generated: true
---

Agent 治理套件（企业配套）：基于策略的工具门控（允许/拒绝/询问）、只追加的结构化 JSONL 审计日志，以及按 agent 的 token 配额与周期预算，状态持久化在 $DSH_HOME/gov/。
