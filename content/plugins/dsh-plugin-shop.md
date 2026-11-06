---
title: dsh-plugin-shop
description: DeepSeek Harness 的插件商店：在 DSH 内提供浏览、安装、启用、禁用与更新插件的市场 UI，每次目录变更都提交进 Git 可追溯。
categories:
- market
tags: &id001
- 市场
- 人工审核
- 可追溯
weight: 1010
params:
  plugin:
    id: dsh-plugin-shop
    name: dsh-plugin-shop
    category: market
    status: community
    repo: https://github.com/LivXue/dsh-plugin-shop
    install: dsh plugin --profile web add dsh-plugin-shop@0.9.2
    summary: DeepSeek Harness 的插件商店：在 DSH 内提供浏览、安装、启用、禁用与更新插件的市场 UI，每次目录变更都提交进 Git 可追溯。
    features:
    - 自动发现：每日收集带 dsh-plugin 或 deepseek-harness 关键字的 npm 包与 GitHub 仓库
    - 严格筛选：每次构建自动检查候选，被拒插件按 17 种预定义原因记录名称并给出排查详情
    - 本地依赖检查：按当前 profile 与 web 客户端提供的模块检查 peer dependency 与版本/配置兼容性
    - 每日更新：目录每日重建并提交 Git，新插件次晨上架、失效仓库同步移除
    - 可报告的失败：安装失败时提供预填的 GitHub issue，含操作、主机错误与末 20 行日志
    tags: *id001
    flag: 与 dsh-market、dsh-plugin-radar 同类不同实现，本站不合并
    notes: README 标注当前版本 0.9.2，安装命令钉该版本；若用 npx 前置则写作 npx -y @deepseek-ai/dsh plugin --profile web add dsh-plugin-shop@0.9.2。安装后需重启 dsh 以加载插件。
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
    url: /plugins/dsh-plugin-shop/
  generated: true
---

DeepSeek Harness 的插件商店：在 DSH 内提供浏览、安装、启用、禁用与更新插件的市场 UI，每次目录变更都提交进 Git 可追溯。
