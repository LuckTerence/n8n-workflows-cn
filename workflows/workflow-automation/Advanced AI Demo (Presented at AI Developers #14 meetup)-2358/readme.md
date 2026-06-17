## 简介
**Advanced AI Demo (Presented at AI Developers #14 meetup)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Pinecone/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2358

---

# Advanced AI Demo (Presented at AI Developers #14 meetup)


## 节点清单

| 节点 | 类型 |
|------|------|
| Send message | Slack |
| Execute JavaScript | Code |
| Recursive Character Text Splitter | 文本分割器 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Embeddings OpenAI2 | OpenAI Embeddings |
| Vector Store Retriever | retrieverVectorStore |
| Download PDF | HTTP Request |
| PDFs to download | 空操作 |
| Read Pinecone Vector Store | Pinecone 向量存储 |
| Question and Answer Chain | chainRetrievalQa |
| Anthropic Chat Model | OpenAI Chat Model |
| Get calendar availability | HTTP 工具 |
| Appointment booking agent | AI Agent |
| Window Buffer Memory | 记忆缓冲区 |
| Insert into Pinecone vector store | Pinecone 向量存储 |
| Book appointment | HTTP 工具 |
| When chat message received | Chat 触发器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Add automation label | Email 发送 |
| On new email to nathan's inbox | Gmail 触发器 |
| Add music label | Email 发送 |
| Assign label with AI | 文本分类器 |
| Webhook | Webhook |
| Whether email contains n8n | IF 判断 |



## 功能说明

Advanced AI Demo (Presented at AI Developers #14 m（AI 增强)Chat 消息触发、Webhook 触发，通过 邮箱 + HTTP API 实现自动化。

Webhook触发、Chat 消息触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：Chat 消息触发, Webhook 触发

## 触发方式
- When chat message received 触发
- On new email to nathan's inbox 触发
- Webhook 触发

## 统计
- 节点总数：26
- 触发节点：3
- 处理节点：17
- 输出节点：6
- 分类：workflow-automation
