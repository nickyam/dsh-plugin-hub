---
title: agentero-dsh
description: 把本地优先的科研工作台 Agentero 接进 DSH，在对话旁开文献库与 PDF 阅读器，让 Agent 查论文、划词翻译、写笔记、整理结论，资料留在本机 Vault。
categories:
- memory
tags: &id001
- 科研
- 文献
- PDF
- 笔记
- 知识库
weight: 1010
params:
  plugin:
    id: agentero-dsh
    name: agentero-dsh
    aliases:
    - Agentero
    - Agentero × DeepSeek Harness
    category: memory
    status: community
    repo: https://github.com/poco-ai/agentero-dsh-plugin
    install: dsh plugin --profile web add agentero-dsh
    summary: 把本地优先的科研工作台 Agentero 接进 DSH，在对话旁开文献库与 PDF 阅读器，让 Agent 查论文、划词翻译、写笔记、整理结论，资料留在本机 Vault。
    features:
    - 读文献：搜索、标签、按 arXiv、DOI 或链接导入、补下载、删除到回收站，回答时引用真实本地论文
    - 读 PDF：翻页、查找、目录、链接，划词后复制、高亮、批注、翻译或加入对话
    - 全文翻译：用 DSH 配置的模型在原页面逐段替换，保留公式与版面
    - 写笔记：编辑自有笔记或让 Agent 代写，每篇论文有专属笔记，讨论结论可整理成阅读笔记
    - 本地优先：论文、PDF、笔记、标注都留在 Vault，与 Agentero 桌面端共用，插件只在本机运行、不另建数据库
    tags: *id001
    notes: 社区项目（组织 poco-ai，非 DeepSeek 官方；原文署名作者 Phil-Fan 为贡献者，主项目仓库在 poco-ai/Agentero）。npm 包名为 agentero-dsh，对应仓库名是 agentero-dsh-plugin（两者不一致，以此仓库为准）。需 DSH 0.2.x、Node.js 24.9+、一个 Agentero Vault 与 Agentero CLI；装完在侧栏打开 agentero-dsh 并配置 CLI 与知识库目录。文章（wx-feishu）称其「读论文、高亮、翻译、记笔记在一个窗口完成」，与 README 一致。
    refs:
    - id: wx-feishu
      title: 3.5 万个插件里，DeepSeek 官方为什么只挑了这 4 个?
      url: https://mp.weixin.qq.com/s/pdJ8cQW1Ua_jhtRR7wR8iQ
      kind_label: 公众号
      publisher: 飞叔（公众号：飞叔 AI赋能推客）
    source_count: 1
    repo_confirmed: true
    category_label: 记忆与知识
    status_label: 社区
    weight: 1010
    url: /plugins/agentero-dsh/
  generated: true
---

把本地优先的科研工作台 Agentero 接进 DSH，在对话旁开文献库与 PDF 阅读器，让 Agent 查论文、划词翻译、写笔记、整理结论，资料留在本机 Vault。
