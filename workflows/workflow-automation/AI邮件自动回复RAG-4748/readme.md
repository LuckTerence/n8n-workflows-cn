## 简介
**AI邮件自动回复RAG**

RAG增强的邮件自动回复系统

> 分类：工作流自动化 | 适配等级：A（需替换Google Docs/Google Drive/Gmail/Notion/Pinecone)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/4748

---

# AI邮件自动回复RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Answer questions with a vector store | 向量存储工具 |
| Pinecone Vector Store1 | Pinecone 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Get Brand brief | 工作流工具 |
| Gmail Trigger | Gmail 触发器 |
| OpenAI Chat Model2 | OpenAI Chat Model |
| If | IF 判断 |
| Simple Memory | 记忆缓冲区 |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Gmail | Gmail |
| Search Information | AI Agent |
| Response writer | AI Agent |
| Set Data | 数据设置 |
| Google Drive Trigger | Google Drive 触发器 |
| Google Drive | Google Drive |
| Pinecone Vector Store | Pinecone 向量存储 |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| When Executed by Another Workflow | 执行工作流触发器 |
| Notion | Notion |
| Aggregate | 数据聚合 |
| Edit Fields | 数据设置 |
| Google Docs | Google Docs |
| Check if Question | LLM Chain |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

手动触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：27
- 触发方式：手动或子流程调用

## 触发方式
- Gmail Trigger 触发
- Google Drive Trigger 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：27
- 触发节点：3
- 处理节点：24
- 输出节点：0
- 分类：workflow-automation
