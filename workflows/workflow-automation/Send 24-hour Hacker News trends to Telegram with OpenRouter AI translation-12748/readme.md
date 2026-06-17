## 简介
**Send 24-hour Hacker News trends to Telegram with OpenRouter AI translation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/12748

---

# Send 24-hour Hacker News trends to Telegram with OpenRouter AI translation


## 节点清单

| 节点 | 类型 |
|------|------|
| Filter | 过滤器 |
| Schedule Trigger | 定时触发器 |
| Send a text message | Telegram |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Algolia parameters | Code |
| Recalculate popularity score | Code |
| Translate | AI Agent |
| Request Algolia | HTTP Request |
| Merge translation results | Code |
| Combine message templates | Code |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
