# Notify on menu orders via ntfy and Home Assistant TTS with daily BAC tracking

https://n8nworkflows.xyz/workflows/14487

## 节点清单

| 节点 | 类型 |
|------|------|
| When Order Received | Webhook |
| Calculate Alcohol and Format Order | Code |
| Log Order to Database | 数据表 |
| Read Today's Orders | 数据表 |
| Calculate Cumulative BAC | Code |
| Send Ntfy Notification | HTTP Request |
| Announce Order with Home Assistant | homeAssistant |

## 触发方式
- When Order Received 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
