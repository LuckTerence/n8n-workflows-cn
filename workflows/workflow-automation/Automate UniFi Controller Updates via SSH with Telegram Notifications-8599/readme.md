# Automate UniFi Controller Updates via SSH with Telegram Notifications

https://n8nworkflows.xyz/workflows/8599

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| HTTP Request | HTTP Request |
| Extract Codename + Date + Time Comparison | Code |
| If: Changed within 24h? | IF 判断 |
| Update package lists | SSH |
| Upgrade UniFi | SSH |
| Message a model | OpenAI |
| Notify via Telegram | Telegram |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
