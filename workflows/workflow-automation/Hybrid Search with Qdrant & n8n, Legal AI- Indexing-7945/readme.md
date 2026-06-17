## 简介
**Hybrid Search with Qdrant & n8n, Legal AI: Indexing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：29 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/7945

---

# Hybrid Search with Qdrant & n8n, Legal AI: Indexing


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Collection | qdrant |
| Check Collection Exists | qdrant |
| If | IF 判断 |
| Index Dataset from HuggingFace | 手动触发 |
| Split Them All Out | 数据拆分 |
| Get Dataset Splits | HTTP Request |
| Divide Per Row | 数据拆分 |
| Loop Over Batches | 分批处理 |
| Aggregate a Batch | 数据聚合 |
| Upsert Points | qdrant |
| Limit | 数据限制 |
| Merge | 数据合并 |
| Sum them Up | 文本摘要 |
| Get the Average Text Length | 数据设置 |
| Loop Over Batches1 | 分批处理 |
| Upsert Points1 | qdrant |
| Create Collection1 | qdrant |
| Check Collection Exists1 | qdrant |
| If1 | IF 判断 |
| Merge1 | 数据合并 |
| Split Out | 数据拆分 |
| Get OpenAI embeddings | HTTP Request |
| Get Dataset Rows (Pagination) | HTTP Request |
| Restructure for Deduplicating | 数据设置 |
| Restructure for Batching | 数据设置 |
| Deduplicate Texts | 文本摘要 |
| Calculate #words in Each Text | 数据设置 |
| Edit Fields | 数据设置 |
| Aggregate a Batch to Embed | 数据聚合 |
| Aggregate a Batch to Upsert | 数据聚合 |

## 触发方式
- Index Dataset from HuggingFace 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：26
- 输出节点：3
- 分类：workflow-automation
