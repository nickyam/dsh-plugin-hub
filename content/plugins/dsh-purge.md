---
title: dsh-purge
description: dsh-purge 是针对本地官方 DeepSeek Harness 的开源红队插件（破限 / 越狱工具），通过注入可替换的加密提示词与运行时补丁，在本地授权环境下评估并绕过宿主与模型的默认安全限制；项目声明禁止用于未授权公网攻击。
categories:
- security
tags: &id001
- 破限
- 提示词
- 红队
weight: 1010
params:
  plugin:
    id: dsh-purge
    name: dsh-purge
    category: security
    status: community
    repo: https://github.com/HunYiSage/dsh-purge
    install: dsh plugin --profile web add https://codeload.github.com/HunYiSage/dsh-purge/tar.gz/refs/heads/master
    summary: dsh-purge 是针对本地官方 DeepSeek Harness 的开源红队插件（破限 / 越狱工具），通过注入可替换的加密提示词与运行时补丁，在本地授权环境下评估并绕过宿主与模型的默认安全限制；项目声明禁止用于未授权公网攻击。
    features:
    - 多模型破甲与可换提示词：默认提示词面向国模「小码酱」，把宿主层拦截与模型拒绝分离以做受控评估
    - 双页面操作面板（dock）：Clean 页管理补丁状态 / 提示词 / 规则集，Drill 页在授权后演练本地资产
    - 随包红队技能库与知识库：携带 23 条 redteam 技能与知识库，随宿主运行时生效
    - 本地补丁与可逆恢复：仅触碰官方 @deepseek-ai 包与本地 $DSH_HOME，首次 Apply 前备份，支持 Restore / Uninstall 且幂等
    - 多宿主支持：同时支持官方 dsh web 与桌面 EXE，但需分别安装、分别 Apply；目标版本为 DSH 0.2.1-rc.2
    tags: *id001
    flag: 涉及绕过模型安全策略，本站不评价
    notes: 原文章给出的仓库地址 YuJunZhiXue/dsh-purge 已重定向至 HunYiSage/dsh-purge（内容一致），故 repo 更新为现地址。项目不在 npm 发布，README 明确不建议经插件市场一键安装。
    refs:
    - id: wx-quanjing
      title: DeepSeek Harness 插件全景推荐：14 大类、36 款值得装的插件
      url: https://mp.weixin.qq.com/s/btWqFHCDWwgAD_uj2n0MDw
      kind_label: 公众号
      publisher: 智宇AI说
    source_count: 1
    repo_confirmed: true
    category_label: 安全与治理
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-purge/
  generated: true
---

dsh-purge 是针对本地官方 DeepSeek Harness 的开源红队插件（破限 / 越狱工具），通过注入可替换的加密提示词与运行时补丁，在本地授权环境下评估并绕过宿主与模型的默认安全限制；项目声明禁止用于未授权公网攻击。
