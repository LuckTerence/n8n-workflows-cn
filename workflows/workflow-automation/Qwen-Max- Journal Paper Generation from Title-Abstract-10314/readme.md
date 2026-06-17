# Qwen-Max: Journal Paper Generation from Title-Abstract

https://n8nworkflows.xyz/workflows/10314

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Extract Input Data | 数据设置 |
| Search CrossRef | HTTP Request |
| Search Semantic Scholar | HTTP Request |
| Search OpenAlex | HTTP Request |
| Merge Reference Sources | 数据合并 |
| Process References | Code |
| Prepare AI Context | 数据设置 |
| AI - Introduction | AI Agent |
| AI - Literature Review | AI Agent |
| AI - Methodology | AI Agent |
| AI - Results | AI Agent |
| AI - Discussion | AI Agent |
| AI - Conclusion | AI Agent |
| Merge All Sections | 数据合并 |
| Compile Document | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：13
- 输出节点：3
- 分类：workflow-automation
