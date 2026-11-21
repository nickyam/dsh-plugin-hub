---
title: dsh-qq2006
description: 把 DeepSeek Harness 的 WebUI 一键变回 2006 年的 QQ 客户端：注册珊瑚蓝主题、镜像 body[data-ds-skin]、全局皮肤表 + 完整组件级补丁，从登录窗到聊天窗口全链路还原那个蓝色小企鹅。可切换、可持久化、默认皮肤零污染。
categories:
- fun
tags: &id001
- 皮肤
- 怀旧
weight: 1010
params:
  plugin:
    id: dsh-qq2006
    name: dsh-qq2006
    category: fun
    status: community
    repo: https://github.com/LaplaceYoung/dsh-qq2006
    install: dsh plugin --profile web add https://github.com/LaplaceYoung/dsh-qq2006
    summary: 把 DeepSeek Harness 的 WebUI 一键变回 2006 年的 QQ 客户端：注册珊瑚蓝主题、镜像 body[data-ds-skin]、全局皮肤表 + 完整组件级补丁，从登录窗到聊天窗口全链路还原那个蓝色小企鹅。可切换、可持久化、默认皮肤零污染。
    features:
    - 可切换 QQ2006 皮肤：设置 → 通用 → QQ2006 皮肤，偏好持久化，随时切回默认皮肤零污染
    - 完整组件级皮肤（源码 monorepo 形态）：QQ2006 登录窗、主面板、聊天窗 chrome、列表式消息、QQ 秀右栏
    - 珊瑚蓝换肤：通过 --dsw-alias-* / --dsw-specific-* token 覆盖背景/边框/按钮/文字配色
    - 原版消息形式与真实交互：列表式消息、Alt+S 发送、右键复制、提示音、QQ 黄色反馈 tip
    - 4 套换肤预设：经典蓝 / 粉红 / 薄荷绿 / 紫罗兰，窗口内实时切换
    tags: *id001
    flag: 社区项目，非官方；npm 发行版仅含 token 换肤与全局皮肤表，登录窗/聊天窗等组件级效果需源码 monorepo 形态才完整
    notes: README 说明：npm 发行版经插件机制无法注入组件级皮肤（改的是宿主 UI 包源码），完整效果需 fork 的 skin/qq2006 分支或 git apply 补丁；素材来自 mengkunsoft/QQ2006，仅供学习交流、请勿商用。
    repo_confirmed: true
    gh:
      stars: 32
      forks: 1
      issues: 0
      language: JavaScript
      license: MIT
      pushed_at: '2026-08-27T17:59:55Z'
      archived: false
      slug: LaplaceYoung/dsh-qq2006
      stars_label: '32'
      forks_label: '1'
      pushed_date: '2026-08-27'
      updated_label: 2 个月前有提交
      updated_days: 85
      stale: false
    category_label: 娱乐与彩蛋
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-qq2006/
  generated: true
---

把 DeepSeek Harness 的 WebUI 一键变回 2006 年的 QQ 客户端：注册珊瑚蓝主题、镜像 body[data-ds-skin]、全局皮肤表 + 完整组件级补丁，从登录窗到聊天窗口全链路还原那个蓝色小企鹅。可切换、可持久化、默认皮肤零污染。
