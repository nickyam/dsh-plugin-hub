---
title: dsh-flash-presets（V4.1 Flash 预设）
description: 专为 DeepSeek V4.1 Flash 调校的 DSH agent 预设包：更短上下文窗口 + 工具裁切 + 低频工具优化 + run_code 合并调用，并内置一份「干活规矩」（如 20 轮内完成、长结果只看末尾、检查通过就交付），在不改变模型能力上限的前提下用更低预算完成能力范围内的任务。
categories:
- billing
tags: &id001
- 省token
- 预设
- V4.1 Flash
- PTC
weight: 1010
params:
  plugin:
    id: dsh-flash-presets
    name: dsh-flash-presets（V4.1 Flash 预设）
    aliases:
    - flash-presets
    - V4 Flash 预设
    category: billing
    status: community
    repo: https://github.com/LarryE135/dsh-flash-presets
    install: dsh plugin --profile web add dsh-flash-presets@0.3.1
    summary: 专为 DeepSeek V4.1 Flash 调校的 DSH agent 预设包：更短上下文窗口 + 工具裁切 + 低频工具优化 + run_code 合并调用，并内置一份「干活规矩」（如 20 轮内完成、长结果只看末尾、检查通过就交付），在不改变模型能力上限的前提下用更低预算完成能力范围内的任务。
    features:
    - 13 条效率规矩：20 轮内完成、超长运行结果只看最后几行、检查通过即交付不再额外测试等，核心是管住「什么时候停手」
    - 工具与调用优化：工具裁切、低频工具优化、run_code 合并批量调用、常驻 PTC 运行时
    - 计划模式：内置计划模式组件（plan-mode v1）与旧 preset id 兼容层
    - 版本门槛严格：要求 DSH >=0.2.1-rc.5 <0.2.3-0，engines 闸会拒装不兼容版本；不要装 0.2.5（在 0.2.2-rc.1 上无法新建会话）
    - 以组合包交付：向 profile 插入预设行，不改宿主源码；--profile 取 web/desktop
    tags: *id001
    flag: 社区项目；仅适配 DeepSeek V4.1 Flash 与 DSH 0.2.1-rc.5~0.2.2 区间；三项运行时改动对整个 profile 生效（PTC 覆盖 / glob-grep 并发标记 / 旧 id 解析），需按需用环境变量关闭；装 0.3.1 别装 0.2.5
    notes: 仓库 LarryE135/dsh-flash-presets（GitHub 搜索「flash-presets deepseek」精确命中、★ 最高），npm 包 dsh-flash-presets（registry 200，README 载 latest=0.3.1）。README 说明仓库内版本 0.3.2（2026-11-16）尚未发 npm/Release，故 install 固定到已发布的 0.3.1，避免装到有问题的 0.2.5。文章（wx-jiaweisi）实测省 23%、把浏览器检查次数从 30 降到 17，属作者单次口径，本站不采信数字，只按其「管住停手」的机制描述写功能。
    repo_confirmed: true
    gh:
      stars: 212
      forks: 14
      issues: 1
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-18T14:22:04Z'
      archived: false
      slug: LarryE135/dsh-flash-presets
      stars_label: '212'
      forks_label: '14'
      pushed_date: '2026-11-18'
      updated_label: 3 天前有提交
      updated_days: 3
      stale: false
    entry_updated: '2026-11-17'
    category_label: 模型与计费
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-flash-presets/
  generated: true
---

专为 DeepSeek V4.1 Flash 调校的 DSH agent 预设包：更短上下文窗口 + 工具裁切 + 低频工具优化 + run_code 合并调用，并内置一份「干活规矩」（如 20 轮内完成、长结果只看末尾、检查通过就交付），在不改变模型能力上限的前提下用更低预算完成能力范围内的任务。
