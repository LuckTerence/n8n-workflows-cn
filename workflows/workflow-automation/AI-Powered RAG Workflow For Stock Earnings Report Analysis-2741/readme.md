## 简介
**AI-Powered RAG Workflow For Stock Earnings Report Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Pinecone/Google Sheets/Google Docs/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2741

---

# AI-Powered RAG Workflow For Stock Earnings Report Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Pinecone Vector Store | Pinecone 向量存储 |
| Embeddings Google Gemini | Google Gemini Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Loop Over Items | 分批处理 |
| When clicking ‘Test workflow’ | 手动触发 |
| AI Agent | AI Agent |
| Vector Store Tool | 向量存储工具 |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| OpenAI Chat Model | OpenAI Chat Model |
| Pinecone Vector Store (Retrieval) | Pinecone 向量存储 |
| Save Report to Google Docs | Google Docs |
| Embeddings Google Gemini (retrieval) | Google Gemini Embeddings |
| List Of Files To Load (Google Sheets) | Google Sheets |
| Download File From Google Drive | Google Drive |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：workflow-automation
