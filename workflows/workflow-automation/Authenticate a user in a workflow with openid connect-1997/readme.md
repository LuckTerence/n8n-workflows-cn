## 简介
**Authenticate a user in a workflow with openid connect**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1997

---

# Authenticate a user in a workflow with openid connect


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



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
