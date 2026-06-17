# Automate LINE & Google Account Linking with OAuth2 Authentication

https://n8nworkflows.xyz/workflows/10950

## 节点清单

| 节点 | 类型 |
|------|------|
| Redirect to LINE OA | 响应 Webhook |
| Get Google Access Token | HTTP Request |
| Get Google User Info | HTTP Request |
| Send Completion Message to LINE | HTTP Request |
| If Follow Event | IF 判断 |
| Create Google Auth URL | 数据设置 |
| Send Auth Link to LINE | HTTP Request |
| LINE Webhook | Webhook |
| Google Auth Callback | Webhook |

## 触发方式
- LINE Webhook 触发
- Google Auth Callback 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：2
- 输出节点：5
- 分类：workflow-automation
