## 简介
**Chat with Your Email History using Telegram, Mistral and Pgvector for RAG**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3763

---

# Chat with Your Email History using Telegram, Mistral and Pgvector for RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Loop Over Items | 分批处理 |
| Came from Telegram? | IF 判断 |
| When chat message received | Chat 触发器 |
| Postgres PGVector Store | PGVector 向量存储 |
| Call the SQL composer Workflow | 工作流工具 |
| Embeddings Ollama | Ollama Embeddings |
| Beautify chat response | 数据设置 |
| Split text into chunks | Code |
| Respond on Telegram in batches | Telegram |
| Escape Markdown | Code |
| No Operation, do nothing | 空操作 |
| Simple Memory | 记忆缓冲区 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Generate session id | 数据设置 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Chat 消息触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：16
- 触发方式：Telegram 消息触发, Chat 消息触发

## 触发方式
- Telegram Trigger 触发
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：13
- 输出节点：1
- 分类：knowledge-rag
