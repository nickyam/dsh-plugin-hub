---
title: dsh-nekowhale-stickers（大肥鱼表情包）
description: 给 DSH 一个能查的表情包知识库：322 张大肥鱼 / GPT娘 表情逐张标好场景、动作、梗和双人表情的对象方向，按情绪检索，还能在本地拼文字表情包。它解决的问题是「AI 只有一个语气」。
categories:
- fun
tags: &id001
- 表情包
- 人格化
- 桌宠
weight: 1010
params:
  plugin:
    id: dsh-nekowhale-stickers
    name: dsh-nekowhale-stickers（大肥鱼表情包）
    aliases:
    - 表情包
    - 大肥鱼
    - nekowhale
    - GPT娘
    category: fun
    status: community
    repo: https://github.com/Loping151/dsh-nekowhale-stickers
    install: dsh plugin --profile web add dsh-nekowhale-stickers
    summary: 给 DSH 一个能查的表情包知识库：322 张大肥鱼 / GPT娘 表情逐张标好场景、动作、梗和双人表情的对象方向，按情绪检索，还能在本地拼文字表情包。它解决的问题是「AI 只有一个语气」。
    features:
    - 表情知识库：逐张标注场景标签、动作描述、关联梗，双人表情记方向，不依赖模型自己看图；常驻上下文约 60 token
    - 情绪检索：按情绪与场景词打分，支持中文部分匹配，随机去重
    - 本地模板：想 / 举牌 / 葱卷 / 上联 / 下联 / 抱，六套模板自己拼文字表情包
    - 增量同步：资源更新后自动拉最新，默认懒下载
    - 自选：agent 可以自己浏览、开关，或只用挑中的一小撮；用户配的黑 / 白名单永远优先
    - 通用接口：cordis 服务 stickers、[sticker:名字] 回复标记、MCP server、CLI 与公开 JSON，不绑框架
    - 网页桌宠：右下角一只大肥鱼，跑在独立跨域 iframe 里不碰会话；双击能查 DeepSeek 余额（只用本机已登录的账号或 API Key，凭据不外发），pet / petBalance 可关
    tags: *id001
    flag: 素材是 CC BY-NC 4.0，商用要另谈
    notes: 表情作者是 B 站「可以叫我云大人/雾雪」（kiriyuki.com），代码 Apache-2.0、素材 CC BY-NC 4.0——非商用可以，商用得另谈授权。322 张是仓库徽章上的数，会随资源更新变。它同时提供 MCP server 形态，所以不用 DSH 也能接到别的地方。dsh 0.2 也可以在网页侧栏「插件 → 添加插件」里填包名安装。
    repo_confirmed: true
    gh:
      stars: 202
      forks: 3
      issues: 0
      language: TypeScript
      license: Apache-2.0
      pushed_at: '2026-11-08T14:55:26Z'
      archived: false
      slug: Loping151/dsh-nekowhale-stickers
      stars_label: '202'
      forks_label: '3'
      pushed_date: '2026-11-08'
      updated_label: 17 天前有提交
      updated_days: 17
      stale: false
    entry_updated: '2026-11-19'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-nekowhale-stickers/
  generated: true
---

给 DSH 一个能查的表情包知识库：322 张大肥鱼 / GPT娘 表情逐张标好场景、动作、梗和双人表情的对象方向，按情绪检索，还能在本地拼文字表情包。它解决的问题是「AI 只有一个语气」。
