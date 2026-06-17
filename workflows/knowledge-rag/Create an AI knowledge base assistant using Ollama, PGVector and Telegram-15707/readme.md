## 简介
**Create an AI knowledge base assistant using Ollama, PGVector and Telegram**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15707

---

# Create an AI knowledge base assistant using Ollama, PGVector and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Postgres PGVector Store | PGVector 向量存储 |
| Embeddings Ollama | Ollama Embeddings |
| Default Data Loader | 文档加载器 |
| Question and Answer Chain | chainRetrievalQa |
| Ollama Chat Model | Ollama Chat Model |
| Vector Store Retriever | retrieverVectorStore |
| Postgres PGVector Store1 | PGVector 向量存储 |
| Embeddings Ollama1 | Ollama Embeddings |
| Extract from File | 从文件提取 |
| If | IF 判断 |
| Form | 表单 |
| Form1 | 表单 |
| Switch | Switch 路由 |
| Extract from File1 | 从文件提取 |
| Extract from File2 | 从文件提取 |
| Extract from File4 | 从文件提取 |
| Extract from File5 | 从文件提取 |
| No Operation, do nothing | 空操作 |
| Telegram Trigger | Telegram 触发器 |
| Send a text message | Telegram |
| No Operation, do nothing1 | 空操作 |



## 功能说明

Telegram 机器人，消息驱动自动化流程（Knowledge)表单提交触发、Telegram 消息触发，通过 Telegram + 数据库 实现自动化。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：表单提交触发, Telegram 消息触发

## 触发方式
- On form submission 触发
- Telegram Trigger 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：19
- 输出节点：1
- 分类：knowledge-rag
