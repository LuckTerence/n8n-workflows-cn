## 简介
**Breakdown Documents into Study Notes using Templating MistralAI and Qdrant**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2339

---

# Breakdown Documents into Study Notes using Templating MistralAI and Qdrant


## 节点清单

| 节点 | 类型 |
|------|------|
| Local File Trigger | localFileTrigger |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Embeddings Mistral Cloud | embeddingsMistralCloud |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Mistral Cloud Chat Model1 | Mistral Chat Model |
| Prep Incoming Doc | 数据设置 |
| Settings | 数据设置 |
| Merge | 数据合并 |
| Get Doc Types | 数据设置 |
| Split Out Doc Types | 数据拆分 |
| For Each Doc Type... | 分批处理 |
| Item List Output Parser | outputParserItemList |
| Vector Store Retriever | retrieverVectorStore |
| Embeddings Mistral Cloud1 | embeddingsMistralCloud |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Mistral Cloud Chat Model2 | Mistral Chat Model |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| Mistral Cloud Chat Model3 | Mistral Chat Model |
| Discover | chainRetrievalQa |
| 2secs | 等待 |
| Get Generated Documents | 数据设置 |
| Generate | LLM Chain |
| Prep For AI | 数据设置 |
| To Binary | 转换为文件 |
| Export to Folder | 读写文件 |
| Get FileType | Switch 路由 |
| Import File | 读写文件 |
| Extract from PDF | 从文件提取 |
| Extract from DOCX | 从文件提取 |
| Extract from TEXT | 从文件提取 |
| Summarization Chain | chainSummarization |
| Qdrant Vector Store | Qdrant 向量存储 |
| Interview | LLM Chain |

## 触发方式
- Local File Trigger 触发

## 统计
- 节点总数：35
- 触发节点：1
- 处理节点：34
- 输出节点：0
- 分类：workflow-automation
