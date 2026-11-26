---
title: dsh-reasoning-only-guard
description: 挡住「模型只在推理通道里答完、正文一个字没有」的那种轮次——它会在会话日志里存下一条空的 assistant 消息，而网关会以「content or tool_calls must be set」拒掉之后每一轮，整个会话从此报废。插件在落盘前补一小段文字，让这条消息永远不为空。
categories:
- security
tags: &id001
- 稳定性
- 防护
- 会话救火
weight: 1010
params:
  plugin:
    id: dsh-reasoning-only-guard
    name: dsh-reasoning-only-guard
    aliases:
    - 空回复守卫
    - reasoning guard
    - 防会话卡死
    category: security
    status: community
    repo: https://github.com/apex-mochen/dsh-reasoning-only-guard
    install: dsh plugin --profile web add github:apex-mochen/dsh-reasoning-only-guard
    summary: 挡住「模型只在推理通道里答完、正文一个字没有」的那种轮次——它会在会话日志里存下一条空的 assistant 消息，而网关会以「content or tool_calls must be set」拒掉之后每一轮，整个会话从此报废。插件在落盘前补一小段文字，让这条消息永远不为空。
    features:
    - 只补空轮：本轮既没有可见文字也没有工具调用时才注入；带内容的轮次原样透传，不删不改
    - 补什么可配：placeholder 自定义占位文字，includeFailedTurns 决定 error / aborted 的轮次要不要一并兜住，enabled 可以先关掉但留着安装
    - 位置正确：包一层 llm/stream 的 AsyncIterable，在终止 chunk finish 之前插入 block-start / text-delta / block-end，赶在累加器记录之前
    - 零依赖：lib/index.js 一百多行，没有 import、不起子进程、不读文件、不发网络请求、不设定时器
    tags: *id001
    flag: 只能预防，修不好已经写坏的会话
    notes: '是预防不是修复——已经落进 session.v3.jsonl.zstd 的空消息它管不了，那种只能手工解包改内容再打包（DSH discussion #6520 记了这个唯一的绕法）。作者自己写得很坦白：对着「按规则报错的桩」跑通了端到端，但真实 DeepSeek 网关是否也把 content: "" 当未设置拒掉，目前仍只是社区反馈。根因其实在 llm-deepseek 的 serialize.ts，DSH 目前不收外部 PR，插件只能算一个够得着的补丁位。要求 DSH 0.1.x（peer @deepseek-ai/cordis ^4.0.1）、Node 20+，装完重启 profile，验证命令 dsh --profile web --dump-config | grep reasoning-only-guard。'
    repo_confirmed: true
    gh:
      stars: 7
      forks: 0
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-09-15T08:53:33Z'
      archived: false
      slug: apex-mochen/dsh-reasoning-only-guard
      stars_label: '7'
      forks_label: '0'
      pushed_date: '2026-09-15'
      updated_label: 2 个月前有提交
      updated_days: 72
      stale: false
    entry_updated: '2026-11-19'
    category_label: 安全与治理
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-reasoning-only-guard/
  generated: true
---

挡住「模型只在推理通道里答完、正文一个字没有」的那种轮次——它会在会话日志里存下一条空的 assistant 消息，而网关会以「content or tool_calls must be set」拒掉之后每一轮，整个会话从此报废。插件在落盘前补一小段文字，让这条消息永远不为空。
