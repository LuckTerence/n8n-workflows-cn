# Auto-Send Vtiger Support Tickets to Telegram (with Status Update)

https://n8nworkflows.xyz/workflows/6329

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger Every n Minutes | 定时触发器 |
| VtigerCRM get Tickets | vtigerNode |
| If there's a data returned | IF 判断 |
| Send a Ticket detail to Telegram | Telegram |
| VtigerCRM Update Ticket Status | vtigerNode |
| No Operation, do nothing | 空操作 |

## 触发方式
- Schedule Trigger Every n Minutes 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
