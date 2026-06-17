## 简介
**Generate Visual Summary & Knowledge Graph Insights for Your Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4619

---

# Generate Visual Summary & Knowledge Graph Insights for Your Email


## 节点清单

| 节点 | 类型 |
|------|------|
| InfraNodus Question Generator | HTTP Request |
| Clean text and organize into statements | Code |
| Google Gemini Chat Model | OpenAI Chat Model |
| Was label provided? | IF 判断 |
| Should analyze snippets? | IF 判断 |
| Should analyze snippets from filtered emails? | IF 判断 |
| Filter emails by label | 过滤器 |
| Get Full Message Content | Email 发送 |
| Should use AI to filter emails further? | IF 判断 |
| Message text or snippet present? | 过滤器 |
| Classify Emails | 文本分类器 |
| Text field present? | IF 判断 |
| Aggregate from full email texts | 数据聚合 |
| Aggregate from email snippets | 数据聚合 |
| Wait before generating questions | 等待 |
| Send the graph link and summary via Telegram | Telegram |
| Send an insight question via Telegram | Telegram |
| Get Messages by Search Criteria | Email 发送 |
| User submits form | 表单触发器 |
| InfraNodus AI Summary & Graph Link | HTTP Request |
| Type of graph to build | Switch 路由 |
| InfraNodus Build a Social Knowledge Graph | HTTP Request |
| InfraNodus Build a Text Knowledge Graph | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Assign Processing Settings | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Gmail | Email 发送 |

## 触发方式
- User submits form 触发
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：27
- 触发节点：3
- 处理节点：15
- 输出节点：9
- 分类：workflow-automation
