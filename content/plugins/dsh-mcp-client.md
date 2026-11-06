---
title: '@deepseek-ai/dsh-mcp-client'
description: 官方 MCP 客户端桥接插件：连接外部 Model Context Protocol 服务器，把它们的工具注册到 ctx.tools，供模型像原生工具一样调用（工具名形如 mcp__github__create_issue）。支持 stdio 与 streamable-http 两种传输，自带断线自动重连。
categories:
- integration
tags: &id001
- MCP
- 官方
- 桥接
- 集成
weight: 1010
params:
  plugin:
    id: dsh-mcp-client
    name: '@deepseek-ai/dsh-mcp-client'
    category: integration
    status: official
    repo: https://github.com/deepseek-ai/deepseek-harness
    install: 在 cordis.yml 里为该插件加一条配置（每服务器一条），无独立 dsh plugin add 命令
    summary: 官方 MCP 客户端桥接插件：连接外部 Model Context Protocol 服务器，把它们的工具注册到 ctx.tools，供模型像原生工具一样调用（工具名形如 mcp__github__create_issue）。支持 stdio 与 streamable-http 两种传输，自带断线自动重连。
    features:
    - 把外部 MCP server 的 Tools 桥接为原生工具（mcp__ 前缀命名，与 Claude Code / Codex 同形）
    - 传输方式：stdio（本地程序）/ streamable-http（远端服务）
    - 断线自动重连、工具名稳定（重连/重载不更名）、按服务器隔离命名空间
    - 默认不启用任何服务器；每服务器一条配置，工具随 harness 启动出现
    tags: *id001
    flag: 官方包，只桥接 Tools（resources / prompts 不支持）
    notes: 源码位于官方 deepseek-harness 单体仓的 packages/mcp/mcp-client；所有 MCP server 默认不启用，且启动命令是沙箱外的可执行代码，请只接可信服务器。MCP resources 与 prompts 当前不被桥接。
    refs:
    - id: deepseekai-works
      title: 'DSH Plugins: What They Are, Where to Find Them, and How to Write One'
      url: https://deepseekai.works/plugins
      kind_label: 教程 / 指南
      publisher: deepseekai.works（第三方教程站）
    source_count: 1
    repo_confirmed: true
    category_label: 集成与迁移
    status_label: 官方
    weight: 1010
    url: /plugins/dsh-mcp-client/
  generated: true
---

官方 MCP 客户端桥接插件：连接外部 Model Context Protocol 服务器，把它们的工具注册到 ctx.tools，供模型像原生工具一样调用（工具名形如 mcp__github__create_issue）。支持 stdio 与 streamable-http 两种传输，自带断线自动重连。
