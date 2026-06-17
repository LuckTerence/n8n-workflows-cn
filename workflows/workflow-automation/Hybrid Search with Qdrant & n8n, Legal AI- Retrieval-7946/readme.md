# Hybrid Search with Qdrant & n8n, Legal AI: Retrieval

https://n8nworkflows.xyz/workflows/7946

## 节点清单

| 节点 | 类型 |
|------|------|
| Index Dataset from HuggingFace | 手动触发 |
| Split Them All Out | 数据拆分 |
| Get Dataset Splits | HTTP Request |
| Divide Per Row | 数据拆分 |
| Keep Test Split | 过滤器 |
| Get Test Queries | HTTP Request |
| Query Points | qdrant |
| Merge | 数据合并 |
| Loop Over Items | 分批处理 |
| Keep Questions with Answers in the Dataset | 过滤器 |
| Keep Questions & IDs | 数据设置 |
| Aggregate Evals | 数据聚合 |
| Percentage of isHits in Evals | 数据设置 |
| isHit = If we Found the Correct Answer | 数据设置 |

## 触发方式
- Index Dataset from HuggingFace 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
