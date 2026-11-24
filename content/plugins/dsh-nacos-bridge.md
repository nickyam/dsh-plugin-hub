---
title: dsh-nacos-bridge（Nacos 接口桥）
description: 一个很薄的桥接插件：从 Nacos 3.2+ AI 注册中心读取已登记的 MCP 服务器与 A2A Agent Card，挂载成 DSH 里能直接调用的工具；新能力只要注册到 Nacos，无需改代码。
categories:
- integration
tags: &id001
- Nacos
- MCP
- A2A
- 接口桥
weight: 1010
params:
  plugin:
    id: dsh-nacos-bridge
    name: dsh-nacos-bridge（Nacos 接口桥）
    aliases:
    - Nacos 接口桥
    - dsh-nacos-bridge-plugin
    - 外部接口桥
    category: integration
    status: community
    repo: https://github.com/MalcolmFeng/dsh-nacos-bridge-plugin
    install: dsh plugin --profile web add dsh-nacos-bridge-plugin
    summary: 一个很薄的桥接插件：从 Nacos 3.2+ AI 注册中心读取已登记的 MCP 服务器与 A2A Agent Card，挂载成 DSH 里能直接调用的工具；新能力只要注册到 Nacos，无需改代码。
    features:
    - 发现并挂载：从 Nacos AI Registry 读 MCP server → mcp__<name>__* 工具，读 A2A Agent Card → a2a__<name>__chat 多轮能力
    - 刻意做薄：约 540 行的胶水层，无 UI、无数据库、无自有业务逻辑，只「发现并重新暴露」已有能力；skill/记忆/会话/多模型交给 DSH 原生插件
    - 零代码扩展：加能力 = 在 Nacos 里注册，插件自动发现成工具
    - 自带运维台：可选 operator console（file IPC），另有 rebuild/restart/start 脚本便于开发与无人值守
    tags: *id001
    flag: 社区项目；需自建可达的 Nacos 3.2+ 实例并开启 AI Registry，且能力已在其中注册；非普通用户开箱即用
    notes: 仓库 MalcolmFeng/dsh-nacos-bridge-plugin（GitHub 搜 dsh-nacos-bridge 唯一精确命中）。README 未给一行式 dsh plugin add 命令，而是通过 pnpm 把 plugins/dsh-nacos-bridge 以 link 方式装进 profile、再用 dsh web --profile web --patch runtime/cordis.yml 启动；本站 install 按插件包名写通用形式，实际按 README 的 pnpm link 流程操作。前置：Nacos 3.2+ 开启 AI Registry，配置 DEEPSEEK_API_KEY。
    repo_confirmed: true
    gh:
      stars: 2
      forks: 0
      issues: 0
      language: TypeScript
      license: MIT
      pushed_at: '2026-09-04T07:26:04Z'
      archived: false
      slug: MalcolmFeng/dsh-nacos-bridge-plugin
      stars_label: '2'
      forks_label: '0'
      pushed_date: '2026-09-04'
      updated_label: 2 个月前有提交
      updated_days: 81
      stale: false
    entry_updated: '2026-11-17'
    category_label: 集成与迁移
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-nacos-bridge/
  generated: true
---

一个很薄的桥接插件：从 Nacos 3.2+ AI 注册中心读取已登记的 MCP 服务器与 A2A Agent Card，挂载成 DSH 里能直接调用的工具；新能力只要注册到 Nacos，无需改代码。
