---
title: dsh-deep-research（自适应深度研究）
description: 基于 DSH 官方 workflow 引擎的深度研究插件，按控制论 + 信息论设计成自适应研究闭环：先定义答案空间与验收标准，再并行研究子问题、按缺口自动派发下一轮、边际增益为零即停，不是固定的提示词流水线。
categories:
- workflow
tags: &id001
- 深度研究
- workflow
- 控制论
- 信息论
weight: 1010
params:
  plugin:
    id: dsh-deep-research
    name: dsh-deep-research（自适应深度研究）
    aliases:
    - '@dsh-external/dsh-deep-research'
    - 深度研究插件
    category: workflow
    status: community
    repo: https://github.com/omdsh-dev/dsh-deep-research
    install: dsh plugin --profile web add git+https://github.com/dsh-external/dsh-deep-research.git
    summary: 基于 DSH 官方 workflow 引擎的深度研究插件，按控制论 + 信息论设计成自适应研究闭环：先定义答案空间与验收标准，再并行研究子问题、按缺口自动派发下一轮、边际增益为零即停，不是固定的提示词流水线。
    features:
    - 答案空间与验收标准：规划代理先定义 scope 与每个子问题的 acceptance，避免闭环校准错误目标
    - 覆盖度自检：按必要多样性定律枚举信息维度，输出 coverage_gaps
    - 三态证据：confirmed / uncertain / gaps 保留置信度与矛盾，不掩盖不确定性
    - 边际增益验证：预测 → 行动（web_search/web_fetch）→ 更新证据 → 零增益即停 + 轮次硬上限
    - 闭环再规划：每轮收集高优缺口自动派发补充研究，对盲区定向侦察
    tags: *id001
    flag: 社区项目；npm 未发布（@dsh-external/dsh-deep-research 查不到），须从 git 安装；研究能力依赖 web_search/web_fetch 工具
    notes: 官方组织仓 dsh-external/dsh-deep-research（GitHub 搜索首位的 omdsh-dev/dsh-deep-research 是镜像，README 相同；README 内 git 安装地址明确写 github.com/dsh-external/dsh-deep-research），npm registry 上 @dsh-external/dsh-deep-research 返回 404，故 install 用 README 的 git+https 形式。README 声明包带 dsh.bundle.patch（cordis.patch.yml），可装进任意 profile。
    repo_confirmed: true
    gh:
      stars: 32
      forks: 9
      issues: 10
      language: TypeScript
      license: MIT
      pushed_at: '2026-08-12T07:12:36Z'
      archived: false
      slug: omdsh-dev/dsh-deep-research
      stars_label: '32'
      forks_label: '9'
      pushed_date: '2026-08-12'
      updated_label: 3 个月前有提交
      updated_days: 106
      stale: false
    entry_updated: '2026-11-19'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-deep-research/
  generated: true
---

基于 DSH 官方 workflow 引擎的深度研究插件，按控制论 + 信息论设计成自适应研究闭环：先定义答案空间与验收标准，再并行研究子问题、按缺口自动派发下一轮、边际增益为零即停，不是固定的提示词流水线。
