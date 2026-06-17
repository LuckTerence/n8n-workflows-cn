## 简介
**Create a Branded AI-Powered Website Chatbot**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2786

---

# Create a Branded AI-Powered Website Chatbot


## 节点清单

| 节点 | 类型 |
|------|------|
| Window Buffer Memory | 记忆缓冲区 |
| Respond to Webhook | 响应 Webhook |
| OpenAI Chat Model | OpenAI Chat Model |
| Make Appointment | HTTP 工具 |
| Execute Workflow Trigger | 执行工作流触发器 |
| varResponse | 数据设置 |
| freeTimeSlots | Code |
| Get Events | HTTP Request |
| Get Availability | 工作流工具 |
| Send Message | 工作流工具 |
| Chat Trigger | Chat 触发器 |
| Switch | Switch 路由 |
| varMessageResponse | 数据设置 |
| Send Message1 | Outlook |
| AI Agent | AI Agent |
| If | IF 判断 |
| Respond With Initial Message | 响应 Webhook |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复。

Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：17
- 触发方式：Chat 消息触发

## 触发方式
- Execute Workflow Trigger 触发
- Chat Trigger 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：10
- 输出节点：5
- 分类：ai-agent
