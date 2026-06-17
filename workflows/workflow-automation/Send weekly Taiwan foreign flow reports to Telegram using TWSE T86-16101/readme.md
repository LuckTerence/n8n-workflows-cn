# Send weekly Taiwan foreign flow reports to Telegram using TWSE T86

https://n8nworkflows.xyz/workflows/16101

## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Report Trigger | 定时触发器 |
| Set Report Config Parameters | 数据设置 |
| Calculate Trading Days | Code |
| Fetch TWSE Daily Data | HTTP Request |
| Aggregate Weekly Foreign Net | Code |
| Format Telegram Message | Code |
| Send Report to Telegram | Telegram |

## 触发方式
- Weekly Report Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
