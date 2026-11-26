---
title: dsh-notifier（通知与远程应答）
description: 人不在电脑前，也能知道 agent 在干什么、并且在它等你的时候回一句。28 个出站通道、6 个入站通道，任务完成 / 出错 / 等审批 / 长任务状态都能推出来，也能从手机批准、回答 ask_user、接着对话或切会话。
categories:
- integration
tags: &id001
- 通知
- 手机应答
- 远程审批
weight: 1010
params:
  plugin:
    id: dsh-notifier
    name: dsh-notifier（通知与远程应答）
    aliases:
    - 通知
    - 远程审批
    - notifier
    category: integration
    status: community
    repo: https://github.com/THEWOLFWALKER/dsh-notifier
    install: dsh plugin --profile web add dsh-notifier@latest
    summary: 人不在电脑前，也能知道 agent 在干什么、并且在它等你的时候回一句。28 个出站通道、6 个入站通道，任务完成 / 出错 / 等审批 / 长任务状态都能推出来，也能从手机批准、回答 ask_user、接着对话或切会话。
    features:
    - 推出去：任务完成、需要审批、报错、长任务状态，以及模型主动发起的通知
    - 答得回：手机上批准或拒绝、回答 ask_user、继续对话、给正在跑的回合加指令、切任务与会话
    - 面板就是操作台：DSH 里原生的「Notify & Control」，另留一个本地回环的 Advanced Console 用来救场与深管
    - 失败不外溢：不认识或不安全的入站动作直接失败关闭；单个出站通道挂掉不会带崩整个通知器
    - 会话事件触发：监听 turn/end、approval/asked、agent/error 这类事件；也支持白名单式回传，未知用户的来消息直接丢弃
    tags: *id001
    flag: 通道凭证与回传白名单要先配好再开
    notes: 作者在 README 顶上挂了「正在进行大规模重构，近期更新可能推迟」。装法是 dsh plugin add dsh-notifier@latest --profile <名>，装完重启一次 DSH 让 Host 插件与 client.js 加载。它和几个近名包不是一回事：xzk-abao/dsh-notify-im 是钉钉 / 企微 / 飞书 webhook 的三事件通知，YanYunCY/dsh-gateway-notify 是移植自 magpie 的多通道推送，c-ling/dsh-plugin-notify 又是另一套；要「推 + 回」这个组合，认 THEWOLFWALKER 这份。
    repo_confirmed: true
    gh:
      stars: 64
      forks: 15
      issues: 8
      language: JavaScript
      license: MIT
      pushed_at: '2026-10-31T10:10:16Z'
      archived: false
      slug: THEWOLFWALKER/dsh-notifier
      stars_label: '64'
      forks_label: '15'
      pushed_date: '2026-10-31'
      updated_label: 26 天前有提交
      updated_days: 26
      stale: false
    entry_updated: '2026-11-19'
    category_label: 集成与迁移
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-notifier/
  generated: true
lastmod: '2026-11-19'
---

人不在电脑前，也能知道 agent 在干什么、并且在它等你的时候回一句。28 个出站通道、6 个入站通道，任务完成 / 出错 / 等审批 / 长任务状态都能推出来，也能从手机批准、回答 ask_user、接着对话或切会话。
