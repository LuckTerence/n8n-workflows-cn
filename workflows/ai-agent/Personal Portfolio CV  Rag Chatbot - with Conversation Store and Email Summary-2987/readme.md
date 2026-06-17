## 简介
**Personal Portfolio CV  Rag Chatbot - with Conversation Store and Email Summary**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Pinecone/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/2987

---

# Personal Portfolio CV  Rag Chatbot - with Conversation Store and Email Summary


## 节点清单

| 节点 | 类型 |
|------|------|
| Embeddings Google Gemini | Google Gemini Embeddings |
| Schedule Trigger | 定时触发器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Google Drive - Resume CV File Created | Google Drive 触发器 |
| Google Drive - Resume CV File Updated | Google Drive 触发器 |
| Download CV File From Google Drive | Google Drive |
| Pinecone - Vector Store forr CV Content | Pinecone 向量存储 |
| CV File Data Loader | 文档加载器 |
| CV content - Recursive Character Text Splitter | 文本分割器 |
| Chat API - webhook | Webhook |
| Personal CV AI Agent Assistant | AI Agent |
| Chat API Response - Webhook | 响应 Webhook |
| Chat Memory -  Window Buffer | 记忆缓冲区 |
| Resume lookup : Vector Store Tool | 向量存储工具 |
| Resume Vector Store (Retrieval) | Pinecone 向量存储 |
| Resume Embeddings Google Gemini (retrieval) | Google Gemini Embeddings |
| Resume Google Gemini Chat Model (retrieval) | OpenAI Chat Model |
| Save Conversation API - Webhook | Webhook |
| Save Conversation - NocoDB | NocoDB |
| Save Conversation API Webhook - Response | 响应 Webhook |
| NocoDB - get all todays conversation | NocoDB |
| Group Conversation By Unique Session + Email - Code | Code |
| Format HTML Display  For email | HTML |
| Send Report To Gmail | Email 发送 |

## 触发方式
- Schedule Trigger 触发
- Google Drive - Resume CV File Created 触发
- Google Drive - Resume CV File Updated 触发
- Chat API - webhook 触发
- Save Conversation API - Webhook 触发

## 统计
- 节点总数：24
- 触发节点：5
- 处理节点：16
- 输出节点：3
- 分类：ai-agent
