---
title: dsh-engram
description: 纯本地 SQLite 的跨会话长期记忆：零外部服务、零 API Key、零 Docker，混合检索（FTS5 全文 + 本地向量 RRF），带证据门与全链路审计，把「记忆」做成装完即用的本地库。
categories:
- memory
tags: &id001
- 记忆
- SQLite
- 向量检索
weight: 1010
params:
  plugin:
    id: dsh-engram
    name: dsh-engram
    category: memory
    status: community
    repo: https://github.com/kenz1117/dsh-engram
    install: dsh plugin --profile web add @kenz1117/dsh-engram
    summary: 纯本地 SQLite 的跨会话长期记忆：零外部服务、零 API Key、零 Docker，混合检索（FTS5 全文 + 本地向量 RRF），带证据门与全链路审计，把「记忆」做成装完即用的本地库。
    features:
    - 纯本地 SQLite：零外部服务、零 API Key、零 Docker，一条命令装完即用
    - 23 个窄参数工具：覆盖保存/检索/事实链/时间线/审计/导出/蒸馏/信念/复习全生命周期
    - 混合检索：FTS5 全文 + 本地向量 RRF，嵌入模型离线推理，失败自动降级纯关键词并显式标记
    - 证据门与全链路审计：engram_assess 强制「充足证据齐备」才判充足；来源会话/轮次/seq 三级溯源 + 取代链 + 矛盾边
    - SM-2 间隔重复复习：只给坐标与门牌线索、先回忆后揭示；协议标签防提示注入、入库脱敏
    tags: *id001
    notes: 嵌入模型离线推理，失败时自动降级纯关键词检索并显式标记；零外部服务、零 API Key、零 Docker。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-engram/
  generated: true
---

纯本地 SQLite 的跨会话长期记忆：零外部服务、零 API Key、零 Docker，混合检索（FTS5 全文 + 本地向量 RRF），带证据门与全链路审计，把「记忆」做成装完即用的本地库。
