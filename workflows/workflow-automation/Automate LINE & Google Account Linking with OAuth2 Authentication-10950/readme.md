## 简介
**Automate LINE & Google Account Linking with OAuth2 Authentication**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10950

---

# Automate LINE & Google Account Linking with OAuth2 Authentication


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
