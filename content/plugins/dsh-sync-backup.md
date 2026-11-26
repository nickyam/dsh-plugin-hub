---
title: dsh-sync-backup（加密备份同步）
description: 加密备份插件，双通道模式，默认本地打包，非本机 http 拒绝。须通过 DSH 设置页配置自动上传通道。凭据存于 DSH 凭据库。
categories:
- tool
tags: &id001
- 加密
- 同步
- 备份
weight: 1000
params:
  plugin:
    id: dsh-sync-backup
    name: dsh-sync-backup（加密备份同步）
    category: tool
    status: community
    repo: https://github.com/weibaohui/dsh-sync
    install: dsh plugin --profile web add github:weibaohui/dsh-sync
    summary: 加密备份插件，双通道模式，默认本地打包，非本机 http 拒绝。须通过 DSH 设置页配置自动上传通道。凭据存于 DSH 凭据库。
    features:
    - 加密归档 + 双通道（Git + WebDAV/对象存储）
    - 默认零外传，仅在显式配置时上传
    - 配置、技能清单、会话记录全管
    - 定时备份 + 保留策略（近 N 份 + 每月 1 份 + 每年 1 份）
    - 恶意冲突明确决策（无法继续必须手动决策）
    tags: *id001
    flag: uploadOnSchedule + dryRun 必须同时开才上传；GIT_ASKPASS 凭据注入；Basic 口令明文 HTTP 等于交出去；非本机 http 拒绝；只能 loopback 127.0.0.1/[::1]
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-26'
    category_label: 工具与能力
    status_label: 社区
    weight: 1000
    url: /plugins/dsh-sync-backup/
  generated: true
---

加密备份插件，双通道模式，默认本地打包，非本机 http 拒绝。须通过 DSH 设置页配置自动上传通道。凭据存于 DSH 凭据库。
