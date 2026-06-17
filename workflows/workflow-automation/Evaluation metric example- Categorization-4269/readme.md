# Evaluation metric example: Categorization

https://n8nworkflows.xyz/workflows/4269

## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Check categorization | 数据设置 |
| Match webhook format | 数据设置 |
| Webhook | Webhook |
| When fetching a dataset row | evaluationTrigger |
| Respond to Webhook | 响应 Webhook |
| Evaluating? | 条件评估 |
| Set metrics | 条件评估 |

## 触发方式
- Webhook 触发
- When fetching a dataset row 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
