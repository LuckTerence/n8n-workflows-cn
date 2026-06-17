# Recipe Recommendations with Qdrant and Mistral

https://n8nworkflows.xyz/workflows/2333

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Test workflow" | 手动触发 |
| Get This Week's Menu | HTTP Request |
| Extract Available Courses | Code |
| Extract Server Data | HTML |
| Get Course Metadata | 数据设置 |
| Get Recipe | HTTP Request |
| Embeddings Mistral Cloud | embeddingsMistralCloud |
| Default Data Loader | 文档加载器 |
| Merge Course & Recipe | 数据合并 |
| Prepare Documents | 数据设置 |
| Recursive Character Text Splitter | 文本分割器 |
| Chat Trigger | Chat 触发器 |
| Extract Recipe Details | HTML |
| Qdrant Recommend API | 工作流工具 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Get Tool Response | 数据设置 |
| Wait for Rate Limits | 等待 |
| Get Mistral Embeddings | HTTP Request |
| Use Qdrant Recommend API | HTTP Request |
| Get Recipes From DB | Code |
| Save Recipes to DB | Code |
| AI Agent | AI Agent |
| Qdrant Vector Store | Qdrant 向量存储 |

## 触发方式
- When clicking "Test workflow" 触发
- Chat Trigger 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：24
- 触发节点：3
- 处理节点：17
- 输出节点：4
- 分类：workflow-automation
