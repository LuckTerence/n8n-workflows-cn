## 简介
**LangChain AI Agent**

基于LangChain节点的Telegram机器人

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2592

---

# LangChain AI Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Window Buffer Memory | 记忆缓冲区 |
| Listen for incoming events | Telegram 触发器 |
| Send final reply | Telegram |
| Send back an image | Telegram 工具 |
| Generate image in Dalle | HTTP 工具 |
| AI Agent | AI Agent |



## 功能说明

LangChain AI Agent（AI 增强)Telegram 消息触发，通过 Telegram 实现自动化。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：Telegram 消息触发

## 触发方式
- Listen for incoming events 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：ai-agent
