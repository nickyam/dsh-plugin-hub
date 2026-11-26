---
title: dsh-pocket（手机同屏）
description: 把 DSH 装进口袋：电脑上跑 dsh web，装好插件后手机扫个二维码就能实时看到并操控电脑上的同一个界面——发任务、看输出、点审批，局域网或公网都能用。
categories:
- remote
tags: &id001
- 手机
- 远程
- 扫码
- 同屏
weight: 1020
params:
  plugin:
    id: dsh-pocket
    name: dsh-pocket（手机同屏）
    aliases:
    - DSH Pocket
    - 手机远程
    - 口袋 DSH
    category: remote
    status: community
    repo: https://github.com/shaobeichen/dsh-pocket
    install: dsh plugin --profile web add dsh-pocket
    summary: 把 DSH 装进口袋：电脑上跑 dsh web，装好插件后手机扫个二维码就能实时看到并操控电脑上的同一个界面——发任务、看输出、点审批，局域网或公网都能用。
    features:
    - 扫码同屏：手机扫码即实时同步电脑上 DSH 的同一界面，人在外面也能看进度、发任务、点审批
    - 局域网 + 公网：支持局域网直连与公网访问两种链路，无需远程桌面或 SSH
    - 一个包一个设置页：装上插件、打开设置页即可用，不用改 DSH 源码
    tags: *id001
    flag: 社区项目；公网访问意味着把 DSH 界面暴露到外网，请设置强口令并留意可访问范围
    notes: 仓库 shaobeichen/dsh-pocket（GitHub 有多个同名 dsh-pocket / dsh-pocket-plus，本条取 README 完整、★ 数最高的 shaobeichen 主仓），npm 包 dsh-pocket。README 徽章里 License 标注有 MIT/GPL 混排，本站不据此下结论。
    repo_confirmed: true
    gh:
      stars: 3040
      forks: 133
      issues: 4
      language: JavaScript
      license: GPL-2.0
      pushed_at: '2026-11-15T04:10:21Z'
      archived: false
      slug: shaobeichen/dsh-pocket
      stars_label: '3040'
      forks_label: '133'
      pushed_date: '2026-11-15'
      updated_label: 11 天前有提交
      updated_days: 11
      stale: false
    entry_updated: '2026-11-17'
    category_label: 移动端与远程
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-pocket/
  generated: true
---

把 DSH 装进口袋：电脑上跑 dsh web，装好插件后手机扫个二维码就能实时看到并操控电脑上的同一个界面——发任务、看输出、点审批，局域网或公网都能用。
