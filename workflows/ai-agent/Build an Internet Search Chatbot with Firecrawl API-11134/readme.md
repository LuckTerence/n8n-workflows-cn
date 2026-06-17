## 简介
**Build an Internet Search Chatbot with Firecrawl API**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11134

---

# Build an Internet Search Chatbot with Firecrawl API


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive search query | Webhook |
| Search the web (Firecrawl) | Firecrawl |
| Answer search query | 响应 Webhook |
| Terminate service flow | 空操作 |
| Receive chat message | Chat 触发器 |
| Query search server (HTTP) | HTTP Request |
| Reply to the user in the chat | 聊天 |
| Terminate interface flow | 空操作 |
| Format search response (Python) | Code |
| Define constants | 数据设置 |
| Manual Trigger | 手动触发 |
| Verify Firecrawl Account Credit Balance | Firecrawl |
| Terminate Monitor Flow | 空操作 |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复，Webhook 触发。

Webhook触发、Chat 消息触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：Webhook 触发, Chat 消息触发, 手动触发

## 触发方式
- Receive search query 触发
- Receive chat message 触发
- Manual Trigger 触发

## 统计
- 节点总数：13
- 触发节点：3
- 处理节点：7
- 输出节点：3
- 分类：ai-agent
