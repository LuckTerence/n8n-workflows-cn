## 简介
**Complete Mandrill Email API Integration for AI Tools (90 Operations)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5620

---

# Complete Mandrill Email API Integration for AI Tools (90 Operations)


## 节点清单

| 节点 | 类型 |
|------|------|
| Mandrill MCP Server | MCP 触发器 |
| Create Export 5 | HTTP Request 工具 |
| Create Export 6 | HTTP Request 工具 |
| Create Export 7 | HTTP Request 工具 |
| Create Export 8 | HTTP Request 工具 |
| Create Export 9 | HTTP Request 工具 |
| Create Inbound 9 | HTTP Request 工具 |
| Create Inbound 10 | HTTP Request 工具 |
| Create Inbound 11 | HTTP Request 工具 |
| Create Inbound 12 | HTTP Request 工具 |
| Create Inbound 13 | HTTP Request 工具 |
| Create Inbound 14 | HTTP Request 工具 |
| Create Inbound 15 | HTTP Request 工具 |
| Create Inbound 16 | HTTP Request 工具 |
| Create Inbound 17 | HTTP Request 工具 |
| Create Ip 13 | HTTP Request 工具 |
| Create Ip 14 | HTTP Request 工具 |
| Create Ip 15 | HTTP Request 工具 |
| Create Ip 16 | HTTP Request 工具 |
| Create Ip 17 | HTTP Request 工具 |
| Create Ip 18 | HTTP Request 工具 |
| Create Ip 19 | HTTP Request 工具 |
| Create Ip 20 | HTTP Request 工具 |
| Create Ip 21 | HTTP Request 工具 |
| Create Ip 22 | HTTP Request 工具 |
| Create Ip 23 | HTTP Request 工具 |
| Create Ip 24 | HTTP Request 工具 |
| Create Ip 25 | HTTP Request 工具 |
| Create Message 11 | HTTP Request 工具 |
| Create Message 12 | HTTP Request 工具 |
| Create Message 13 | HTTP Request 工具 |
| Create Message 14 | HTTP Request 工具 |
| Create Message 15 | HTTP Request 工具 |
| Create Message 16 | HTTP Request 工具 |
| Create Message 17 | HTTP Request 工具 |
| Create Message 18 | HTTP Request 工具 |
| Create Message 19 | HTTP Request 工具 |
| Create Message 20 | HTTP Request 工具 |
| Create Message 21 | HTTP Request 工具 |
| Create Metadata 4 | HTTP Request 工具 |
| Create Metadata 5 | HTTP Request 工具 |
| Create Metadata 6 | HTTP Request 工具 |
| Create Metadata 7 | HTTP Request 工具 |
| Create Reject 3 | HTTP Request 工具 |
| Create Reject 4 | HTTP Request 工具 |
| Create Reject 5 | HTTP Request 工具 |
| Create Sender 7 | HTTP Request 工具 |
| Create Sender 8 | HTTP Request 工具 |
| Create Sender 9 | HTTP Request 工具 |
| Create Sender 10 | HTTP Request 工具 |
| Create Sender 11 | HTTP Request 工具 |
| Create Sender 12 | HTTP Request 工具 |
| Create Sender 13 | HTTP Request 工具 |
| Create Subaccount 7 | HTTP Request 工具 |
| Create Subaccount 8 | HTTP Request 工具 |
| Create Subaccount 9 | HTTP Request 工具 |
| Create Subaccount 10 | HTTP Request 工具 |
| Create Subaccount 11 | HTTP Request 工具 |
| Create Subaccount 12 | HTTP Request 工具 |
| Create Subaccount 13 | HTTP Request 工具 |
| Create Tag 5 | HTTP Request 工具 |
| Create Tag 6 | HTTP Request 工具 |
| Create Tag 7 | HTTP Request 工具 |
| Create Tag 8 | HTTP Request 工具 |
| Create Tag 9 | HTTP Request 工具 |
| Create Template 8 | HTTP Request 工具 |
| Create Template 9 | HTTP Request 工具 |
| Create Template 10 | HTTP Request 工具 |
| Create Template 11 | HTTP Request 工具 |
| Create Template 12 | HTTP Request 工具 |
| Create Template 13 | HTTP Request 工具 |
| Create Template 14 | HTTP Request 工具 |
| Create Template 15 | HTTP Request 工具 |
| Create Url 6 | HTTP Request 工具 |
| Create Url 7 | HTTP Request 工具 |
| Create Url 8 | HTTP Request 工具 |
| Create Url 9 | HTTP Request 工具 |
| Create Url 10 | HTTP Request 工具 |
| Create Url 11 | HTTP Request 工具 |
| Create User 4 | HTTP Request 工具 |
| Create User 5 | HTTP Request 工具 |
| Create User 6 | HTTP Request 工具 |
| Create User 7 | HTTP Request 工具 |
| Create Webhook 5 | HTTP Request 工具 |
| Create Webhook 6 | HTTP Request 工具 |
| Create Webhook 7 | HTTP Request 工具 |
| Create Webhook 8 | HTTP Request 工具 |
| Create Webhook 9 | HTTP Request 工具 |
| Create Whitelist 3 | HTTP Request 工具 |
| Create Whitelist 4 | HTTP Request 工具 |
| Create Whitelist 5 | HTTP Request 工具 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：91
- 触发方式：手动或子流程调用

## 触发方式
- Mandrill MCP Server 触发

## 统计
- 节点总数：91
- 触发节点：1
- 处理节点：0
- 输出节点：90
- 分类：devops
