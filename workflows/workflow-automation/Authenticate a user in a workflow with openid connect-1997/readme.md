# Authenticate a user in a workflow with openid connect

https://n8nworkflows.xyz/workflows/1997

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Code | Code |
| user info | HTTP Request |
| send back login page | 响应 Webhook |
| IF token is present | IF 判断 |
| Welcome page | HTML |
| send back welcome page | 响应 Webhook |
| IF user info ok | IF 判断 |
| login form | HTML |
| Set variables : auth, token, userinfo, client id, scope | 数据设置 |
| IF we have code in URI and not in PKCE mode | IF 判断 |
| get access_token from /token endpoint with code | HTTP Request |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
