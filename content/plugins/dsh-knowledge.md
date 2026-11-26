---
title: dsh-knowledge（知识库）
description: 一套能装进 DSH 的完整知识库：把文件、目录、网页和笔记导入，切块、向量化、混合检索，再让模型带着出处回答——可以零向量配置跑，也可以全本地模型跑，不需要另起一个知识库服务。
categories:
- memory
tags: &id001
- 知识库
- 混合检索
- 本地模型
weight: 1010
params:
  plugin:
    id: dsh-knowledge
    name: dsh-knowledge（知识库）
    aliases:
    - 知识库
    - RAG
    - 本地向量检索
    category: memory
    status: community
    repo: https://github.com/Soren-ABT/dsh-knowledge
    install: 先给目标 profile 的 pnpm-workspace.yaml 补 allowBuilds（esbuild / onnxruntime-node / protobufjs），再 dsh plugin --profile web add dsh-knowledge
    summary: 一套能装进 DSH 的完整知识库：把文件、目录、网页和笔记导入，切块、向量化、混合检索，再让模型带着出处回答——可以零向量配置跑，也可以全本地模型跑，不需要另起一个知识库服务。
    features:
    - 文档来源：文件、目录、网页、文本笔记；本地路径能持续重扫与重新索引
    - 混合检索：FTS5 BM25 + 向量召回 + RRF 融合 + MMR 去重，重排可选
    - 证据上下文：按文档顺序动态生成 ContextWindow，命中之后能围绕原位继续往下读，不是只给一段碎片
    - 全本地也能跑：本地 embedding、本地 rerank、本地 OCR 都支持；也能接 OpenAI 兼容接口或 Ollama
    - 文档处理：常见办公格式与扫描 PDF，PaddleOCR 优先、Tesseract 兜底，MinerU 可选
    - 管理面板：知识库分组、批量导入、预览、召回测试、模型管理、索引重建
    tags: *id001
    flag: 装之前要改 pnpm 构建白名单，否则 add 会中途退出
    notes: '安装有个前置动作最容易漏——esbuild、onnxruntime-node、protobufjs 这几个依赖要在安装期构建，pnpm 10 默认拒绝执行，dsh plugin add 会在登记 bundle 之前就退出。要先把 allowBuilds 合进该 profile 已有的 pnpm-workspace.yaml（别重复加第二个 allowBuilds: 键，YAML 会坏），再重跑一次 add，第二次会接着把 bundle 登记完。Node 要求 ^22.19.0 || >=24.0.0。默认本地 embedding 模型是 onnx-community/Qwen3-Embedding-0.6B-ONNX，约 585 MB、1024 维，跑在带版本 IPC 的独立子进程里，崩溃或超时只重建子进程、不用重启 DSH。OCR 推理也在单独子进程里，挂了只会让这份文档导入失败、不会带走 DSH。同类同名包不少（lemoncat7、XZX888、slder 等的 dsh-knowledge / dsh-knowledge-base / local-knowledge-base），认 Soren-ABT 这一份。'
    repo_confirmed: true
    gh:
      stars: 107
      forks: 14
      issues: 4
      language: TypeScript
      license: AGPL-3.0
      pushed_at: '2026-11-15T04:35:38Z'
      archived: false
      slug: Soren-ABT/dsh-knowledge
      stars_label: '107'
      forks_label: '14'
      pushed_date: '2026-11-15'
      updated_label: 11 天前有提交
      updated_days: 11
      stale: false
    entry_updated: '2026-11-19'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-knowledge/
  generated: true
---

一套能装进 DSH 的完整知识库：把文件、目录、网页和笔记导入，切块、向量化、混合检索，再让模型带着出处回答——可以零向量配置跑，也可以全本地模型跑，不需要另起一个知识库服务。
