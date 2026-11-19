---
title: dsh-skill-explorer（技能浏览器）
description: 在 DSH 侧栏加一行「Skill Center」，按来源分层浏览当前加载的技能，用每行开关决定某个技能给不给模型调用（改 SKILL.md 头部的 disable-model-invocation），并提供可视化编辑、导入与安全回收站。
categories:
- tool
tags: &id001
- 技能管理
- 侧栏
- 模型调用开关
weight: 1010
params:
  plugin:
    id: dsh-client-ui-skill-explorer
    name: dsh-skill-explorer（技能浏览器）
    aliases:
    - '@linxin666/dsh-client-ui-skill-explorer'
    - 技能浏览器
    - Skill Center
    category: tool
    status: community
    repo: https://github.com/zhu1090093659/dsh-web/tree/dev/packages/dsh-skill-explorer
    install: dsh plugin --profile web add @linxin666/dsh-client-ui-skill-explorer
    summary: 在 DSH 侧栏加一行「Skill Center」，按来源分层浏览当前加载的技能，用每行开关决定某个技能给不给模型调用（改 SKILL.md 头部的 disable-model-invocation），并提供可视化编辑、导入与安全回收站。
    features:
    - 按来源分组：系统自带、项目 .dsh/skills 与 .agents/skills、自定义目录、用户级 ~/.dsh/skills 与 ~/.agents/skills、运行时注册
    - 模型调用开关：每行开关改写 SKILL.md 头部的 disable-model-invocation，关掉后模型看不到该技能但文件仍在硬盘，模型目录热刷新
    - 搜索与分面筛选：按名称或描述边打边筛，叠加来源分组、启用状态与行标记（插件提供 / 无本地文件 / 符号链接）三个分面
    - 导入 / 新建 / 编辑：从主机目录或浏览器读 ZIP 批量建技能（按官方验收规则校验、强来源已提供则跳过、只新建不覆盖），表单新建标准 SKILL.md，编辑只改描述、when-to-use 与正文
    - 安全回收站：删除把文件移入 .trash 可恢复；偏好存 localStorage
    tags: *id001
    flag: 社区项目（BSD-3-Clause，非 DeepSeek 官方）；与 dsh-skills-manager 功能重叠
    notes: 官方仓库是 zhu1090093659/dsh-web 单体仓 dev 分支下的 packages/dsh-skill-explorer 子包，npm 包发布在 @linxin666 名下（@linxin666/dsh-client-ui-skill-explorer），和 dsh-web-all 同源。README 标 DSH >=0.2.2-rc.3。注意 npm repository 字段只写了单体仓根地址，实际源码在 packages/dsh-skill-explorer。文章（wx-top10-30d）把它与第 6 名技能管理器并列并称「功能有重叠，装一个就够」，与 README 定位一致。
    repo_confirmed: true
    gh:
      stars: 10515
      forks: 640
      issues: 0
      language: TypeScript
      license: Apache-2.0
      pushed_at: '2026-11-18T13:49:58Z'
      archived: false
      slug: zhu1090093659/dsh-web
      stars_label: 10.5k
      forks_label: '640'
      pushed_date: '2026-11-18'
    category_label: 工具与能力
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-client-ui-skill-explorer/
  generated: true
---

在 DSH 侧栏加一行「Skill Center」，按来源分层浏览当前加载的技能，用每行开关决定某个技能给不给模型调用（改 SKILL.md 头部的 disable-model-invocation），并提供可视化编辑、导入与安全回收站。
