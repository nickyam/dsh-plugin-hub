---
title: dsh-univer-office
description: dsh-univer-office 是 DeepSeek Harness（DSH）的 Univer 办公插件，把电子表格、文档、幻灯片、关系表与画布集成进统一运行时，让 AI 代理用自然语言创建 / 编辑 / 验证办公文件，并通过隔离工作树实现安全检查。
categories:
- content
tags: &id001
- 表格
- 文档
- 幻灯片
- 画布
weight: 1010
params:
  plugin:
    id: dsh-univer-office
    name: dsh-univer-office
    category: content
    status: community
    repo: https://github.com/dream-num/dsh-univer-office
    install: 'dsh plugin --profile web add dsh-univer-office

      dsh web

      '
    summary: dsh-univer-office 是 DeepSeek Harness（DSH）的 Univer 办公插件，把电子表格、文档、幻灯片、关系表与画布集成进统一运行时，让 AI 代理用自然语言创建 / 编辑 / 验证办公文件，并通过隔离工作树实现安全检查。
    features:
    - 分析与构建电子表格：读写 Excel、写公式、格式化与验证，生成图表 / 透视表，导出 .xlsx / .csv / .tsv
    - 撰写与排版文档：段落 / 富文本 / 列表 / 表格 / 图像 / 页眉页脚，导出 .docx
    - 创建与修改演示文稿：按主题生成幻灯片、重设计页面、检测溢页与重叠文本，导出 .pptx
    - 隔离草稿机制：每次写入起自隔离 draft，用户可实时观看并在对话中批准 / 丢弃，不直接覆盖当前版本
    - 多内容合一：一个 .univer 文件可同时含 Sheets / Docs / Slides / Bases / Boards，公式与嵌入可互相引用
    tags: *id001
    notes: Dream Num 出品的 Univer 办公套件 DSH 插件；支持 Sheets / Docs / Slides / Bases / Boards 统一于 .univer 文件。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 内容创作与办公
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-univer-office/
  generated: true
---

dsh-univer-office 是 DeepSeek Harness（DSH）的 Univer 办公插件，把电子表格、文档、幻灯片、关系表与画布集成进统一运行时，让 AI 代理用自然语言创建 / 编辑 / 验证办公文件，并通过隔离工作树实现安全检查。
