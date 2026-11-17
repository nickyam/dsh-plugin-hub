---
title: dsh-novel-craft（文风偏好小说）
description: 面向中文小说作者的写作插件：正文不进写稿上下文，你只对候选稿点赞/点踩，模型自己把偏好总结成一份可编辑的「文风档案」，下一轮带档案写稿、写完再点再总结，越用越懂你的口味。
categories:
- content
tags: &id001
- 小说
- 文风
- 偏好学习
- 创作
weight: 1010
params:
  plugin:
    id: dsh-novel-craft
    name: dsh-novel-craft（文风偏好小说）
    aliases:
    - 文风偏好插件
    - 点赞点踩写小说
    category: content
    status: community
    repo: https://github.com/shiyan688/dsh-novel-craft
    install: dsh plugin --profile web add dsh-novel-craft
    summary: 面向中文小说作者的写作插件：正文不进写稿上下文，你只对候选稿点赞/点踩，模型自己把偏好总结成一份可编辑的「文风档案」，下一轮带档案写稿、写完再点再总结，越用越懂你的口味。
    features:
    - 点赞点踩学文风：对好段落 👍、坏段落 👎，模型把点选提炼成可编辑的偏好档案（喜欢什么、避免什么）
    - 候选稿与局部改稿：支持候选稿、章节管理与局部重写
    - 正文不进上下文：靠偏好积累而非堆提示词来调文风，减少上下文占用
    tags: *id001
    flag: 社区项目（MIT）；依赖使用者持续点选来积累偏好
    notes: 仓库 shiyan688/dsh-novel-craft，npm 已发布 dsh-novel-craft（registry 200），README 给 npm 与 git 两种安装，本站 install 用 npm 稳定版；README 明确英文文档只放仓库、不进 npm 包。文章称它「只让你点赞点踩，模型自己总结你的文风」，与 README 一致。
    refs:
    - id: wx-xiaobai
      title: DeepSeek Harness 插件越装越卡？17 个真插件＋3 条变现路，按这个顺序装！
      url: https://mp.weixin.qq.com/s/2JXJhd9hmSHGfB39dCUlSQ
      kind_label: 公众号
      publisher: Stefan学AI（公众号：晓白AI纪元）
    source_count: 1
    repo_confirmed: true
    category_label: 内容创作与办公
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-novel-craft/
  generated: true
---

面向中文小说作者的写作插件：正文不进写稿上下文，你只对候选稿点赞/点踩，模型自己把偏好总结成一份可编辑的「文风档案」，下一轮带档案写稿、写完再点再总结，越用越懂你的口味。
