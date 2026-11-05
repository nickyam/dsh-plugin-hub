---
title: '@deepseek-ai/dsh-mcp-client'
description: 把外部 MCP server 的工具桥接进 DSH，工具名以 mcp__ 前缀原生出现。
categories:
- integration
tags: &id001
- MCP
- 官方
- 桥接
weight: 100
params:
  plugin:
    id: dsh-mcp-client
    name: '@deepseek-ai/dsh-mcp-client'
    category: integration
    status: official
    summary: 把外部 MCP server 的工具桥接进 DSH，工具名以 mcp__ 前缀原生出现。
    tags: *id001
    notes: 第三方教程明确：MCP 只桥接 Tools，resources 与 prompts 不支持；所有 MCP server 默认不启用，因为启动命令是沙箱外受信任的可执行代码。
    mentions:
    - source: deepseekai-works
      stance: 仅提及
      quote: 译述：@deepseek-ai/dsh-mcp-client 通过 stdio 或 streamable-http 连接 MCP server，其工具会以 mcp__github__create_issue 这类名字原生出现；只有 Tools 被桥接，resources 与 prompts 完全不支持。
      source_title: 'DSH Plugins: What They Are, Where to Find Them, and How to Write One'
      source_url: https://deepseekai.works/plugins
      source_kind_label: 教程 / 指南
      source_publisher: deepseekai.works（第三方教程站）
    source_count: 1
    has_conflict: false
    agreement: 单篇提及
    confidence: 待核实
    category_label: 集成与迁移
    status_label: 官方
    weight: 100
    url: /plugins/dsh-mcp-client/
  generated: true
---

把外部 MCP server 的工具桥接进 DSH，工具名以 mcp__ 前缀原生出现。
