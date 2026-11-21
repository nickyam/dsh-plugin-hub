---
title: dsh-topic-audit（插件真伪审计）
description: 审计 GitHub 的 dsh-plugin 话题、把真插件与蹭话题的无关仓库分开的工具：按仓库根目录是否带 cordis bundle 清单、README 是否提到 DSH，判成 plugin / companion / not-a-plugin 三类，可作为 GitHub Action 每晚复跑。
categories:
- security
tags: &id001
- 安全
- 审计
- 话题
- 防投毒
weight: 1010
params:
  plugin:
    id: dsh-topic-audit
    name: dsh-topic-audit（插件真伪审计）
    aliases:
    - 话题审计
    - dsh-plugin 话题审计
    category: security
    status: community
    repo: https://github.com/ciceroyang/dsh-topic-audit
    install: dsh plugin --profile web add github:ciceroyang/dsh-topic-audit
    summary: 审计 GitHub 的 dsh-plugin 话题、把真插件与蹭话题的无关仓库分开的工具：按仓库根目录是否带 cordis bundle 清单、README 是否提到 DSH，判成 plugin / companion / not-a-plugin 三类，可作为 GitHub Action 每晚复跑。
    features:
    - 三类判定：plugin（根带 cordis.patch.yml 等清单、可 dsh plugin add）/ companion（无清单但与 DSH 相关）/ not-a-plugin
    - 应对话题冒名：话题可按 star 排序，无关仓库蹭标签就能排在真插件前面，本工具专门识别这种情况
    - 可复现：每晚从干净 --bands 运行重建资产，rolling latest 标签附可验证配方
    - 可作 composite action：夜间任务三行接入
    tags: *id001
    flag: 社区项目；npm 未发布（registry 404），按 git 安装；判定的是「是否真插件」，不是仓库质量
    notes: 仓库 ciceroyang/dsh-topic-audit（npm registry 返回 404，故 install 用 github 形式）。README 自述它更像生态审计工具（companion 类），但文章把它列为「地基」插件之一用于查真伪，本站按社区条目收录并在简介里说明它是审计工具。GitHub 有 yunhuantian/dsh-plugin-hub、863683348/dsh-plugin-audit 等近似项目，本条取名字精确命中的 ciceroyang 仓库。
    repo_confirmed: true
    gh:
      stars: 0
      forks: 0
      issues: 1
      language: JavaScript
      license: MIT
      pushed_at: '2026-09-17T12:43:52Z'
      archived: false
      slug: ciceroyang/dsh-topic-audit
      stars_label: '0'
      forks_label: '0'
      pushed_date: '2026-09-17'
      updated_label: 2 个月前有提交
      updated_days: 65
      stale: false
    entry_updated: '2026-11-17'
    category_label: 安全与治理
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-topic-audit/
  generated: true
---

审计 GitHub 的 dsh-plugin 话题、把真插件与蹭话题的无关仓库分开的工具：按仓库根目录是否带 cordis bundle 清单、README 是否提到 DSH，判成 plugin / companion / not-a-plugin 三类，可作为 GitHub Action 每晚复跑。
