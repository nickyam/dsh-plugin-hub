---
title: dsh-our-free-model
description: 装上后模型列表里多出若干可直接用的免费选项，不用注册、不用填 API Key，用来零成本起步；免费车道来自 OpenCode Zen 网关、Kilo AI 公共网关等上游，直连不经第三方中转。
categories:
- model
tags: &id001
- 免费模型
- 免Key
- 备用通道
weight: 1050
params:
  plugin:
    id: dsh-our-free-model
    name: dsh-our-free-model
    category: model
    status: community
    repo: https://github.com/Ebony-Vinyl/dsh-our-free-model
    install: dsh plugin --profile web add @ebony-vinyl/dsh-our-free-model@2.8.0
    summary: 装上后模型列表里多出若干可直接用的免费选项，不用注册、不用填 API Key，用来零成本起步；免费车道来自 OpenCode Zen 网关、Kilo AI 公共网关等上游，直连不经第三方中转。
    features:
    - 开箱即用无配置：不需要账号、Key 或配额申请，免费车道模型直接出现在选择器
    - 上游公开透明且直连：免费车道来源为 OpenCode Zen 网关与 Kilo AI 公共网关，不经第三方中转
    - 应用内升级与热重载：设置页一键升级（SHA-256 校验、备份、原子替换、热重载），失败自动回滚
    - 用量看板与转发端口：Token 热力图留在本机；本机工具可通过 base URL 调用，提供 /v1/chat/completions 等端点
    - 聚合渠道与省 Token：内置 76 家提供商注册表，写入 Key 后模型以 provider/model 出现；工具输出压缩实测可移除约 90% 字节
    tags: *id001
    flag: 免费额度与可用性以仓库说明为准；npm 裸名 dsh-our-free-model 非本仓库发布，请装带 scope 的 @ebony-vinyl 包
    notes: README 警告不要装 npm 上裸名的 dsh-our-free-model（非本仓库发布）；本仓库发布的是带 scope 的 @ebony-vinyl/dsh-our-free-model。免费车道高峰期可能按会话限流返回 429；部分上游声明提示词可能被记录，勿发敏感内容。上游额度政策随时可能变更。
    repo_confirmed: true
    gh:
      stars: 79831
      forks: 2249
      issues: 205
      language: JavaScript
      license: NOASSERTION
      pushed_at: '2026-11-18T02:24:22Z'
      archived: false
      slug: Ebony-Vinyl/dsh-our-free-model
      stars_label: 79.8k
      forks_label: '2249'
      pushed_date: '2026-11-18'
      updated_label: 8 天前有提交
      updated_days: 8
      stale: false
    entry_updated: '2026-11-06'
    category_label: 免费模型与接入
    status_label: 社区
    weight: 1050
    url: /plugins/dsh-our-free-model/
  generated: true
---

装上后模型列表里多出若干可直接用的免费选项，不用注册、不用填 API Key，用来零成本起步；免费车道来自 OpenCode Zen 网关、Kilo AI 公共网关等上游，直连不经第三方中转。
