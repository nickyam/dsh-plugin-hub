---
title: dsh-at-file
description: 给 DSH Web 界面加 Codex 风格 @文件 引用：输入框打 @ 搜工作区文件 / 目录，插入工作区相对路径引用而不粘贴全文内容。
categories:
- tool
tags: &id001
- '@文件'
- 指令
weight: 1010
params:
  plugin:
    id: dsh-at-file
    name: dsh-at-file
    category: tool
    status: community
    repo: https://github.com/omdsh-dev/dsh-at-file
    install: dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.7.0.tar.gz
    summary: 给 DSH Web 界面加 Codex 风格 @文件 引用：输入框打 @ 搜工作区文件 / 目录，插入工作区相对路径引用而不粘贴全文内容。
    features:
    - 输入框打 @ 打开工作区路径选择器，模糊搜索并插入文件 / 目录引用
    - 只插入路径引用标记，不打开文件、不读取内容（由 Agent 自身工具按需读取）
    - 支持文件名 / 正则过滤器，分全局与工作区两级
    - 可配置 maxIndexedFiles 索引上限与 ignoreDirs 忽略目录
    tags: *id001
    notes: README 提醒：官方 DSH 新版已内置 @file / @session 引用，新装建议优先用官方实现；本插件保留给已有环境，偶发维护。安装后重启 dsh web 使 Host 与客户端加载新版本。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: true
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-at-file/
  generated: true
---

给 DSH Web 界面加 Codex 风格 @文件 引用：输入框打 @ 搜工作区文件 / 目录，插入工作区相对路径引用而不粘贴全文内容。
