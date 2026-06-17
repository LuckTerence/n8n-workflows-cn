## 简介
**Generate B2B Lead Opportunities from Websites with Brightdata & OpenRouter AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：15 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/8076

---

# Generate B2B Lead Opportunities from Websites with Brightdata & OpenRouter AI


## 节点清单

| 节点 | 类型 |
|------|------|
| parameters | 数据设置 |
| extract url | Code |
| scrap urls | brightData |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| scrap urls1 | brightData |
| HTML cleaner | HTML |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Structured Output Parser2 | 结构化输出解析器 |
| OpenRouter Chat Model3 | OpenRouter Chat Model |
| merge pages | Code |
| clean list | Code |
| When chat message received | Chat 触发器 |
| Find best pages | AI Agent |
| Identify business opportunities | AI Agent |
| de-dupe | AI Agent |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：15
- 输出节点：0
- 分类：workflow-automation
