## 简介
**Self-Hosted JWT Authentication System with Data Tables and Token Management**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：59 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/9660

---

# Self-Hosted JWT Authentication System with Data Tables and Token Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate Salt | 加密 |
| Hash Password | 加密 |
| Process login webhook | 数据设置 |
| Get User | 数据表 |
| Extract Salt & Hash | Code |
| Hash Input Password | 加密 |
| Sign Access Token | 加密 |
| Sign Refresh Token | 加密 |
| Format JWT Tokens | Code |
| Merge JWT Tokens | 数据合并 |
| Hash Refresh Token for Storage | 加密 |
| Parse JWT | Code |
| Verify HMAC Signature | 加密 |
| Compare Signatures | Code |
| Create User | 数据表 |
| Registration Webhook | Webhook |
| Format Password & Salt | Code |
| Format User Data | Code |
| Error Registration Response | 响应 Webhook |
| Validate Registration Request | Code |
| Registration Successful | 响应 Webhook |
| If User Exists | IF 判断 |
| User Not Found | 响应 Webhook |
| Code in JavaScript | Code |
| Update User Refresh Token | 数据表 |
| Store Refresh Token | 数据表 |
| Merge | 数据合并 |
| Verify Access Token | Webhook |
| When Executed by Another Workflow | 执行工作流触发器 |
| Refresh Access Token | Webhook |
| Parse Refresh Token | Code |
| Verify Signature | 加密 |
| Compare Refresh Token Signature | Code |
| Hash Refresh Token For DB Lookup | 加密 |
| If Refresh Token Exists | 数据表 |
| If Refresh Token Is Valid | IF 判断 |
| Create Access Token Payload | Code |
| Format Access Token JWT | Code |
| Return New Access Token | 响应 Webhook |
| Session Expired | 响应 Webhook |
| Parse Register Request | 数据设置 |
| Login Successful | 响应 Webhook |
| Login Credentials Invalid Response | 响应 Webhook |
| Process Verify Token Webhook | 数据设置 |
| Verify Input | Code |
| Verify Password | Code |
| Create JWT Payload | Code |
| Process Refresh Token | 数据设置 |
| Sign New Access Token | 加密 |
| If Username Is Available | IF 判断 |
| Get User By Username | 数据表 |
| Username Taken Error | 响应 Webhook |
| Registration Request Invalid Error | 响应 Webhook |
| If Email Is Available | IF 判断 |
| Get User By Email | 数据表 |
| Email Taken Error | 响应 Webhook |
| Login Webhook | Webhook |
| Bad Request | 响应 Webhook |
| Access Token Valid | 响应 Webhook |
| Access Token Invalid | 响应 Webhook |
| SET ACCESS AND REFRESH SECRET | 数据设置 |
| SET ACCESS AND REFRESH SECRET1 | 数据设置 |
| SET ACCESS AND REFRESH SECRET2 | 数据设置 |

## 触发方式
- Registration Webhook 触发
- Verify Access Token 触发
- When Executed by Another Workflow 触发
- Refresh Access Token 触发
- Login Webhook 触发

## 统计
- 节点总数：63
- 触发节点：5
- 处理节点：45
- 输出节点：13
- 分类：workflow-automation
