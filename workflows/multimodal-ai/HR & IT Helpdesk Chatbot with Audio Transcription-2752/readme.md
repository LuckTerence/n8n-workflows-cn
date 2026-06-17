## 简介
**HR & IT Helpdesk Chatbot with Audio Transcription**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2752

---

# HR & IT Helpdesk Chatbot with Audio Transcription


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| HTTP Request | HTTP Request |
| Extract from File | 从文件提取 |
| Create HR Policies | PGVector 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Telegram Trigger | Telegram 触发器 |
| Verify Message Type | Switch 路由 |
| OpenAI | OpenAI |
| Telegram1 | Telegram |
| Unsupported Message Type | Telegram |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| Answer questions with a vector store | 向量存储工具 |
| Postgres PGVector Store | PGVector 向量存储 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Telegram | Telegram |
| Edit Fields | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Telegram Trigger 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：15
- 输出节点：4
- 分类：multimodal-ai
