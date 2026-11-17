---
title: dsh-plugin-academic-paper（学术文献）
description: 学术文献插件：检索交给插件、综述交给模型——从 arXiv 与 Semantic Scholar 真实数据源检索并生成 GB/T 7714 / APA / BibTeX 引用，引用格式本地确定性生成，从机制上杜绝模型编造论文、作者与 DOI。
categories:
- content
tags: &id001
- 学术
- 文献
- arXiv
- 引用
- 防幻觉
weight: 1010
params:
  plugin:
    id: dsh-plugin-academic-paper
    name: dsh-plugin-academic-paper（学术文献）
    aliases:
    - 学术文献插件
    - 防编造文献
    category: content
    status: community
    repo: https://github.com/zhaoxuejie/dsh-plugin-academic-paper
    install: dsh plugin --profile web add dsh-plugin-academic-paper
    summary: 学术文献插件：检索交给插件、综述交给模型——从 arXiv 与 Semantic Scholar 真实数据源检索并生成 GB/T 7714 / APA / BibTeX 引用，引用格式本地确定性生成，从机制上杜绝模型编造论文、作者与 DOI。
    features:
    - 真实数据源检索：arXiv + Semantic Scholar 公开 API，支持关键词/作者/年份过滤与相关性/日期/引用数排序
    - 单篇详情：摘要、全部作者、期刊/会议、引用数、PDF 与官方链接
    - 确定性引用：GB/T 7714 / APA / BibTeX 三种格式本地生成，不依赖大模型
    - 会话隔离文献库：DOI / arXiv ID / 标题自动去重，支持删除、清空、批量导出 .bib / .md
    - 防幻觉：system prompt 强制学术文献必须经工具检索，禁止编造
    tags: *id001
    flag: 社区项目；需 Node.js 22+ 的 DSH Web profile；检索走公开 API，注意网络可达性
    notes: 仓库 zhaoxuejie/dsh-plugin-academic-paper，npm 已发布 dsh-plugin-academic-paper（registry 200），README 推荐方式 A npm 安装 dsh plugin --profile web add dsh-plugin-academic-paper，本站 install 与其一致。文章称其「把查这件事从模型手里拿走」，与 README 的「插件负责检索与引用、模型负责解读综述」一致。
    refs:
    - id: wx-xiaobai
      title: DeepSeek Harness 插件越装越卡？17 个真插件＋3 条变现路，按这个顺序装！
      url: https://mp.weixin.qq.com/s/2JXJhd9hmSHGfB39dCUlSQ
      kind_label: 公众号
      publisher: Stefan学AI（公众号：晓白AI纪元）
    source_count: 1
    repo_confirmed: true
    category_label: 内容创作与办公
    status_label: 社区
    weight: 1010
    url: /plugins/dsh-plugin-academic-paper/
  generated: true
---

学术文献插件：检索交给插件、综述交给模型——从 arXiv 与 Semantic Scholar 真实数据源检索并生成 GB/T 7714 / APA / BibTeX 引用，引用格式本地确定性生成，从机制上杜绝模型编造论文、作者与 DOI。
