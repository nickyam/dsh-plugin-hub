---
title: billion-context（上下文压缩）
description: 架在编程助手与模型 API 之间的上下文压缩代理：由模型自己决定何时压缩、压缩什么，把已消耗的对话增量压缩成分层摘要且可逆、对前缀缓存友好，让小上下文窗口也能跑月级长会话；DSH 只是它支持的 20 多个客户端之一。
categories:
- workflow
tags: &id001
- 上下文压缩
- 长会话
- 省token
- 跨客户端
weight: 1010
params:
  plugin:
    id: billion-context
    name: billion-context（上下文压缩）
    aliases:
    - bili
    - 十亿上下文
    - 上下文压缩代理
    category: workflow
    status: community
    repo: https://github.com/ranxianglei/billion-context
    install: dsh plugin --profile web add billion-context
    summary: 架在编程助手与模型 API 之间的上下文压缩代理：由模型自己决定何时压缩、压缩什么，把已消耗的对话增量压缩成分层摘要且可逆、对前缀缓存友好，让小上下文窗口也能跑月级长会话；DSH 只是它支持的 20 多个客户端之一。
    features:
    - 模型驱动的分层增量压缩：压缩时机与范围由模型判断而非硬截断，摘要分层写入、可按需解压，保留前缀缓存
    - 四个上下文管理工具：compress（折叠区间为摘要）、decompress（按需还原）、search_context（在摘要与可见消息里搜关键词）、acp_status（上下文占用与可压缩区间概览）
    - 跨客户端通用：同一套 acp-kernel 支持 DSH、Claude Code、Codex、OpenCode、Kimi、Gemini、Qwen 等 20+ 编程助手，DSH 下提供 /acp 与 /acp-cache 会话内命令
    - 长会话能力：官方称 100K 小窗口即可、省 5 倍 token、单会话可跑月级；仓库附生产规模纵向研究与第三方基准报告（数字以仓库原文为准，本站未实测）
    - 安装通道：DSH 下 `dsh plugin --profile <name> add billion-context` 与 `bili plugin install dsh` 等价；也可 `bili dsh` 用启动器全量注入
    tags: *id001
    flag: 通用代理型工具，非 DSH 专属；native 插件与 standalone 扩展不可同时启用，否则会重复压缩
    notes: 仓库 ranxianglei/billion-context（master 分支），npm 包 billion-context，README 标 v0.1.208 附近（文章写 0.1.208，npm 实时版本以 registry 为准）。它不是纯 DSH 插件：架在任意编程助手与模型 API 之间重写 Anthropic/OpenAI 流，DSH 只是其支持客户端之一，本站按「可在 DSH 安装使用」收录。全局 CLI 安装为 `npm install -g billion-context --prefix=~/.local`（bili 命令落在 ~/.local/bin）；DSH 专用安装见上。native 插件（bili plugin install）与 standalone 扩展（billion-context-pi 等）互斥，同时开会双重压缩，安装器会自动切换并备份原配置到 .bili-bak。文章（wx-huxiaomo）的「省 5 倍 token / 下载 175 万」为文章与安装界面口径，本站不采信为独立结论。
    refs:
    - id: wx-huxiaomo
      title: DSH 最值得装的 7 款插件：从省 5 倍 token 到余额小鲸鱼
      url: https://mp.weixin.qq.com/s/pOxsRRqyCiFI3moxX676xQ
      kind_label: 公众号
      publisher: 狐小墨（公众号：狐小墨 AI驱动创新）
    source_count: 1
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/billion-context/
  generated: true
---

架在编程助手与模型 API 之间的上下文压缩代理：由模型自己决定何时压缩、压缩什么，把已消耗的对话增量压缩成分层摘要且可逆、对前缀缓存友好，让小上下文窗口也能跑月级长会话；DSH 只是它支持的 20 多个客户端之一。
