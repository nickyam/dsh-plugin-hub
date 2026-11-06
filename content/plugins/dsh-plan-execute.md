---
title: dsh-plan-execute
description: 双模型路由：把规划与执行拆给不同模型，复杂任务先由推理模型规划拆解，再交给经济模型执行，从而兼顾规划质量与执行成本。
categories:
- workflow
tags: &id001
- 双模型
- 路由
- 省成本
weight: 10
params:
  plugin:
    id: dsh-plan-execute
    name: dsh-plan-execute
    category: workflow
    status: community
    repo: ''
    install: ''
    summary: 双模型路由：把规划与执行拆给不同模型，复杂任务先由推理模型规划拆解，再交给经济模型执行，从而兼顾规划质量与执行成本。
    features:
    - 规划与执行分离：复杂任务由推理模型产出方案，经济模型负责落地
    - 按需规划：执行模型先判断是否需要规划，需要时才调用规划模型
    - 降本增效：规划阶段保证思考质量，执行阶段压低 token 成本
    tags: *id001
    notes: 未找到与 ID 同名且可公开访问验证的仓库；检索命中多为名称相近的 dsh-plan-and-execute（如 Yaaaaaaa233/dsh-plan-and-execute，双模型路由/规划执行分离）以及不公开的 dsh-external/dsh-plan-execute，内容依据参考文章整理。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: false
    category_label: 协作与工作流
    status_label: 社区
    weight: 10
    url: /plugins/dsh-plan-execute/
  generated: true
---

双模型路由：把规划与执行拆给不同模型，复杂任务先由推理模型规划拆解，再交给经济模型执行，从而兼顾规划质量与执行成本。
