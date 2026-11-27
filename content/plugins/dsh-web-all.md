---
title: dsh-web-all（Web 全家桶）
description: DSH Web 的官方聚合包，一条命令装齐家族全部功能插件：任务看板、Git 图谱、桌面宠物、移动端远程、SSH 运维、模型能力、用量统计、会话归档、皮肤中心、设置区与社区插件，外加右侧面板 dsh-better-sidebar。每项可在「设置 → 插件 → 插件管理」里单独开关。
categories:
- ui
tags: &id001
- 全家桶
- 看板
- 远程
- SSH
weight: 1030
params:
  plugin:
    id: dsh-web-all
    name: dsh-web-all（Web 全家桶）
    aliases:
    - dsh-web-ui-all
    - '@linxin666/dsh-web-all'
    - dsh-web full suite
    category: ui
    status: community
    repo: https://github.com/zhu1090093659/dsh-web
    install: dsh plugin --profile web add @linxin666/dsh-web-all@latest
    summary: DSH Web 的官方聚合包，一条命令装齐家族全部功能插件：任务看板、Git 图谱、桌面宠物、移动端远程、SSH 运维、模型能力、用量统计、会话归档、皮肤中心、设置区与社区插件，外加右侧面板 dsh-better-sidebar。每项可在「设置 → 插件 → 插件管理」里单独开关。
    features:
    - 任务看板：多列跟踪与定时调度
    - 移动端远程：二维码配对、跨设备同步、触控手势
    - SSH 运维：Web 终端、SFTP 传输、隧道与集群命令
    - 用量统计、会话归档、皮肤中心、社区插件源
    - 右侧面板 dsh-better-sidebar（文件渲染 / 编辑、终端、Git、对话、子代理）
    tags: *id001
    flag: 包名 @linxin666/dsh-web-all，仓库是 zhu1090093659/dsh-web 单体仓
    notes: 官方仓库是 zhu1090093659/dsh-web 单体仓，npm 包发布在 @linxin666 名下；安装后需重启 dsh web 才出现侧栏图标。也可直接 `dsh plugin --profile web add github:zhu1090093659/dsh-web` 从仓库装。子插件独立发包，只想用部分功能可单独安装对应 @linxin666/dsh-* 包。
    repo_confirmed: true
    gh:
      stars: 10656
      forks: 657
      issues: 0
      language: TypeScript
      license: Apache-2.0
      pushed_at: '2026-11-26T17:09:24Z'
      archived: false
      slug: zhu1090093659/dsh-web
      stars_label: 10.7k
      forks_label: '657'
      pushed_date: '2026-11-26'
      stale: false
    entry_updated: '2026-11-06'
    category_label: 界面与体验
    status_label: 社区
    weight: 1030
    url: /plugins/dsh-web-all/
  generated: true
lastmod: '2026-11-06'
---

DSH Web 的官方聚合包，一条命令装齐家族全部功能插件：任务看板、Git 图谱、桌面宠物、移动端远程、SSH 运维、模型能力、用量统计、会话归档、皮肤中心、设置区与社区插件，外加右侧面板 dsh-better-sidebar。每项可在「设置 → 插件 → 插件管理」里单独开关。
