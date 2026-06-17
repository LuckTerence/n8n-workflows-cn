## 简介
**Build an On-Premises AI Kaggle Competition Assistant with Qdrant RAG and Ollama**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：20 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/3967

---

# Build an On-Premises AI Kaggle Competition Assistant with Qdrant RAG and Ollama


## 节点清单

| 节点 | 类型 |
|------|------|
| Local File Trigger | localFileTrigger |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Settings | 数据设置 |
| Merge | 数据合并 |
| Get FileType | Switch 路由 |
| Import File | 读写文件 |
| Extract from TEXT | 从文件提取 |
| Summarization Chain | chainSummarization |
| Qdrant Vector Store | Qdrant 向量存储 |
| Markdown | Markdown |
| Embeddings Ollama | Ollama Embeddings |
| Ollama Summarizer | lmOllama |
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Vector Store Tool | 向量存储工具 |
| Window Buffer Memory | 记忆缓冲区 |
| Qdrant Vector Store2 | Qdrant 向量存储 |
| Ollama Chat Model3 | Ollama Chat Model |
| Embeddings Ollama2 | Ollama Embeddings |
| Ollama Chat Model4 | Ollama Chat Model |

## 触发方式
- Local File Trigger 触发
- When chat message received 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：19
- 输出节点：0
- 分类：knowledge-rag
