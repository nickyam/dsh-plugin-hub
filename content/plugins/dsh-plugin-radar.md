---
title: dsh-plugin-radar
description: DSH 开源生态雷达：持续收集插件候选、归并兼容性记录，并发布可浏览的目录与机器可读数据，帮助使用者按兼容性筛选插件、把生态数据接入自己的工具。
categories:
- market
tags: &id001
- 雷达
- 兼容性
- 数据接口
weight: 1010
params:
  plugin:
    id: dsh-plugin-radar
    name: dsh-plugin-radar
    category: market
    status: community
    repo: https://github.com/AdamPlatin123/dsh-plugin-radar
    install: ''
    summary: DSH 开源生态雷达：持续收集插件候选、归并兼容性记录，并发布可浏览的目录与机器可读数据，帮助使用者按兼容性筛选插件、把生态数据接入自己的工具。
    features:
    - 持续发现：GitHub + npm 持续扫描候选插件，按仓库去重形成全量清单
    - 兼容性记录：聚合多轮运行级测试与社区登记，给出可用 / 不兼容 / 待定 / 未测四档判定
    - 公开数据接口：无需密钥的静态 JSON（快照指针、统计、逐条明细），供下游市场与工具接入
    - 可浏览目录与站点：按分类与监测状态渲染，默认筛选可用项
    - 社区登记：通过 GitHub 提交 PR 或给仓库加 dsh-plugin topic 补充条目与更正判定
    tags: *id001
    flag: 数据 / 目录类项目，非可安装插件
    notes: 雷达站点数据在构建期打包；公开 JSON 暂时不可用通常不影响已部署的浏览。生产运行级测试引擎未开源。项目声明为社区项目，与 DeepSeek 官方无隶属关系。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 插件市场与发现
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-plugin-radar/
  generated: true
---

DSH 开源生态雷达：持续收集插件候选、归并兼容性记录，并发布可浏览的目录与机器可读数据，帮助使用者按兼容性筛选插件、把生态数据接入自己的工具。
