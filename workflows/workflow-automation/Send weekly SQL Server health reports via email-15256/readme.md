# Send weekly SQL Server health reports via email

https://n8nworkflows.xyz/workflows/15256

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| top slow queries | microsoftSql |
|  missing indexes | microsoftSql |
| index fragmentation | microsoftSql |
| blocking & wait stats | microsoftSql |
| Merge | 数据合并 |
| Code in JavaScript | Code |
| Send email | Email 发送 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
