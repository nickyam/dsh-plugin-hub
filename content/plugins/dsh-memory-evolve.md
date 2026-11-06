---
title: dsh-memory-evolve
description: 给 DSH 补上跨会话长期记忆与后台自我进化：五轨分层记忆、四轨待办、内部会话团队、外部 AI 派单与记忆同步，多数能力默认关闭、按需开启。
categories:
- memory
tags: &id001
- 记忆
- 跨会话
weight: 1010
params:
  plugin:
    id: dsh-memory-evolve
    name: dsh-memory-evolve
    category: memory
    status: community
    repo: https://github.com/csyangwen/dsh-memory-evolve
    install: dsh plugin --profile web add github:csyangwen/dsh-memory-evolve
    summary: 给 DSH 补上跨会话长期记忆与后台自我进化：五轨分层记忆、四轨待办、内部会话团队、外部 AI 派单与记忆同步，多数能力默认关闭、按需开启。
    features:
    - 五轨记忆：用户档案、全局事实、项目关键记忆、项目日志与每日日志分层存放，每回合自动记录，重要结论可按 git 分支生效
    - 四轨待办与本地搜索：生活/工作/项目/每日待办按工作目录隔离，支持优先级、截止日期与本地文档检索
    - 内部会话团队：一句话拉起设计/前端/后端/QA 子会话并放进共享房间，消息互通、状态变更推送
    - 外部 AI 派单：把视觉重做、代码评审等重活异步派给 Kimi / Codex / Grok / Hermes，先拿任务 id 不阻塞当前会话
    - 记忆同步：用代码仓库的专用分支作为记忆远端，多机自动识别同一项目，冲突可选本地/远端/两者
    tags: *id001
    notes: 社区同名实现不止一个（另有 piaobo123/dsh-memory-evolve 等），本条目以 csyangwen 版为准；装后需在设置里按需开启各项能力。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: true
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-memory-evolve/
  generated: true
---

给 DSH 补上跨会话长期记忆与后台自我进化：五轨分层记忆、四轨待办、内部会话团队、外部 AI 派单与记忆同步，多数能力默认关闭、按需开启。
