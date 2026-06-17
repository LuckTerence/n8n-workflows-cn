# Manage job records via webhook REST API with PostgreSQL

https://n8nworkflows.xyz/workflows/16081

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Switch | Switch 路由 |
| Get All Jobs | PostgreSQL |
| Create Job | PostgreSQL |
| Update Job | PostgreSQL |
| Delete Job | PostgreSQL |
| Return Success Response | 响应 Webhook |
| Return Job List | 响应 Webhook |
| Error During Fetching Jobs | 响应 Webhook |
| Error during job creation | 响应 Webhook |
| Error during job details update | 响应 Webhook |
| Error during job deletion | 响应 Webhook |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：5
- 输出节点：6
- 分类：workflow-automation
