## 简介
**Chat with News Articles using AI Analysis in Telegram with Vector Search**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：21 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10996

---

# Chat with News Articles using AI Analysis in Telegram with Vector Search


## 节点清单

| 节点 | 类型 |
|------|------|
| Send a document | Telegram |
| Structured Output Parser1 | 结构化输出解析器 |
| VLM Agent2 | OpenAI Chat Model |
| VLM Agent3 | OpenAI Chat Model |
| Split Out | 数据拆分 |
| HTTP Request1 | HTTP Request |
| No Operation, do nothing1 | 空操作 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Insert Data to Store | vectorStoreInMemory |
| Query Data Tool | vectorStoreInMemory |
| AI Agent | AI Agent |
| Code | Code |
| Check Whether URL | IF 判断 |
| Listen to Telegram for Link | Telegram 触发器 |
| Rename Link Field | 数据设置 |
| VLM Run Highlighter | AI Agent |
| Check URLs Validity | IF 判断 |
| Covert to Text File | 转换为文件 |
| OpenAI Chat Model | OpenAI Chat Model |
| Send a Reply | Telegram |
| Start Asking | Telegram |

## 触发方式
- Listen to Telegram for Link 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：17
- 输出节点：4
- 分类：knowledge-rag
