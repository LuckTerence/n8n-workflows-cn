## 简介
**Automate LINE & Google Account Linking with OAuth2 Authentication**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Automate LINE & Google Account Linking with OAuth2。

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

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- LINE Webhook 触发
- Google Auth Callback 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：2
- 输出节点：5
- 分类：workflow-automation
