## 简介
**SMS Messaging API Integration for AI Agents with BulkSMS**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5548

---

# SMS Messaging API Integration for AI Agents with BulkSMS


## 节点清单

| 节点 | 类型 |
|------|------|
| BulkSMS JSON REST MCP Server | MCP 触发器 |
| List Blocked Numbers | HTTP Request 工具 |
| Block Phone Number | HTTP Request 工具 |
| Transfer Account Credits | HTTP Request 工具 |
| Retrieve Message History | HTTP Request 工具 |
| Send New Message | HTTP Request 工具 |
| Send Quick Message | HTTP Request 工具 |
| View Message Details | HTTP Request 工具 |
| List Related Messages | HTTP Request 工具 |
| Retrieve User Profile | HTTP Request 工具 |
| Generate Attachment Upload URL | HTTP Request 工具 |
| List All Webhooks | HTTP Request 工具 |
| Register New Webhook | HTTP Request 工具 |
| Remove Webhook | HTTP Request 工具 |
| Get Webhook Details | HTTP Request 工具 |
| Update Webhook Settings | HTTP Request 工具 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：手动或子流程调用

## 触发方式
- BulkSMS JSON REST MCP Server 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：0
- 输出节点：15
- 分类：ai-agent
