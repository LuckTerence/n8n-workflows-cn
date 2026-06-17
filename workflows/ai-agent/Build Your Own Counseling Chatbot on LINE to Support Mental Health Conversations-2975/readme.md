## 简介
**Build Your Own Counseling Chatbot on LINE to Support Mental Health Conversations**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2975

---

# Build Your Own Counseling Chatbot on LINE to Support Mental Health Conversations


## 节点清单

| 节点 | 类型 |
|------|------|
| Loading Animation | HTTP Request |
| ReplyMessage - Not supported | HTTP Request |
| AI Agent | AI Agent |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| ReplyMessage - Line | HTTP Request |
| Line Chatbot | Webhook |
| Check Message Type IsText? | IF 判断 |
| Format Reply | 数据设置 |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：Webhook 触发

## 触发方式
- Line Chatbot 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：ai-agent
