---
title: deepseek-design
description: DSH 的可编辑设计系统插件：AI 生成、可视化编辑、模板市场与 PPT 制作一体化，并提供视频能力，适合在 DSH 里直接出设计稿和演示文稿。
categories:
- visual
tags: &id001
- 设计稿
- PPT
- 模板
- 视频
weight: 1010
params:
  plugin:
    id: deepseek-design
    name: deepseek-design
    category: visual
    status: community
    repo: https://github.com/Devin-AXIS/deepseek-design
    install: npx @deepseek-ai/dsh plugin --profile web add deepseek-idesign deepseek-ippt deepseek-ivideo
    summary: DSH 的可编辑设计系统插件：AI 生成、可视化编辑、模板市场与 PPT 制作一体化，并提供视频能力，适合在 DSH 里直接出设计稿和演示文稿。
    features:
    - 可编辑设计系统：AI 生成设计稿并可视化编辑，模板市场一站式取用（deepseek-idesign）
    - PPT 工作室：演示文稿制作能力，直接产出可编辑幻灯片（deepseek-ippt）
    - 视频能力：视频生成 / 编辑（deepseek-ivideo）随仓提供
    - 原生 DSH 集成：以 deepseek-idesign / deepseek-ippt / deepseek-ivideo 三个包发布，dsh plugin 安装
    - （README 未列更多细节；以仓库说明为准）
    tags: *id001
    notes: 实际以 deepseek-idesign、deepseek-ippt、deepseek-ivideo 三个包同时安装；若已装 dsh 命令，可将 npx @deepseek-ai/dsh 替换为 dsh。Web 界面默认 http://127.0.0.1:3080。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/deepseek-design/
  generated: true
---

DSH 的可编辑设计系统插件：AI 生成、可视化编辑、模板市场与 PPT 制作一体化，并提供视频能力，适合在 DSH 里直接出设计稿和演示文稿。
