# Docker Registry Cleanup Workflow

https://n8nworkflows.xyz/workflows/2835

## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Manifest Digest | HTTP Request |
| Remove Old Tags | HTTP Request |
| Retrieve Image Tags | HTTP Request |
| List Images | HTTP Request |
| Extract Image Names | Code |
| Identify Tags to Remove | Code |
| Scheduled Trigger | 定时触发器 |
| Send Notification Email | Email 发送 |
| Split Tags | 数据拆分 |
| Filter Valid Tags | 过滤器 |
| Fetch Manifest Digest for Blob | HTTP Request |
| Update Fields | 数据设置 |
| Group Tags by Image | Code |
| Sort by Creation Date | 数据排序 |
| Send Failure Notification Email | Email 发送 |
| Execute Garbage Collection | SSH |

## 触发方式
- Scheduled Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：8
- 输出节点：7
- 分类：devops
