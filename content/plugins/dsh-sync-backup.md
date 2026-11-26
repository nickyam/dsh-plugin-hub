---
title: dsh-sync-backup
description: 加密备份同步
categories: [tool]
tags: [加密, 同步, 备份]
weight: 4002
params:
  plugin:
    id: dsh-sync-backup
    name: dsh-sync-backup
    category: tool
    status: community
    repo: https://github.com/weibaohui/dsh-sync
    install: dsh plugin --profile web add github:weibaohui/dsh-sync
    summary: 加密备份同步
    features:
    - 加密归档
    - 双通道（Git+WebDAV/对象存储）
    - 默认零外传
    - 配置、技能清单、会话记录全管
    - 定时备份+保留策略（近 N 份+每月 1 份+每年 1 份）
    - 恶意冲突明确决策
---
