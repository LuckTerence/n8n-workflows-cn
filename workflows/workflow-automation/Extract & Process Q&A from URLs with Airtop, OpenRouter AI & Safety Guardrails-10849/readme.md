## 简介
**Extract & Process Q&A from URLs with Airtop, OpenRouter AI & Safety Guardrails**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10849

---

# Extract & Process Q&A from URLs with Airtop, OpenRouter AI & Safety Guardrails


## 节点清单

| 节点 | 类型 |
|------|------|
| Filter Only URLs | 过滤器 |
| Extract Q&A from URL | Airtop |
| Apply Safety Guardrails | guardrails |
| OpenRouter Model | OpenRouter Chat Model |
| Send Safe Response | Telegram |
| Send Violation Alert | Telegram |
| Tavily Web Search | tavilyTool |
| Telegram Trigger1 | Telegram 触发器 |
| Main agent | AI Agent |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger1 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
