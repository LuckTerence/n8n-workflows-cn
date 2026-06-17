## 简介
**Generate Consensus Answers with Multiple AI Models & Peer Review System**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11660

---

# Generate Consensus Answers with Multiple AI Models & Peer Review System


## 节点清单

| 节点 | 类型 |
|------|------|
| Chat Trigger | Chat 触发器 |
| Gemini Model | OpenRouter Chat Model |
| Merge Answers | 数据合并 |
| Aggregate Answers | 数据聚合 |
| Merge Reviews | 数据合并 |
| Aggregate Reviews | 数据聚合 |
| Final Analysis Agent | AI Agent |
| Mistral Model | OpenRouter Chat Model |
| Gemma Model | OpenRouter Chat Model |
| Llama Model | OpenRouter Chat Model |
| Answer Agent #4 | LLM Chain |
| Answer Agent #3 | LLM Chain |
| Answer Agent #2 | LLM Chain |
| Answer Agent #1 | LLM Chain |
| Review Agent #1 | LLM Chain |
| Review Agent #2 | LLM Chain |
| Review Agent #3 | LLM Chain |
| Review Agent #4 | LLM Chain |
| Deepseek R1 model | OpenRouter Chat Model |



## 功能说明

Generate Consensus Answers with Multiple AI Models（AI 增强)Chat 消息触发，通过 n8n 内置节点实现自动化。

Chat 消息触发，通过 工作流编排 实现自动化。

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

- 节点总数：19
- 触发方式：Chat 消息触发

## 触发方式
- Chat Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：18
- 输出节点：0
- 分类：workflow-automation
