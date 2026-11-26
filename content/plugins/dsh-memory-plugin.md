---
title: dsh-memory-plugin（OpenViking 记忆）
description: 火山引擎 OpenViking 官方出的 DSH 接入包：每轮按你自己说的话自动召回记忆与画像，会话过程自动采集、到阈值自动提交，并把 OpenViking 服务端的 MCP 工具与 skills 挂进 DSH；前提是有一个连得通的 OpenViking 服务。
categories:
- memory
tags: &id001
- OpenViking
- 长期记忆
- 自动召回
- MCP
weight: 1010
params:
  plugin:
    id: dsh-memory-plugin
    name: dsh-memory-plugin（OpenViking 记忆）
    aliases:
    - OpenViking Memory
    - '@openviking/dsh-memory-plugin'
    - 跨会话长期记忆
    category: memory
    status: community
    repo: https://github.com/volcengine/OpenViking
    install: dsh plugin --profile web add @openviking/dsh-memory-plugin
    summary: 火山引擎 OpenViking 官方出的 DSH 接入包：每轮按你自己说的话自动召回记忆与画像，会话过程自动采集、到阈值自动提交，并把 OpenViking 服务端的 MCP 工具与 skills 挂进 DSH；前提是有一个连得通的 OpenViking 服务。
    features:
    - 自动召回：每轮 pre-step 只用「用户自己写的话」检索，注入画像、可用记忆索引与技能目录；DSH 注入的时间/插件通知与工具结果不参与查询，纯注入批次不发请求
    - 自动采集与提交：session/event 采集用户、助手与可选工具结果，turn/end 按 pending token 阈值提交；写失败进共享 pending 队列，后台每 60s 探活重放，不用重启 dsh
    - 工具面全量桥接：服务端 MCP 工具挂成 mcp__openviking__*（search / read / list / tree / grep / glob / remember / write / edit / forget / add_resource / add_skill / rule_search / session_history 等），服务端升级就多工具，不用等插件发版
    - 内置 skills：openviking-memory、openviking-skills、ov-experience-memory、openviking-rule-search、ov-memory-doctor
    - viking:// 守卫：文件类工具（read/glob/grep/edit/write/str_replace_editor）拿 viking:// URI 会被拦下并指向 mcp__openviking__*；skill 目录下的写操作指向 add_skill
    - 工作区身份：默认按会话工作区的 git origin 推导 peer，一个仓库跨子目录、worktree、克隆、机器共用一份记忆；recallPeerScope=all 时跨工作区召回
    - 压缩与恢复：压缩完成后补一条 <openviking-context> 提示，给出会话 id 与用 session_history 找回细节的方法
    - 诊断：scripts/ov-memory-doctor.mjs 一次查安装、凭据配置与服务连通性（--json / --offline / --timeout / --no-color）
    tags: *id001
    flag: 由火山引擎 OpenViking 项目发布（非 DeepSeek 官方）；没配好 OpenViking 服务端等于装了不能用，README 要求服务端支持 viking://~ 家目录别名
    notes: npm 包是 scoped 的 @openviking/dsh-memory-plugin（0.5.42，Apache-2.0；仓库 volcengine/OpenViking 整体 AGPL-3.0）。npm 上另有同名裸包 dsh-memory-plugin（Culeot/dsh-memory，MIT，走 ctx.storage 的本地记忆域），跟本包不是一个东西，装错就完全不是这个功能。凭据解析顺序 OPENVIKING_* 环境变量 → ~/.openviking/ovcli.conf → ~/.openviking/ov.conf；桌面版从插件页装时不会问凭据，要先自己写好 ovcli.conf。peerDependencies 是 @deepseek-ai/dsh-llm / dsh-mcp-client / dsh-skill-filesystem（>=0.1.0-rc.6 <1.0.0-0），Node ^22.19.0 || >=24（DSH 0.2.1-rc.2+ 实际要 Node >=24.9）。mcpEnabled=false 只关 MCP 工具与 skills，召回/采集/提交照旧；skipSubagentSessions 默认 false；forget 是永久删除。本站另有 dsh-openviking（Rxiain/dsh-openviking，社区侧对接层），两者不是同一项目。内容依据官方 README 与 npm 元数据整理。
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-26'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-memory-plugin/
  generated: true
---

火山引擎 OpenViking 官方出的 DSH 接入包：每轮按你自己说的话自动召回记忆与画像，会话过程自动采集、到阈值自动提交，并把 OpenViking 服务端的 MCP 工具与 skills 挂进 DSH；前提是有一个连得通的 OpenViking 服务。
