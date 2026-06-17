## 简介
**Build Your First AI Agent**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6270

---

# Build Your First AI Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Get News | rssFeedReadTool |
| Get Weather | HTTP Request 工具 |
| Your First AI Agent | AI Agent |
| Connect your model | OpenAI Chat Model |
| Example Chat | Chat 触发器 |
| Conversation Memory | 记忆缓冲区 |



## 功能说明

Build Your First AI Agent（AI 增强)Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：6
- 触发方式：Chat 消息触发

## 触发方式
- Get News 触发
- Example Chat 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：3
- 输出节点：1
- 分类：ai-agent
