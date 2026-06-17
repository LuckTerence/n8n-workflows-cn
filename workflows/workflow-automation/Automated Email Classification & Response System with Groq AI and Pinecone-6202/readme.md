## 简介
**Automated Email Classification & Response System with Groq AI and Pinecone**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6202

---

# Automated Email Classification & Response System with Groq AI and Pinecone


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| Switch1 | Switch 路由 |
| Code | Code |
| Basic LLM Chain | LLM Chain |
| Groq Chat Model | Groq Chat Model |
| Groq Chat Model1 | Groq Chat Model |
| X | Twitter |
| Groq Chat Model2 | Groq Chat Model |
| Basic LLM Chain1 | LLM Chain |
| Groq Chat Model3 | Groq Chat Model |
| Code2 | Code |
| Switch | Switch 路由 |
| Pinecone Vector Store | Pinecone 向量存储 |
| Embeddings Cohere | Cohere Embeddings |
| When clicking ‘Execute workflow’ | 手动触发 |
| HTTP Request | HTTP Request |
| Extract from File | 从文件提取 |
| Code3 | Code |
| Pinecone Vector Store1 | Pinecone 向量存储 |
| Embeddings Cohere1 | Cohere Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| send email to team | Email 发送 |
| send reply to customer | Email 发送 |
| send to support team | Email 发送 |
| Send to customer | Email 发送 |
| rejection email | Email 发送 |
| to hr | Email 发送 |
| accepted confirm to candidate | Email 发送 |
| bill send to team | Email 发送 |
| TO SALES TEAM | Email 发送 |
| CLEAN AI AGENT OUTPUT | Code |
| RAG INQURY REPLY | AI Agent |
| Sentiment Analysis of feedback | sentimentAnalysis |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：34
- 触发节点：1
- 处理节点：22
- 输出节点：11
- 分类：workflow-automation
