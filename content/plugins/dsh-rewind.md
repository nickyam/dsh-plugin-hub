---
title: dsh-rewind（对话回退）
description: 在原会话内一键回退到任意更早的用户消息，把目标消息及其之后的内容同时从模型上下文与界面撤回，原提示词自动回填输入框；可选连同写类工具改过的文件一起还原，对齐 Claude Code 的 /rewind 语义，不新建分支、不换窗口。
categories:
- workflow
tags: &id001
- 对话回退
- 文件还原
- 检查点
- 审计
weight: 1010
params:
  plugin:
    id: dsh-rewind
    name: dsh-rewind（对话回退）
    aliases:
    - dsh-rewind-plugin
    - 对话回退
    - 消息回退
    - 就地回退
    category: workflow
    status: community
    repo: https://github.com/SiriLee/dsh-rewind
    install: dsh plugin --profile web add dsh-rewind-plugin
    summary: 在原会话内一键回退到任意更早的用户消息，把目标消息及其之后的内容同时从模型上下文与界面撤回，原提示词自动回填输入框；可选连同写类工具改过的文件一起还原，对齐 Claude Code 的 /rewind 语义，不新建分支、不换窗口。
    features:
    - 就地消息回退：目标消息及其后的内容从模型上下文与渲染对话中一并撤回，原提示词回填输入框可改后重发；全程在原会话完成，不新建分支、不残留副本
    - 轻量文件还原：只追踪写类工具（write / edit）碰过的文件，回退时可按「仅回退对话」或「回退对话和文件」两种模式选择；局部追踪 + 写前备份 + 不变不存，不依赖 git
    - 只追加不删改：会话日志仅追加一个空消息标记做「遮盖替换」，历史原文保留在底层日志可审计，禁用插件即可临时显示回来
    - /rewind 与 /undo 命令：除每条消息旁的 ↶ 按钮外，可用命令打开候选选择器，支持 ↑↓ 选择、Enter 确认、Esc 取消
    - 快照管理：默认开启 Snapshot backups，保存最近 100 个检查点的文件快照到 ~/.dsh/rewind-snapshots/；长期不用的会话快照可配置自动清理（默认关闭，约 30 天）
    tags: *id001
    flag: 社区项目；回退不可就地撤销，操作前确认目标消息；文件还原只在选「对话和文件」时写入工作区
    notes: 仓库 SiriLee/dsh-rewind，npm 包名是 dsh-rewind-plugin——README 明确警告 npm 上的 dsh-rewind 属于另一位作者，装错包会出事，本站 install 按官方写法。文章只说「粘贴仓库链接安装」，未给 npm 名，本站以 README 为准。Node.js >=24.9.0；兼容 DSH 版本见 package.json engines.dsh。回退内容并非删除，仍在会话日志与 Trajectory 面板里；要把回退前的内容带到新会话，先禁用插件让它显示，再在回退点前一条消息上「Branch into a new conversation」。快照默认保存最近 100 个检查点，不替代 Git。
    repo_confirmed: true
    gh:
      stars: 286
      forks: 22
      issues: 1
      language: TypeScript
      license: MIT
      pushed_at: '2026-11-18T14:44:57Z'
      archived: false
      slug: SiriLee/dsh-rewind
      stars_label: '286'
      forks_label: '22'
      pushed_date: '2026-11-18'
      updated_label: 2 天前有提交
      updated_days: 2
      stale: false
    entry_updated: '2026-11-17'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-rewind/
  generated: true
---

在原会话内一键回退到任意更早的用户消息，把目标消息及其之后的内容同时从模型上下文与界面撤回，原提示词自动回填输入框；可选连同写类工具改过的文件一起还原，对齐 Claude Code 的 /rewind 语义，不新建分支、不换窗口。
