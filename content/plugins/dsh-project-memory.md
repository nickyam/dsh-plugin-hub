---
title: dsh-project-memory
description: 为 DSH agent 建一份能活过单次会话的项目记忆：自动持久化任务清单与读过的文件/文档/代码符号，会话被压缩或切换后仍可检索，并带 path:line 引用以便溯源。
categories:
- memory
tags: &id001
- 记忆
- 项目级
weight: 1010
params:
  plugin:
    id: dsh-project-memory
    name: dsh-project-memory
    category: memory
    status: community
    repo: https://github.com/00080000/dsh-project-memory
    install: dsh plugin --profile web add github:00080000/dsh-project-memory
    summary: 为 DSH agent 建一份能活过单次会话的项目记忆：自动持久化任务清单与读过的文件/文档/代码符号，会话被压缩或切换后仍可检索，并带 path:line 引用以便溯源。
    features:
    - TaskBridge：会话的 todo 列表与触及的文件持久化为每项目任务实体，工作流可切换并恢复，关联文件保持近期加权排序
    - 自动、读取时记忆化：模型读到某文件的瞬间才进索引，无人读的文件永不被扫描
    - 混合召回：对文档、符号、经验笔记与洞察做排名检索，针对中日韩查询自动开启 LLM 查询扩展
    - 文档↔代码交叉链接：提到某符号的文档在查询该符号时浮现，链接按当前符号表实时解析、不会过时
    - 分层洞察记忆：教训/决策/程序为统一实体，跨任务/项目/全局范围，近重复自动合并或强化
    tags: *id001
    notes: 无原生构建、无向量数据库；79MB 本地嵌入表（leanvec）默认安装运行，缺失时回退纯词法召回。装后需重启 dsh web。
    refs:
    - id: tree-top10
      title: 10 Best DeepSeek Harness Plugins for AI Developers in 2026
      url: https://api.treerouter.ai/en/blog/best-deepseek-harness-plugins-2026
      kind_label: 第三方媒体
      publisher: TreeRouter Blog（英文，第三方）
    source_count: 1
    repo_confirmed: true
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-project-memory/
  generated: true
---

为 DSH agent 建一份能活过单次会话的项目记忆：自动持久化任务清单与读过的文件/文档/代码符号，会话被压缩或切换后仍可检索，并带 path:line 引用以便溯源。
