---
title: dsh-agent-teams（社区版）
description: 把当前 DSH 会话变成队长，可组装持久化的子智能体、把目标拆成依赖感知的任务，并通过直接消息协调工作；提供团队协议、14 个协调工具、持久状态、自动共享任务调度器与实时 Web UI，无需额外工作流引擎。
categories:
- workflow
tags: &id001
- 多智能体
- 协作
weight: 1030
params:
  plugin:
    id: dsh-agent-teams
    name: dsh-agent-teams（社区版）
    category: workflow
    status: community
    repo: https://github.com/NanmiCoder/dsh-agent-teams
    install: dsh plugin --profile web add github:NanmiCoder/dsh-agent-teams
    summary: 把当前 DSH 会话变成队长，可组装持久化的子智能体、把目标拆成依赖感知的任务，并通过直接消息协调工作；提供团队协议、14 个协调工具、持久状态、自动共享任务调度器与实时 Web UI，无需额外工作流引擎。
    features:
    - 队长制委派：当前会话化身队长，组建团队、分配角色、汇总最终结果
    - 持久成员：成员是可续跑的 DSH 子智能体，可唤醒做聚焦的后续回合
    - 依赖感知的任务：任务显式流转于不同状态，依赖未完成前不会被认领
    - 直接消息：成员之间（或向队长）发持久邮箱消息，无需中继
    - 实时活动面板：Web UI 以分段进度、可折叠花名册与交互式任务 DAG 展示；规划阶段先出草稿再「Approve & Run」
    tags: *id001
    flag: 与官网内置 Agent teams 名称相近，勿混
    notes: 官网界面另有标为 Experimental 的 Agent teams，属开箱即用能力，本站不收录；这里只记需要单独安装的社区插件。需在兼容宿主（README 提供确切版本与兼容矩阵）上运行。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    - id: wx-dabaihua
      title: DeepSeek Harness 是个啥？大白话讲透 + 10 分钟上手 + 好用插件清单
      url: http://mp.weixin.qq.com/s?__biz=MzkwMDMzMzE0Mg==&mid=2247488511&idx=1&sn=b8f08d42ca17c2895080d4180cd3d6c9
      kind_label: 公众号
      publisher: 微信公众号（原文署名待补）
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 3
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-agent-teams/
  generated: true
---

把当前 DSH 会话变成队长，可组装持久化的子智能体、把目标拆成依赖感知的任务，并通过直接消息协调工作；提供团队协议、14 个协调工具、持久状态、自动共享任务调度器与实时 Web UI，无需额外工作流引擎。
