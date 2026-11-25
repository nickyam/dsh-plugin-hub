---
title: dsh-pua（任务推进与验收）
description: 把原版 PUA 带到 DSH：在 Agent 反复失败、过早放弃或草率宣告完成时，提醒换方法、查原因、拿证据；支持 15 种大厂风味与角色模式、会话级开关、按验收结果继续的 Loop 循环与防作弊门。
categories:
- workflow
tags: &id001
- PUA
- 任务推进
- 验收循环
- 防作弊
weight: 1010
params:
  plugin:
    id: dsh-pua
    name: dsh-pua（任务推进与验收）
    aliases:
    - DSH PUA
    - PUA 任务推进
    - 验收循环
    category: workflow
    status: community
    repo: https://github.com/MichengAI/dsh-pua
    install: dsh plugin --profile web add @michengai/dsh-pua@latest --registry=https://registry.npmjs.org/
    summary: 把原版 PUA 带到 DSH：在 Agent 反复失败、过早放弃或草率宣告完成时，提醒换方法、查原因、拿证据；支持 15 种大厂风味与角色模式、会话级开关、按验收结果继续的 Loop 循环与防作弊门。
    features:
    - 遇到困难换方法、完成前核对证据，减少「说完成了却没验证」；效果随模型与任务而定，不保证每次解决
    - 15 种大厂风味 + P7/P9/P10/夸夸/妈妈等角色模式，侧边栏全局配置，聊天入口可单独调当前会话
    - 验收 Loop：填任务、验收命令与轮次上限，Agent 持续修正直到验收通过/达上限/取消；GFM 管道表输出状态表与 KPI 卡
    - 防作弊门：拦截读取隐藏基准答案（含联网搜索），变更测试/评分/CI 资产时向模型注入提醒
    tags: *id001
    flag: 全局开关控制入口可用，当前会话默认关闭需单独打开；宿主 0.2.2+（>=0.2.2-rc.1 <0.3.0-0），Node 22.19+；Apache-2.0
    notes: 官方仓库 github.com/MichengAI/dsh-pua（npm 包 @michengai/dsh-pua，Apache-2.0）。文章只给包名 @michengai/dsh-pua 与「重复失败/过早放弃/缺少验证时提醒换方法、查原因、提交证据」，与 README 核心定位吻合，据此收录；仓库由包名检索核实。安装命令按官方 README 的精确形式（带 @latest 与 --registry）。版本门槛复杂：0.2.2-rc.1 之前宿主装插件 1.0.12、0.1.x 装 0.3.28；README 自动支持后续 0.2.x RC，0.3.0 由版本门拦截。文章强调「全局允许不等于会话已启用」「Loop 要设验收方式与轮次上限」，与 README 一致。它与站内 dsh-agent-teams（多 Agent 小队）定位不同，未合并。
    repo_confirmed: true
    gh: null
    entry_updated: '2026-11-24'
    category_label: 协作与工作流
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-pua/
  generated: true
---

把原版 PUA 带到 DSH：在 Agent 反复失败、过早放弃或草率宣告完成时，提醒换方法、查原因、拿证据；支持 15 种大厂风味与角色模式、会话级开关、按验收结果继续的 Loop 循环与防作弊门。
