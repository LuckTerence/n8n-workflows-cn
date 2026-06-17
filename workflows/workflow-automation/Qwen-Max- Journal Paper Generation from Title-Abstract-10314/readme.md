## 简介
**Qwen-Max: Journal Paper Generation from Title-Abstract**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10314

---

# Qwen-Max: Journal Paper Generation from Title-Abstract


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
