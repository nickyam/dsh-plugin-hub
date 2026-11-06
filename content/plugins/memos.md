---
title: MemOS
description: MemOS 是面向 LLM 与 AI Agent 的记忆操作系统，统一长期记忆的存储 / 检索 / 管理，原生支持 DeepSeek Harness 的本地与云端插件，提供自动召回、后台捕获、混合检索与本地记忆查看器。
categories:
- memory
tags: &id001
- 记忆操作系统
- 混合检索
- DSH
weight: 1010
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
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/memos/
  generated: true
---

MemOS 是面向 LLM 与 AI Agent 的记忆操作系统，统一长期记忆的存储 / 检索 / 管理，原生支持 DeepSeek Harness 的本地与云端插件，提供自动召回、后台捕获、混合检索与本地记忆查看器。
