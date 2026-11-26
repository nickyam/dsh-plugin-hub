---
title: dsh-claude-style（Claude 风格主题）
description: 为 DSH Web GUI 复刻 Claude Code Desktop 风格与交互的主题插件：Claude/DeepSeek 品牌切换、六套配色预设、亮暗跟随系统，并含消息回退与版本历史等交互增强，同时只启用一个主题。
categories:
- fun
tags: &id001
- 主题
- Claude风格
- 换肤
- 交互增强
weight: 1010
params:
  plugin:
    id: dsh-claude-style
    name: dsh-claude-style（Claude 风格主题）
    aliases:
    - Claude 风格主题
    - Claude Desktop 风格
    - dsh-claude-style
    category: fun
    status: community
    repo: https://github.com/Nwflower/dsh-claude-style
    install: dsh plugin --profile web add dsh-claude-style
    summary: 为 DSH Web GUI 复刻 Claude Code Desktop 风格与交互的主题插件：Claude/DeepSeek 品牌切换、六套配色预设、亮暗跟随系统，并含消息回退与版本历史等交互增强，同时只启用一个主题。
    features:
    - 外观：Claude/DeepSeek 品牌切换、亮暗跟随系统，Claude/DeepSeek/羊皮纸/森林/暮色/蔷薇六套配色预设，可编辑/新建/复制/重命名/删除
    - 交互增强：消息回退与版本历史，依赖 DSH 自带浏览器组件模块 @deepseek-ai/dsh-client-ui-primitives，无需额外装组件包
    - 同一时刻只启用一个主题；宿主 dsh >=0.2.2-rc.3，装好后重启 DSH
    - 安装双路：npm 包 dsh-claude-style（推荐）或 GitHub 发布分支 Nwflower/dsh-claude-style#dist
    tags: *id001
    flag: 只是外观/交互，底层模型不变、不给 Claude 账号或额度；宿主 dsh >=0.2.2-rc.3；多数 MIT，钠渲染引擎 PolyForm Shield 1.0.0、Clawd 角色帧图非 MIT
    notes: 官方仓库 github.com/Nwflower/dsh-claude-style（npm 包 dsh-claude-style，默认分支 master，npm latest 0.22.1）。文章只给包名 dsh-claude-style 与「Claude Code Desktop 风格主题 + 配色 + 消息回退 + 版本历史 + 宿主>=0.2.2-rc.3 + 建议只启一个主题」，与 README 逐条吻合，据此收录；仓库由包名检索核实，README 在 master 分支。文章特别提醒「界面像 Claude 不代表底层模型变成 Claude，也不会获得 Claude 账号或额度」，README 定位一致，作为 flag 保留。消息/文件回退的检查点范围有限（Git 提交、外部服务修改、其他命令副作用不会自动全撤销）。许可需注意：仓库多数 MIT，但钠渲染引擎为 PolyForm Shield 1.0.0、Clawd 角色帧图不在 MIT 范围内。与站内 dsh-dream-skin（LLLAAAAA，8 套 Mirage 主题+壁纸+强调色）定位不同，未合并。
    repo_confirmed: true
    gh:
      stars: 720
      forks: 92
      issues: 1
      language: TypeScript
      license: NOASSERTION
      pushed_at: '2026-11-26T16:41:58Z'
      archived: false
      slug: Nwflower/dsh-claude-style
      stars_label: '720'
      forks_label: '92'
      pushed_date: '2026-11-26'
      updated_label: 今天有提交
      updated_days: 0
      stale: false
    entry_updated: '2026-11-24'
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-claude-style/
  generated: true
lastmod: '2026-11-24'
---

为 DSH Web GUI 复刻 Claude Code Desktop 风格与交互的主题插件：Claude/DeepSeek 品牌切换、六套配色预设、亮暗跟随系统，并含消息回退与版本历史等交互增强，同时只启用一个主题。
