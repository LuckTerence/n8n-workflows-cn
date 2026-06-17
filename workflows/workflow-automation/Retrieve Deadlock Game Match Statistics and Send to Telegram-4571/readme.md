# Retrieve Deadlock Game Match Statistics and Send to Telegram

https://n8nworkflows.xyz/workflows/4571

## 节点清单

| 节点 | 类型 |
|------|------|
| Send Telegram Message | Telegram |
| Fetch Profile HTML | HTTP Request |
| Extract Match ID | Function |
| Fetch Match HTML | HTTP Request |
| Parse Players | Function |
| Format Message | Function |
| Telegram Trigger | Telegram 触发器 |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
