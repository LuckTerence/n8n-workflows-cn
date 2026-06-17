## 简介
**AI-Powered Email Automation for Business: Summarize & Respond with RAG**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2852

---

# AI-Powered Email Automation for Business: Summarize & Respond with RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| Markdown | Markdown |
| DeepSeek R1 | OpenAI Chat Model |
| Send Email | Email 发送 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Email Classifier | 文本分类器 |
| Email Summarization Chain | chainSummarization |
| Write email | AI Agent |
| Review email | LLM Chain |
| When clicking ‘Test workflow’ | 手动触发 |
| Create collection | HTTP Request |
| Refresh collection | HTTP Request |
| Get folder | Google Drive |
| Download Files | Google Drive |
| Default Data Loader | 文档加载器 |
| Token Splitter | textSplitterTokenSplitter |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Do nothing | 空操作 |
| OpenAI | OpenAI Chat Model |
| DeepSeek | OpenAI Chat Model |
| OpenAI 4-o-mini | OpenAI Chat Model |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：18
- 输出节点：4
- 分类：workflow-automation
