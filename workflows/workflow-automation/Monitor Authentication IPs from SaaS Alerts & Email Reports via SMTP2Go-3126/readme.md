# Monitor Authentication IPs from SaaS Alerts & Email Reports via SMTP2Go

https://n8nworkflows.xyz/workflows/3126

## 节点清单

| 节点 | 类型 |
|------|------|
| GET Events - Login Successful | HTTP Request |
| Send Email Upon Completion (SMTP2Go) | HTTP Request |
| Remove Duplicate IPs | 去重 |
| Convert CSV to Base64 | moveBinaryData |
| Convert to CSV | 转换为文件 |
| Filter IP Information | 数据设置 |
| Combine all Authentication Events | 数据合并 |
| GET Events - OAuth Authentication | HTTP Request |
| GET Events - Office365 Shell WCSS | HTTP Request |
| Set Date and Form Variables | 数据设置 |
| Authentication Request Form | 表单触发器 |

## 触发方式
- Authentication Request Form 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
