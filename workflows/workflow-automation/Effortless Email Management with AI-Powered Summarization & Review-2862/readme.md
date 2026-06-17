## 简介
**Effortless Email Management with AI-Powered Summarization & Review**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2862

---

# Effortless Email Management with AI-Powered Summarization & Review


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| Markdown | Markdown |
| Send Email | Email 发送 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Email Summarization Chain | chainSummarization |
| Write email | AI Agent |
| OpenAI | OpenAI Chat Model |
| Gmail | Email 发送 |
| Text Classifier | 文本分类器 |
| Edit Fields | 数据设置 |
| When clicking ‘Test workflow’ | 手动触发 |
| Create collection | HTTP Request |
| Refresh collection | HTTP Request |
| Get folder | Google Drive |
| Download Files | Google Drive |
| Default Data Loader | 文档加载器 |
| Token Splitter | textSplitterTokenSplitter |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| DeepSeek Chat Model | lmChatDeepSeek |
| Email Reviewer | AI Agent |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：16
- 输出节点：5
- 分类：workflow-automation
