## 简介
**Open Deep Research - AI-Powered Autonomous Research Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2883

---

# Open Deep Research - AI-Powered Autonomous Research Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Chat Message Trigger | Chat 触发器 |
| Generate Search Queries using LLM | LLM Chain |
| LLM Response Provider (OpenRouter) | OpenRouter Chat Model |
| Parse and Chunk JSON Data | Code |
| Perform SerpAPI Search Request | HTTP Request |
| Perform Jina AI Analysis Request | HTTP Request |
| Format SerpAPI Organic Results | Code |
| Extract Relevant Context via LLM | AI Agent |
| Generate Comprehensive Research Report | AI Agent |
| Split Data for SerpAPI Batching | 分批处理 |
| Split Data for Jina AI Batching | 分批处理 |
| LLM Memory Buffer (Input Context) | 记忆缓冲区 |
| LLM Memory Buffer (Report Context) | 记忆缓冲区 |
| Fetch Wikipedia Information | Wikipedia 工具 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

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

- 节点总数：14
- 触发方式：Chat 消息触发

## 触发方式
- Chat Message Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
