---
title: dsh-plugin-save-token（省 Token 压缩）
description: 在每次模型请求入口对超长工具输出做可逆、结构感知的压缩：原始全文存盘，模型只看到带检索路径的浓缩版；每条替换都要求一步可还原、且压缩后 token 数严格变小，目标是只降 token 成本不降智能水平。
categories:
- billing
tags: &id001
- 省token
- 上下文压缩
- 工具输出
- 可逆
weight: 1010
params:
  plugin:
    id: dsh-plugin-save-token
    name: dsh-plugin-save-token（省 Token 压缩）
    aliases:
    - save-token
    - 动态省token插件
    category: billing
    status: community
    repo: https://github.com/vibe-any/dsh-plugin-save-token
    install: dsh plugin --profile web add dsh-plugin-save-token
    summary: 在每次模型请求入口对超长工具输出做可逆、结构感知的压缩：原始全文存盘，模型只看到带检索路径的浓缩版；每条替换都要求一步可还原、且压缩后 token 数严格变小，目标是只降 token 成本不降智能水平。
    features:
    - 结构感知压缩：识别管道分隔的高密度表格，保留首 60 行 + 带行号步进采样中段 + 末 40 行，模型拿到「带坐标的地图」可按行号精确取回
    - 可逆红线：任何替换都能一步还原，原始文本始终落盘；压缩后估算 token 必须严格小于原文
    - 中度过压缩更省：README 引述 RCT，激进压缩（keep 0.2）反而让成本 +1.8%，中度压缩（0.5）省 27.9%，故按结构保留而非乱删
    - 长内容才动手：对过长工具结果（大 JSON / CLI 表格 / 日志）生效，短输出不触发
    - 跨客户端：同一套 token 优化内核也作为 Codex CLI 插件（MCP stdio server）发布
    tags: *id001
    flag: 社区项目；需 Web profile 与 pnpm；依赖 spillStore（标准部署自带，缺失时压缩默认关闭）；装后需重启 dsh
    notes: 仓库 vibe-any/dsh-plugin-save-token（GitHub 搜索「save-token deepseek harness」精确命中、★ 最高），npm 已发布 dsh-plugin-save-token（registry 200），README 给 npm / github / 本地三种安装，本站 install 用 npm 稳定版。文章（wx-jiaweisi）实测它省 7.6%，属作者单次口径，本站不采信数字；README 自述「长任务省两成左右、完成率未受影响」也是作者口径，同样只作功能描述不作结论。
    refs:
    - id: wx-jiaweisi
      title: 给 DeepSeek 大肥鱼装省 Token 插件，实测 5 款，最高竟然省了近 40%
      url: https://mp.weixin.qq.com/s/fJnxDLVbNezuCbsjb2asrw
      kind_label: 公众号
      publisher: 甲维斯机（公众号：甲维斯机）
    source_count: 1
    repo_confirmed: true
    category_label: 模型与计费
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-plugin-save-token/
  generated: true
---

在每次模型请求入口对超长工具输出做可逆、结构感知的压缩：原始全文存盘，模型只看到带检索路径的浓缩版；每条替换都要求一步可还原、且压缩后 token 数严格变小，目标是只降 token 成本不降智能水平。
