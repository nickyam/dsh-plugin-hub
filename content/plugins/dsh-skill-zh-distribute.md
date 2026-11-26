---
title: dsh-skill-zh-distribute（中文多平台分发）
description: 零代码 DSH skill：把一份「母本」内容改写成掘金、公众号、X、小红书、B站五个平台各自的原生格式，并给出错开发布的防垃圾时间表；诚实说明多数中文平台没有免费发文 API，实际模式是 AI 生成各平台文案、人工五分钟粘贴。
categories:
- content
tags: &id001
- 分发
- 多平台
- skill
- 内容创作
weight: 1010
params:
  plugin:
    id: dsh-skill-zh-distribute
    name: dsh-skill-zh-distribute（中文多平台分发）
    aliases:
    - zh-distribute
    - 一稿多发
    - 多平台分发 skill
    category: content
    status: community
    repo: https://github.com/zjukop/dsh-skill-zh-distribute
    install: npm i -g dsh-skill-zh-distribute && dsh-skill-zh-distribute
    summary: 零代码 DSH skill：把一份「母本」内容改写成掘金、公众号、X、小红书、B站五个平台各自的原生格式，并给出错开发布的防垃圾时间表；诚实说明多数中文平台没有免费发文 API，实际模式是 AI 生成各平台文案、人工五分钟粘贴。
    features:
    - 一稿五平台：母本 → 掘金 / 公众号 / X / 小红书 / B站各自的头部博主格式文案
    - 各平台档案：受众、格式、长度、语气、标签、CTA、坑位逐平台给出
    - 防垃圾时间表：错开发布时间并给出理由
    - 诚实边界：不代发、不绕反垃圾，多数平台无免费写 API，产出 daily-pack 供人工粘贴
    tags: *id001
    flag: 社区 skill（非 Cordis bundle）；走 skill 文件系统 provider 加载，不是 dsh plugin add；npm 全局安装后用附带链接器装到 ~/.dsh/skills/zh-distribute
    notes: 仓库 zjukop/dsh-skill-zh-distribute（GitHub 精确命中唯一），npm 已发布 dsh-skill-zh-distribute（registry 200）。README 明确这是零代码 skill 而非代码插件，dsh plugin add 装的是 bundle、不适用；正确装法 npm i -g 后运行 dsh-skill-zh-distribute 链接器。文章把它列为创作组「一稿多发」，本站按其 skill 属性在 install 与 flag 里写清。
    repo_confirmed: true
    gh:
      stars: 0
      forks: 0
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-10-04T07:12:55Z'
      archived: false
      slug: zjukop/dsh-skill-zh-distribute
      stars_label: '0'
      forks_label: '0'
      pushed_date: '2026-10-04'
      updated_label: 1 个月前有提交
      updated_days: 53
      stale: false
    entry_updated: '2026-11-17'
    category_label: 内容创作与办公
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-skill-zh-distribute/
  generated: true
lastmod: '2026-11-17'
---

零代码 DSH skill：把一份「母本」内容改写成掘金、公众号、X、小红书、B站五个平台各自的原生格式，并给出错开发布的防垃圾时间表；诚实说明多数中文平台没有免费发文 API，实际模式是 AI 生成各平台文案、人工五分钟粘贴。
