---
title: dsh-backup
description: 备份 DSH 用户数据
categories: [tool]
tags: [备份, 恢复, 同步]
weight: 4000
params:
  plugin:
    id: dsh-backup
    name: dsh-backup
    category: tool
    status: community
    repo: https://github.com/xiaoyuyu6420/dsh-backup
    install: dsh plugin --profile web add github:xiaoyuyu6420/dsh-backup
    summary: 备份 DSH 用户数据
    features:
    - 备份 ~/.dsh 全量用户数据
    - 支持定时备份与手动备份
    - 支持通过 GitHub 仓库进行版本化存储
---
