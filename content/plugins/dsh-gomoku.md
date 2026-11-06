---
title: dsh-gomoku
description: 在 DSH 里和 AI 下五子棋，也可以让两个 AI 对局看谁棋力更强；15×15 棋盘嵌在侧边栏，每步落子来自 LLM 纯推理判断，黑/白提示词可编辑、推理过程可见。
categories:
- fun
tags: &id001
- 游戏
- 五子棋
weight: 1010
params:
  plugin:
    id: dsh-gomoku
    name: dsh-gomoku
    category: fun
    status: community
    repo: https://github.com/omdsh-dev/dsh-gomoku
    install: dsh plugin --profile demo add github:omdsh-dev/dsh-gomoku
    summary: 在 DSH 里和 AI 下五子棋，也可以让两个 AI 对局看谁棋力更强；15×15 棋盘嵌在侧边栏，每步落子来自 LLM 纯推理判断，黑/白提示词可编辑、推理过程可见。
    features:
    - 人机与双 AI 对弈：执黑/执白/双 AI 三种模式，15×15 无禁手规则
    - 黑白 AI 分别设置模型与思考档位（Off/High/Max），不支持时自动回落默认
    - 思考过程分侧展示：每方推理日志列在棋盘两侧，可点开查看完整推理
    - 暂停与手动接管：随时中断 AI 思考、手动落子，再次继续
    - 黑/白系统提示词分开编辑（含规则、术语与 Few-shot 示例）；弹窗关闭不中断对局；瞬时失败自动重试
    tags: *id001
    flag: 社区项目，非官方；当前适配 dsh 0.2.0-rc.2，需 Web profile，不再兼容 0.1.x 客户端运行时
    notes: README 提示：需 Web profile（如内置 web profile），适配 dsh 0.2.0-rc.2；使用新版 dsh.client 声明与 dsh-client-ui-renderer 插槽，升级 dsh 后应重新做兼容性检查。
    refs:
    - id: baike-dsh
      title: 百度百科：DeepSeek Harness
      url: https://baike.baidu.com/item/deepseek%20harness/68533699
      kind_label: 百科
      publisher: 百度百科
    source_count: 1
    repo_confirmed: true
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-gomoku/
  generated: true
---

在 DSH 里和 AI 下五子棋，也可以让两个 AI 对局看谁棋力更强；15×15 棋盘嵌在侧边栏，每步落子来自 LLM 纯推理判断，黑/白提示词可编辑、推理过程可见。
