## 简介
**Build an AI-Powered Tech Radar Advisor with SQL DB, RAG, and Routing Agents**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3151

---

# Build an AI-Powered Tech Radar Advisor with SQL DB, RAG, and Routing Agents


## 节点清单

| 节点 | 类型 |
|------|------|
| Download Doc File From Google Drive | Google Drive |
| Doc File Data Loader | 文档加载器 |
| Cron | 定时触发器 |
| MySQL -delete all data | MySQL |
| MySQL - insert all from sheets | MySQL |
| Google Sheets - Tech Radar | Google Sheets |
| Code - Transform table into rows | Code |
| Google Docs - Update GDoc | Google Docs |
| Google Drive - Doc File Updated | Google Drive 触发器 |
| Content - Recursive Character Text Splitter | 文本分割器 |
| Google Sheets - Read TechRadar | Google Sheets |
| Code - Simplify Mapping to Original Query | Code |
| Codes - Simplify Mapping to Original Query | Code |
| Execute Workflow - Sql Agent | 执行工作流 |
| Execute Workflow - RAG Agent | 执行工作流 |
| AI Agent - Output Guardrail | AI Agent |
| LLM - Determine - Agent Input Router | LLM Chain |
| When Executed by Another Workflow | 执行工作流触发器 |
| 1_Get DB Schema and Tables List | mySqlTool |
| 2_Get Table Definition | mySqlTool |
| 3_Execute actual query | mySqlTool |
| AI Agent -DB Sql Agent | AI Agent |
| Pinecone Vector Store (Retrieval) | Pinecone 向量存储 |
| 4_RagTool | 向量存储工具 |
| AI Agent - RAG | AI Agent |
| Embeddings - Tech Radar Data Embedding | Google Gemini Embeddings |
| Pinecone - Vector Store for Embedding Content | Pinecone 向量存储 |
| Retrieve Embeddings - Tech Radar Vector DB | Google Gemini Embeddings |
| AI Agent - Retrieval | OpenAI Chat Model |
| AI Chat Model - Claude 3.5 Sonnet | OpenAI Chat Model |
| AI Chat Model - QwQ 32b | Groq Chat Model |
| AI Chatmodel - Deepseek 32B | Groq Chat Model |
| AI Chat Model - llama3-8b | Groq Chat Model |
| API Response - Respond to Webhook | 响应 Webhook |
| API Request - Webhook | Webhook |
| Determine if  is 'RAG' | IF 判断 |
| User Conversation history | 记忆缓冲区 |

## 触发方式
- Cron 触发
- Google Drive - Doc File Updated 触发
- When Executed by Another Workflow 触发
- API Request - Webhook 触发

## 统计
- 节点总数：37
- 触发节点：4
- 处理节点：32
- 输出节点：1
- 分类：knowledge-rag
