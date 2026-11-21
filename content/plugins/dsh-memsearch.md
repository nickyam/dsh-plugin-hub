---
title: dsh-memsearch（自动语义记忆）
description: 让 DSH 像 Codex / Claude Code 的 memsearch 插件一样默认自动写入与按需召回记忆：会话开始后台跑一次索引并注入状态提示，每轮结束把用户问题与最终回复追加进本地记忆日志并增量重索引；纯本地，默认不调用任何 LLM。
categories:
- memory
tags: []
weight: 1010
params:
  plugin:
    id: dsh-memsearch
    name: dsh-memsearch（自动语义记忆）
    aliases:
    - dsh-memsearch
    - MemSearch-dsh
    - 语义记忆插件
    category: memory
    status: community
    repo: https://github.com/clouwer/dsh-memsearch
    install: dsh plugin --profile web add dsh-memsearch
    summary: 让 DSH 像 Codex / Claude Code 的 memsearch 插件一样默认自动写入与按需召回记忆：会话开始后台跑一次索引并注入状态提示，每轮结束把用户问题与最终回复追加进本地记忆日志并增量重索引；纯本地，默认不调用任何 LLM。
    features:
    - 会话开始：后台 memsearch index，注入一条插件来源状态消息（版本、embedding provider、记忆目录、历史文件数 + 用 memory-recall skill 的提示）
    - 每轮结束：自动捕获用户问题与最终回复，按紧凑格式追加到 <memoryDir>/<YYYY-MM-DD>.md，去重后增量重索引
    - 检索沿用官方设计：不自动塞上下文，由 agent 按需通过 memsearch 官方 memory-recall skill 检索
    - 可配置 memoryDir、collection、injectSessionStatus、capture、captureMinPromptLength（默认 10，短问候不捕获）、maxCaptureChars（默认 8000）、summarizePlugin、indexAfterCapture
    - 记忆日志默认落 ~/.memsearch/memory/，设 MEMSEARCH_DIR 时落 $MEMSEARCH_DIR/memory/；配置需要在 cordis.patch.yml 用 insert 列表追加插件实例
    flag: npm 包名是 dsh-memsearch，文章写的 MemSearch-dsh 返回 404；跨平台记忆是 memsearch 生态能力，本插件只负责 DSH 侧的写与召回
    notes: 官方仓库 clouwer/dsh-memsearch，npm 包 dsh-memsearch；文章包名 MemSearch-dsh 在 npm 查无此包（404），按 README 用 dsh-memsearch。文中「记忆在 Claude Code、Codex、DSH、OpenClaw、OpenCode 之间自由流动、同一台机器同一项目文件夹下通用」描述的是 memsearch 本体生态，本插件 README 只声明「对齐官方 Codex/Claude Code memsearch 插件的自动写入与召回」，不承诺跨平台，卡片按 README 写。安装后还需在 cordis.patch.yml 用 insert 列表追加配置才能启用自动捕获，不是装完即生效。
    repo_confirmed: true
    gh:
      stars: 1
      forks: 0
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-08-14T06:26:58Z'
      archived: false
      slug: clouwer/dsh-memsearch
      stars_label: '1'
      forks_label: '0'
      pushed_date: '2026-08-14'
      updated_label: 3 个月前有提交
      updated_days: 99
      stale: false
    entry_updated: '2026-11-19'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-memsearch/
  generated: true
---

让 DSH 像 Codex / Claude Code 的 memsearch 插件一样默认自动写入与按需召回记忆：会话开始后台跑一次索引并注入状态提示，每轮结束把用户问题与最终回复追加进本地记忆日志并增量重索引；纯本地，默认不调用任何 LLM。
