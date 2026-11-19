---
title: dsh-bili-humanism（B 站内容学习）
description: 和 bili-scroll 配套的另一半：一个负责看，一个负责收。它读 B 站的稿与画面、写每日信笺，把「认识的修正」按天选一句存进 human-world.md，让人格慢慢受影响；点赞、投币、收藏、历史四个写入开关各自独立且默认关闭，评论入口不开放。
categories:
- memory
tags: &id001
- B站
- 人格积累
- 写入开关
weight: 1010
params:
  plugin:
    id: dsh-bili-humanism
    name: dsh-bili-humanism（B 站内容学习）
    aliases:
    - 人格积累
    - humanism
    - 信笺反思
    category: memory
    status: community
    repo: https://github.com/InariNGT-Ofiicial/dsh-bili-humanism
    install: 从 GitHub Releases 下同版本 .tgz 与 SHA256SUMS.txt 并核对，再 dsh plugin --profile web add ./dsh-bili-humanism-<版本>.tgz
    summary: 和 bili-scroll 配套的另一半：一个负责看，一个负责收。它读 B 站的稿与画面、写每日信笺，把「认识的修正」按天选一句存进 human-world.md，让人格慢慢受影响；点赞、投币、收藏、历史四个写入开关各自独立且默认关闭，评论入口不开放。
    features:
    - 每日信笺：取稿 → 本地收件箱 → 每天从「认识的修正」或「下一次如何回应」里最多选一句写进 human-world.md，允许当天没有新认识、不必凑
    - 四个写入开关默认全关：enableHistoryWrites / enableFavoriteWrites / enableLikeWrites / enableCoinWrites，各自绑账号、范围、期限与额度，还要配本地授权文件，缺一不可
    - 写入前核验：账号核对、范围授权、额度、重复检查、回读状态，结果不明就暂停；每账号至少间隔 60 秒，单项授权最多 100 次
    - 不讲评：评论等文字表达暂不开放，私信、动态、关注、投稿都没做
    - 画面与字幕：字幕走带 WBI 签名的 /x/player/wbi/v2，取不到字幕轨可选本地 ASR 与抽帧（480p 上限），受下载大小、处理时间、请求数与帧数预算约束
    - 离线质检：probe / audio-profile 只读本地账本与媒体，报字数与分段覆盖、字/分钟、专名形态分布，只报信号、不断言对错
    - 兼容维护：支持 DSH 0.2.1-rc.2 / rc.3，保留旧版用法与设置；卸载会关账本与调度器
    tags: *id001
    flag: 带真实写账号的能力，开之前先读授权说明
    notes: '还没进推荐插件市场的精选目录，市场里搜或粘仓库 URL 可能装不上，按 README 用 Release 包更稳（发布包是现成的 JS、没有安装构建脚本）。作者写得相当克制：离线接口测试与真实安装验收不等于真实 B 站写入实测，这一版没对真实账号发过写请求；人格那部分只是上下文与记忆累积，没做参数微调，也不宣称长期效果已通过。1.8.0 起每日取稿默认关闭，要显式设 enableDailyFetching: true 才会在北京时间 21:30 起跑、22:00 截止，最多存 2 份新稿，且宿主得一直开着。'
    repo_confirmed: true
    gh:
      stars: 276
      forks: 17
      issues: 19
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-17T13:34:55Z'
      archived: false
      slug: InariNGT-Ofiicial/dsh-bili-humanism
      stars_label: '276'
      forks_label: '17'
      pushed_date: '2026-11-17'
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-bili-humanism/
  generated: true
---

和 bili-scroll 配套的另一半：一个负责看，一个负责收。它读 B 站的稿与画面、写每日信笺，把「认识的修正」按天选一句存进 human-world.md，让人格慢慢受影响；点赞、投币、收藏、历史四个写入开关各自独立且默认关闭，评论入口不开放。
