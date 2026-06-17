# Clone NocoDB tables and data to another base

https://n8nworkflows.xyz/workflows/15373

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Config | 数据设置 |
| Create NocoDB Table | HTTP Request |
| Create Tables | 分批处理 |
| Prepare fields data for Insert | 数据设置 |
| Copy rows to new tables | 分批处理 |
| Fetch tables records | HTTP Request |
| Get Source Table Metadata | HTTP Request |
| Split tables | 数据拆分 |
| Fetch tables records1 | HTTP Request |
| Copy data over? | Switch 路由 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
