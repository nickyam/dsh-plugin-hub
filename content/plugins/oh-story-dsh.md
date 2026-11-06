---
title: oh-story-dsh
description: oh-story-dsh 是 DeepSeek Harness（DSH）的社区插件，把小说、短剧、互动游戏与视频解说四大创作工作台打包集成进 DSH Web，为本地作品目录提供专业的故事创作、改编与生产工具（与 DeepSeek 无隶属关系）。
categories:
- content
tags: &id001
- 小说
- 短剧
- 游戏脚本
- 视频解说
- 工作流
weight: 1010
params:
  plugin:
    id: oh-story-dsh
    name: oh-story-dsh
    category: content
    status: community
    repo: https://github.com/zenstory-ai/oh-story-dsh
    install: 'npx -y --package pnpm@11.7.0 --package @deepseek-ai/dsh@0.2.1-rc.5 dsh plugin --profile web add @oh-story/dsh@0.1.23 &&

      npx -y @deepseek-ai/dsh@0.2.1-rc.5 web

      '
    summary: oh-story-dsh 是 DeepSeek Harness（DSH）的社区插件，把小说、短剧、互动游戏与视频解说四大创作工作台打包集成进 DSH Web，为本地作品目录提供专业的故事创作、改编与生产工具（与 DeepSeek 无隶属关系）。
    features:
    - 四大创作工作台：DSH Web 新增小说、短剧、游戏、视频解说工作台，各配固定版本上游 Skills
    - 文件即创作事实：工作台只投影项目文件、不写并行库，人工未保存内容不被并发 Agent 覆盖
    - 媒体生产先确认：生图 / 生视频 / 配音 / 生音乐先在 Chat 展示预检，用户确认后才调用供应商 API
    - 不占其他场景：仅当 workspace 真有创作项目时接管布局，可收起并记住选择
    - 纯 DSH 原生扩展：Agent / 会话 / 模型 / 权限审批 / Chat 仍是 DSH 原生，插件只加 Skills、Roles 与工作流
    tags: *id001
    notes: README 示例安装固定 @oh-story/dsh@0.1.23 与 dsh@0.2.1-rc.5；社区插件，与 DeepSeek 无隶属关系。
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
    url: /plugins/oh-story-dsh/
  generated: true
---

oh-story-dsh 是 DeepSeek Harness（DSH）的社区插件，把小说、短剧、互动游戏与视频解说四大创作工作台打包集成进 DSH Web，为本地作品目录提供专业的故事创作、改编与生产工具（与 DeepSeek 无隶属关系）。
