## 简介
**AI Agents can Create, Enrich leads with this Lemlist Tool MCP Server**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5233

---

# AI Agents can Create, Enrich leads with this Lemlist Tool MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| Lemlist Tool MCP Server | MCP 触发器 |
| Get many activities | Lemlist 工具 |
| Get many campaigns | Lemlist 工具 |
| Get campaign stats | Lemlist 工具 |
| Fetches a previously completed enrichment | Lemlist 工具 |
| Enrich a lead using an email or LinkedIn URL | Lemlist 工具 |
| Enrich a person using an email or LinkedIn URL | Lemlist 工具 |
| Create a lead | Lemlist 工具 |
| Delete a lead | Lemlist 工具 |
| Get a lead | Lemlist 工具 |
| Unsubscribe a lead | Lemlist 工具 |
| Get a team | Lemlist 工具 |
| Get team credits | Lemlist 工具 |
| Add an email to an unsubscribe list | Lemlist 工具 |
| Delete an email from an unsubscribe list | Lemlist 工具 |
| Get many unsubscribed emails | Lemlist 工具 |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

手动触发，通过 邮箱 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

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
- Lemlist Tool MCP Server 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：15
- 输出节点：0
- 分类：ai-agent
