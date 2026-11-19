---
title: DSH-EasyRewrite（撤回与气泡编辑）
description: 给 DSH Web 补上「发出去了也能改」：点自己的消息气泡原位重编辑，点复制键旁的撤回键把这条及其后全部截掉。关键是惰性提交——在你真正按「确定」或「发送」之前，对话、模型上下文、会话日志一点没动。
categories:
- ui
tags: &id001
- 撤回
- 消息编辑
- 界面增强
weight: 1010
params:
  plugin:
    id: dsh-easyrewrite
    name: DSH-EasyRewrite（撤回与气泡编辑）
    aliases:
    - 撤回
    - 气泡编辑
    - 消息重编辑
    - easyrewrite
    category: ui
    status: community
    repo: https://github.com/Renzic-Stone/DSH-EasyRewrite
    install: dsh plugin --profile web add dsh-easyrewrite
    summary: 给 DSH Web 补上「发出去了也能改」：点自己的消息气泡原位重编辑，点复制键旁的撤回键把这条及其后全部截掉。关键是惰性提交——在你真正按「确定」或「发送」之前，对话、模型上下文、会话日志一点没动。
    features:
    - 气泡原位编辑：单击自己的消息进编辑态，保留原始 Markdown，Esc 取消 / Ctrl+Enter 确定
    - 撤回：每条用户消息的复制键旁一个撤回键，弹灰色的「撤回这条消息及其后 x 条提问？」确认胶囊
    - 惰性提交：确认撤回只回填输入框，真正的截断发生在按发送时；中途关掉 DSH，会话零改动
    - 无痕替换：原会话归档 → 同名新会话顶到目标消息之前 → 修改后的文本自动发出，感知上就是原对话被编辑过
    - 版本翻页器：最终回复的动作条上渲染 ‹1/2›，点击或方向键切换版本，其余归档，只留一份活跃
    - 三档编辑宽度：紧凑（气泡原宽起，上限 360px）/ 标准 360px / 扩展顶满 / 自定义
    - 带图编辑：确认后图片随文本一起发出，编辑中可删可粘可拖入新图，刷新后进度能恢复
    - 草稿持久化：按会话存，切标签页或刷新不丢；超过 10 秒未处理的待定草稿自动备份到本地
    - 三语界面与官方风格设置卡：中文 / English / 日本語，改完即时生效
    tags: *id001
    flag: 靠归档 + 同名新会话实现，会话列表会多出归档项
    notes: '只用官方扩展点（keyed 槽覆盖、官方 fork RPC、官方组件与设计令牌），不改 DSH 源码，卸载即还原、不留配置残留。一条硬限制来自宿主：DSH 只能在已闭合的轮次边界上 fork，正在流式输出的那一轮里的消息要等回复结束才能撤回。npm 包名 dsh-easyrewrite，也可 github: 装。v3.1.0 起适配 dsh 0.2.x 与 0.1.7 系列；0.1.1-rc.2 及更早宿主请停在 2.3.1（那条线的最终版，功能完整、不再加新功能）。'
    repo_confirmed: true
    gh:
      stars: 133
      forks: 16
      issues: 3
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-12T12:51:49Z'
      archived: false
      slug: Renzic-Stone/DSH-EasyRewrite
      stars_label: '133'
      forks_label: '16'
      pushed_date: '2026-11-12'
    category_label: 界面与体验
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-easyrewrite/
  generated: true
---

给 DSH Web 补上「发出去了也能改」：点自己的消息气泡原位重编辑，点复制键旁的撤回键把这条及其后全部截掉。关键是惰性提交——在你真正按「确定」或「发送」之前，对话、模型上下文、会话日志一点没动。
