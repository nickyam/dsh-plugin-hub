---
title: MemOS
description: MemOS 是面向 LLM 与 AI Agent 的记忆操作系统，统一长期记忆的存储 / 检索 / 管理，原生支持 DeepSeek Harness 的本地与云端插件，提供自动召回、后台捕获、混合检索与本地记忆查看器。
categories:
- memory
tags: &id001
- 记忆操作系统
- 混合检索
- DSH
weight: 1020
params:
  plugin:
    id: memos
    name: MemOS
    category: memory
    status: community
    repo: https://github.com/MemTensor/MemOS
    install: npx @deepseek-ai/dsh plugin --profile web add @memtensor/memos-cloud-dsh-plugin@latest
    summary: MemOS 是面向 LLM 与 AI Agent 的记忆操作系统，统一长期记忆的存储 / 检索 / 管理，原生支持 DeepSeek Harness 的本地与云端插件，提供自动召回、后台捕获、混合检索与本地记忆查看器。
    features:
    - 统一记忆 API：单一接口增删改查记忆，以图谱结构组织，可检视可编辑，非黑盒向量库
    - 多模态记忆：原生支持文本、图像、工具轨迹与人格设定，统一检索与推理
    - 多 Cube 知识库管理：将多个知识库组合为记忆立方体，支持隔离、受控共享与动态组合
    - 异步摄取（MemScheduler）：毫秒级延迟异步执行记忆操作，高并发下稳定运行
    - 记忆反馈与纠正：用自然语言反馈修正、补充或替换既有记忆
    tags: *id001
    notes: DSH 支持本地（memos-local-plugin，curl 安装脚本）与云端（@memtensor/memos-cloud-dsh-plugin）两种插件；README 另注 token 节省等数字，本站不引用具体数值。
    repo_confirmed: true
    gh:
      stars: 12444
      forks: 1129
      issues: 150
      language: TypeScript
      license: Apache-2.0
      pushed_at: '2026-11-18T12:09:12Z'
      archived: false
      slug: MemTensor/MemOS
      stars_label: 12.4k
      forks_label: '1129'
      pushed_date: '2026-11-18'
      updated_label: 6 天前有提交
      updated_days: 6
      stale: false
    entry_updated: '2026-11-06'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1020
    url: /plugins/memos/
  generated: true
---

MemOS 是面向 LLM 与 AI Agent 的记忆操作系统，统一长期记忆的存储 / 检索 / 管理，原生支持 DeepSeek Harness 的本地与云端插件，提供自动召回、后台捕获、混合检索与本地记忆查看器。
