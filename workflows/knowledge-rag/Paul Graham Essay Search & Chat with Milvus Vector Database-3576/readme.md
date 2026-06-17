## 简介
**Paul Graham Essay Search & Chat with Milvus Vector Database**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3576

---

# Paul Graham Essay Search & Chat with Milvus Vector Database


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Fetch Essay List | HTTP Request |
| Extract essay names | HTML |
| Split out into items | 数据拆分 |
| Fetch essay texts | HTTP Request |
| Limit to first 3 | 数据限制 |
| Extract Text Only | HTML |
| Recursive Character Text Splitter1 | 文本分割器 |
| Milvus Vector Store | vectorStoreMilvus |
| AI Agent | AI Agent |
| When chat message received | Chat 触发器 |
| Default Data Loader | 文档加载器 |
| Milvus Vector Store as tool | vectorStoreMilvus |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model | OpenAI Chat Model |
| Embeddings OpenAI1 | OpenAI Embeddings |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

Chat 消息触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：手动触发, Chat 消息触发

## 触发方式
- When clicking "Execute Workflow" 触发
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：12
- 输出节点：2
- 分类：knowledge-rag
