---
title: dsh-imagegen（VisioWork 生图）
description: DSH Web GUI 的生图工作台：文生图 / 图生图、提示词反推、无限画布与画廊，可自行添加生图渠道与模型（gpt-image-2、Grok Imagine、Nano Banana、Seedream 等 OpenAI 兼容端点），并支持电商套图与对话内生图。
categories:
- visual
tags: &id001
- 生图
- 文生图
- 图生图
- 无限画布
weight: 1010
params:
  plugin:
    id: dsh-imagegen
    name: dsh-imagegen（VisioWork 生图）
    aliases:
    - VisioWork
    - 生图工作台
    - VisioWork 生图
    category: visual
    status: community
    repo: https://github.com/dickpy/dsh-imagegen
    install: dsh plugin --profile web add @dickpy/dsh-imagegen
    summary: DSH Web GUI 的生图工作台：文生图 / 图生图、提示词反推、无限画布与画廊，可自行添加生图渠道与模型（gpt-image-2、Grok Imagine、Nano Banana、Seedream 等 OpenAI 兼容端点），并支持电商套图与对话内生图。
    features:
    - 文生图 / 图生图：配置生图提供方、API 地址与密钥、检测并选择模型，生成 / 编辑 / 比较图片
    - 提示词反推：上传或选一张图，反推出可直接生图的提示词，一键填回生图框
    - 无限画布：把提示词、参考图与生成节点连成可迭代创作流程，从历史或画廊加入素材继续生成
    - 电商套图与海报编辑：从商品参考图生成主图 / 卖点图 / 场景图，画布内叠加可编辑文字、Logo 与价格
    - 画廊与历史：管理创作结果、模板与标签，跨设备接续创作；对话中也能调用生图并把结果带回会话
    tags: *id001
    flag: 文章称 VisioWork、包名 dsh-imagegen；npm 包 @dickpy/dsh-imagegen，与已收录的 dsh-image-gen（shanliuling，对话生图）是不同插件
    notes: 官方仓库 github.com/dickpy/dsh-imagegen（npm 包 @dickpy/dsh-imagegen，Apache-2.0）。文章称「VisioWork」、只给包名 dsh-imagegen 与「文生图 / 图生图 + 选图生提示词 + 自行添加生图渠道和模型」的描述；GitHub 搜不到 VisioWork 同名仓库，按包名 dsh-imagegen 与功能（提示词反推 + 可配渠道模型）对应到 dickpy/dsh-imagegen，据此收录。注意区分：站内已有 dsh-image-gen（shanliuling/dsh-image-gen，别名「生图插件 / 图像创作」）仓库与功能均不同，系另一插件，未合并；say007go/dsh-imagegen 同样是 OpenAI 风格生图插件但没有无限画布与提示词反推描述，文章所述「选图生提示词 + 画布」更贴合 dickpy 版，故取此仓库。安装需 Node.js 20+，装后重启 dsh web，到「设置 → 生图配置」添加提供方与密钥；生图 API 费用自付。
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-21'
    category_label: 视觉与设计
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-imagegen/
  generated: true
---

DSH Web GUI 的生图工作台：文生图 / 图生图、提示词反推、无限画布与画廊，可自行添加生图渠道与模型（gpt-image-2、Grok Imagine、Nano Banana、Seedream 等 OpenAI 兼容端点），并支持电商套图与对话内生图。
