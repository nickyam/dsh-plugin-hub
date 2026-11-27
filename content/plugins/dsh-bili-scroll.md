---
title: dsh-bili-scroll（刷 B 站）
description: 每天替你刷一轮 B 站：按关键词搜近几天的视频，逐条读字幕原文（不看摘要）判断值不值得看，写一份 Markdown 报告到 out/<日期>.md，特别值得的留一条评论 @ 你。
categories:
- content
tags: &id001
- B站
- 日报
- 内容筛选
weight: 1020
params:
  plugin:
    id: dsh-bili-scroll
    name: dsh-bili-scroll（刷 B 站）
    aliases:
    - B站日报
    - bili scroll
    - 每天刷B站
    category: content
    status: community
    repo: https://github.com/c1overzz/dsh-bili-scroll
    install: dsh plugin --profile web add https://github.com/c1overzz/dsh-bili-scroll/releases/download/v2.0.2/dsh-bili-scroll-2.0.2.tgz
    summary: 每天替你刷一轮 B 站：按关键词搜近几天的视频，逐条读字幕原文（不看摘要）判断值不值得看，写一份 Markdown 报告到 out/<日期>.md，特别值得的留一条评论 @ 你。
    features:
    - 按关键词搜（留空用内置几组），逐条读字幕原文再判断；没字幕的演示类视频先从故事板抽几帧看画面
    - 日报落盘：每条含「为什么值得」与它自己的一句话，段首固定写成
    - 自动评论：开着时每轮发一条评论 @ 你，默认每轮 1 条，设置页最多可到 20 条
    - 峰谷时段自动跑：挑 DeepSeek 优惠时段，省 token
    - 本地转写：可选装 Whisper 等本地转写，读不到字幕的视频也能处理（模型 538 MB 起，可在设置里换小的）
    tags: *id001
    flag: npm 上是旧版，别用 add dsh-bili-scroll 装
    notes: 这条最容易踩坑——npm 上的包还停在 0.1.7（作者说发布账号在申诉，2026-10-17 之后的新版只能从 Release 装），照 npm 装会拿到缺参数的旧版，建 Python 环境时依赖装不上、二维码也画不出来。用 README 给的 Release tgz 直链，连不上 GitHub 可在前面加 gh-proxy.com。要求 dsh ≥ 0.1.7-rc.1，版本不够内核会静默跳过这个插件，装了跟没装一样还不报错。装完必须重启一次 dsh。空间：不装本地转写约 84 MB，装了约 1 GB。机器上最好有 Python 3.10+ 或 uv（都没有也行，插件会自己下一份 uv 并核对 sha256）。桌面版 0.1.3 及更早装不起来，0.1.4 起已修；桌面版上自动跑那一轮若卡住，先用设置页的「现在跑一轮」。
    repo_confirmed: true
    gh:
      stars: 1479
      forks: 135
      issues: 137
      language: JavaScript
      license: MIT
      pushed_at: '2026-11-23T10:19:55Z'
      archived: false
      slug: c1overzz/dsh-bili-scroll
      stars_label: '1479'
      forks_label: '135'
      pushed_date: '2026-11-23'
      stale: false
    entry_updated: '2026-11-19'
    category_label: 内容创作与办公
    status_label: 社区
    weight: 1020
    url: /plugins/dsh-bili-scroll/
  generated: true
lastmod: '2026-11-19'
---

每天替你刷一轮 B 站：按关键词搜近几天的视频，逐条读字幕原文（不看摘要）判断值不值得看，写一份 Markdown 报告到 out/<日期>.md，特别值得的留一条评论 @ 你。
