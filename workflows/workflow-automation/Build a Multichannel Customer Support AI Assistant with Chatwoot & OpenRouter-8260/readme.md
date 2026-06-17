## 简介
**Build a Multichannel Customer Support AI Assistant with Chatwoot & OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8260

---

# Build a Multichannel Customer Support AI Assistant with Chatwoot & OpenRouter


## 节点清单

| 节点 | 类型 |
|------|------|
| Chatwoot Webhook | Webhook |
| Squize Webhook Data | 数据设置 |
| Check If Incoming Message | IF 判断 |
| Load Chatwoot Conversation History | HTTP Request |
| Process Loaded History | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Chatwoot Assistant | LLM Chain |
| Send Message | HTTP Request |



## 功能说明

Build a Multichannel Customer Support AI Assistant（AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

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
- Chatwoot Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
