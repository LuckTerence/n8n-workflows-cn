# Create Snapshot of Contabo VPS instances on a daily basis

https://n8nworkflows.xyz/workflows/2403

## 节点清单

| 节点 | 类型 |
|------|------|
| Set snapshot attributes | 数据设置 |
| Schedule Trigger | 定时触发器 |
| When clicking ‘Test workflow’ | 手动触发 |
| Credential | 数据设置 |
| Authorization | HTTP Request |
| List instances | HTTP Request |
| Split Out | 数据拆分 |
| UUID | HTTP Request |
| TRACE ID | HTTP Request |
| List snapshots | HTTP Request |
| UUID1 | HTTP Request |
| Merge | 数据合并 |
| get Date & Time | 日期时间 |
| Delete existing snapshot | HTTP Request |
| Create a new snapshot | HTTP Request |
| Create a new snapshot1 | HTTP Request |
| UUID2 | HTTP Request |
| UUID3 | HTTP Request |
| UUID4 | HTTP Request |
| Formatted Date | 日期时间 |
| Whether snapshot there is no snapshot | IF 判断 |
| set snapshot attributes | 数据设置 |

## 触发方式
- Schedule Trigger 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：8
- 输出节点：12
- 分类：workflow-automation
