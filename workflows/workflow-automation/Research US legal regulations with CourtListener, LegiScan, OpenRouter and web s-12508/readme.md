## 简介
**Research US legal regulations with CourtListener, LegiScan, OpenRouter and web search**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12508

---

# Research US legal regulations with CourtListener, LegiScan, OpenRouter and web search


## 节点清单

| 节点 | 类型 |
|------|------|
| Court Listener Discovery | HTTP Request 工具 |
| Google Search Discovery | HTTP 工具 |
| LegiScan Discovery | HTTP Request 工具 |
| Court Listener Retrieveal | HTTP Request 工具 |
| Think Tool Prioritization | 思考工具 |
| LegiScan Retrieval | HTTP Request 工具 |
| DocumentCloud Retrieval | HTTP Request 工具 |
| Jina URL Text Extraction | jinaAiTool |
| Think Tool Analysis | 思考工具 |
| Step 5: Verification | LLM Chain |
| Structured Output Parser | 结构化输出解析器 |
| If hallucinations present | IF 判断 |
| Think Tool Analysis1 | 思考工具 |
| Set Report | 数据设置 |
| Set Output | 数据设置 |
| Retry if Tools Not Used | IF 判断 |
| Retry if Tools Not Used1 | IF 判断 |
| Retry if Response Empty | IF 判断 |
| Retry if Response Empty1 | IF 判断 |
| Step 1: Discovery | AI Agent |
| Auto Fallback | OpenRouter Chat Model |
| Auto Fallback1 | OpenRouter Chat Model |
| Step 2: Prioritization | AI Agent |
| Auto Fallback2 | OpenRouter Chat Model |
| Step 3: Retrieval | AI Agent |
| Auto Fallback3 | OpenRouter Chat Model |
| Step 4: Report Writing | AI Agent |
| Auto Fallback4 | OpenRouter Chat Model |
| Auto Fallback5 | OpenRouter Chat Model |
| Step 6: Fixing Hallucinations | AI Agent |
| If Empty Output | IF 判断 |
| If Empty Output1 | IF 判断 |
| Plural Retrieval | HTTP Request 工具 |
| Plural Discovery1 | HTTP Request 工具 |
| Qwen3 | OpenRouter Chat Model |
| Qwen4 | OpenRouter Chat Model |
| Sonnet 4.5 | OpenRouter Chat Model |
| Sonnet 4. | OpenRouter Chat Model |
| Opus | OpenRouter Chat Model |
| Opus1 | OpenRouter Chat Model |
| Document Cloud Discovery | HTTP Request 工具 |
| Trigger legal research request (Webhook) | Webhook |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，Webhook 触发。

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

- 节点总数：42
- 触发方式：Webhook 触发

## 触发方式
- Trigger legal research request (Webhook) 触发

## 统计
- 节点总数：42
- 触发节点：1
- 处理节点：32
- 输出节点：9
- 分类：workflow-automation
