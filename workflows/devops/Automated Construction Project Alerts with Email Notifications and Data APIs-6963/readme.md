# Automated Construction Project Alerts with Email Notifications and Data APIs

https://n8nworkflows.xyz/workflows/6963

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Email Trigger | Email 读取 |
| Check Email Subject | IF 判断 |
| Extract Location Info | Code |
| Search Government Data | HTTP Request |
| Search Construction Sites | HTTP Request |
| Process Construction Data | Code |
| Check if Projects Found | IF 判断 |
| Generate Email Report | Code |
| Send Alert Email | Email 发送 |
| Send No Results Email | Email 发送 |
| Wait For Data | 等待 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：devops
