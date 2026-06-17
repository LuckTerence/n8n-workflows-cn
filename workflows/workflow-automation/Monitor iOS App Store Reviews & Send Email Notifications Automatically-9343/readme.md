# Monitor iOS App Store Reviews & Send Email Notifications Automatically

https://n8nworkflows.xyz/workflows/9343

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Extract Reviews | Code |
| Any new reviews? | IF 判断 |
| App Config | 数据设置 |
| Fetch Reviews | HTTP Request |
| Filter latest Review | Code |
| Send notification | Email 发送 |
| False Case | 数据设置 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
