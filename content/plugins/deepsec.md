---
title: DeepSec
description: DeepSec（前 VibeGuard）是 AI 安全攻防一体平台，将 Shield（AI 生成代码安全审计）与 Spear（授权渗透测试引擎）统一到一套 CLI、TUI 与 IDE 插件中；并提供了包装该 CLI 的 DSH 插件封装。
categories:
- security
tags: &id001
- 代码审计
- 渗透测试
- 安全
weight: 1010
params:
  plugin:
    id: deepsec
    name: DeepSec
    category: security
    status: community
    repo: https://github.com/Unclecheng-li/DeepSec
    install: ''
    summary: DeepSec（前 VibeGuard）是 AI 安全攻防一体平台，将 Shield（AI 生成代码安全审计）与 Spear（授权渗透测试引擎）统一到一套 CLI、TUI 与 IDE 插件中；并提供了包装该 CLI 的 DSH 插件封装。
    features:
    - Shield 代码审计：实时审计 AI 生成代码中的幻觉包、缺失防护与模式错误（L1 / L2 / L3 SAST）
    - Spear 授权渗透：Recon → Explore → Fact → Reflect → Report → PoC 全流程自动化，内置 40+ 技能包
    - 签名 / 白名单授权闸门：Spear 以授权白名单为核心，拒绝白名单外目标，默认阻止私有 / 回环地址
    - 多角色与多格式报告：5 种角色（pentester / redteam / auditor / blueteam / ctf_player），输出 Markdown / SARIF / JSON / HTML
    - 统一平台与生态：一套 CLI + TUI 工作台 + VSCode / JetBrains 插件，配置统一于 ~/.deepsec/config.yaml
    tags: *id001
    flag: 渗透测试须在授权范围内使用
    notes: README 同时提供 dsh-deepsec-shield 与 dsh-deepsec-spear 两个 DSH 插件封装（位于 dsh-plugins/，包装 DeepSec CLI 为 Agent 工具），但本 README 未给出对应的 dsh plugin add 命令，故 install 留空；核心安装为 pip install -e .，另有 Rust TUI 与 IDE 插件。Spear 渗透以授权白名单为闸门，私有 / 回环地址默认拒绝。
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
    url: /plugins/deepsec/
  generated: true
---

DeepSec（前 VibeGuard）是 AI 安全攻防一体平台，将 Shield（AI 生成代码安全审计）与 Spear（授权渗透测试引擎）统一到一套 CLI、TUI 与 IDE 插件中；并提供了包装该 CLI 的 DSH 插件封装。
