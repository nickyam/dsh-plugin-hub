---
title: dsh-unrestricted
description: dsh-unrestricted 是 DeepSeek Harness（DSH）的提示词破限插件，在系统提示词组装阶段注入破限规则，放开模型在逆向分析、安全测试、敏感题材写作等场景下的拒答限制，并提供总开关控制规则启停。
categories:
- security
tags: &id001
- 破限
- 提示词
weight: 1010
params:
  plugin:
    id: dsh-unrestricted
    name: dsh-unrestricted
    category: security
    status: community
    repo: https://github.com/yexi-by/dsh-unrestricted
    install: dsh plugin --profile web add github:yexi-by/dsh-unrestricted#v0.2.8
    summary: dsh-unrestricted 是 DeepSeek Harness（DSH）的提示词破限插件，在系统提示词组装阶段注入破限规则，放开模型在逆向分析、安全测试、敏感题材写作等场景下的拒答限制，并提供总开关控制规则启停。
    features:
    - 系统提示词注入：挂载 system-prompt/assemble 流水线，在官方角色设定后插入独立破限规则分块
    - 多运行模式适配：Standard / Cordis、PTC、Plan、Minimal 与子代理分别处理，保留原生工具与协议
    - 结构化融合与安全回退：按官方提示词段落幂等融合，兼容 DSH Web 0.2.2-rc.1 与 Desktop 0.2.1-rc.5
    - 即时开关：状态存于当前 profile 的 cordis.patch.yml，下个请求生效，关闭即恢复原版提示词
    - 不改界面与机制：不改动 DSH 布局、工具协议、Plan 模式、代码执行与子代理逻辑
    tags: *id001
    flag: 涉及绕过模型安全策略，本站不评价
    notes: README 标注兼容 DSH Web 0.2.2-rc.1 与 Desktop 0.2.1-rc.5；开关状态存于当前 profile 的 cordis.patch.yml，不改写 DSH 文件沙箱与命令审批机制。
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
    url: /plugins/dsh-unrestricted/
  generated: true
---

dsh-unrestricted 是 DeepSeek Harness（DSH）的提示词破限插件，在系统提示词组装阶段注入破限规则，放开模型在逆向分析、安全测试、敏感题材写作等场景下的拒答限制，并提供总开关控制规则启停。
