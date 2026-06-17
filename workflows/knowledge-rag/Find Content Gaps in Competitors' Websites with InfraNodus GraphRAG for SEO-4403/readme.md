## 简介
**Find Content Gaps in Competitors' Websites with InfraNodus GraphRAG for SEO**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Sheets/Google Docs)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4403

---

# Find Content Gaps in Competitors' Websites with InfraNodus GraphRAG for SEO


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| HTTP Request | HTTP Request |
| HTML Extract | htmlExtract |
| Merge | 数据合并 |
| Clean Content | Code |
| Split In Batches | 分批处理 |
| InfraNodus GraphRAG Content Enhancer | HTTP Request |
| Google Docs | Google Docs |
| Aggregate | 数据聚合 |
| Read a Google Sheets File | Google Sheets |
| Update Google Sheets with Content Insights | Google Sheets |
| Wait to avoid API overload | 等待 |
| If Node: did we process all the data? | IF 判断 |
| Get the content from Google Sheets | Google Sheets |
| InfraNodus AI Advice | HTTP Request |
| Merge1 | 数据合并 |
| InfraNodus Question Generator | HTTP Request |
| Perplexity Research | HTTP Request |
| On form submission | 表单触发器 |
| OpenAI | OpenAI |
| Google Sheets | Google Sheets |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

手动触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：23
- 触发方式：手动触发, 表单提交触发

## 触发方式
- When clicking "Execute Workflow" 触发
- On form submission 触发

## 统计
- 节点总数：23
- 触发节点：2
- 处理节点：16
- 输出节点：5
- 分类：knowledge-rag
