---
title: dsh-ops
description: 以提高 token 效率为目的的底层操作工具插件，提供 ops 系列工具并隐藏 / 替换部分官方工具，减少 Token 消耗与任务耗时，低改动面、低侵入性。
categories:
- workflow
tags: &id001
- 自动化
- token优化
weight: 1010
params:
  plugin:
    id: dsh-ops
    name: dsh-ops
    category: workflow
    status: community
    repo: https://github.com/T-Auto/dsh-ops
    install: dsh plugin --profile web add dsh-ops
    summary: 以提高 token 效率为目的的底层操作工具插件，提供 ops 系列工具并隐藏 / 替换部分官方工具，减少 Token 消耗与任务耗时，低改动面、低侵入性。
    features:
    - Bash 与宿主 Shell 隐藏独立配置：Windows 可用 ops_bash 替代 pwsh，也可保留官方 Shell
    - Native / PTC 消费者预设共享有界工具面：Bash 由单行开关控制，关闭替换时原版工具保持可用
    - 动态工具加载：启用 DSH 预留的 tools_addition，渐进式加载高级功能（pdf / word 读取、批量修改），不导致系统提示词膨胀
    - Native 模式紧凑工具：返回带行号与更好错误回馈，遏制报错循环、减少调用轮次
    - PTC 模式结构化工具：返回结构化 JSON 值，降低编写 TypeScript 的 token 总量与心智负担
    tags: *id001
    notes: 需 DSH 0.2.2-rc.1 及以上（0.5 系列不再支持 0.2.0 / 0.2.1）；桌面端须用桌面应用自带 CLI。README 曾提示 0.5.0 存在缓存膨胀 bug，安装前请确认已修复到最新版。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-ops/
  generated: true
---

以提高 token 效率为目的的底层操作工具插件，提供 ops 系列工具并隐藏 / 替换部分官方工具，减少 Token 消耗与任务耗时，低改动面、低侵入性。
