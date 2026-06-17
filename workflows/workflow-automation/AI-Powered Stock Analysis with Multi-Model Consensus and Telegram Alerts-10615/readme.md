## 简介
**AI-Powered Stock Analysis with Multi-Model Consensus and Telegram Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10615

---

# AI-Powered Stock Analysis with Multi-Model Consensus and Telegram Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Stock Check | 定时触发器 |
| Analyze Stock Trends | Code |
| Predict Future Trends | Code |
| Format Telegram Message | 数据设置 |
| Send Telegram Alert | Telegram |
| Analyze News Sentiment | Code |
| Process Analyst Ratings | Code |
| Analyze Social Sentiment | Code |
| Combine All Analysis | 数据合并 |
| Generate Comprehensive Recommendation | Code |
| OpenAI GPT Model | OpenAI Chat Model |
| Anthropic Claude Model | OpenAI Chat Model |
| Prepare AI Validation Input | 数据设置 |
| Combine AI Validations | 数据合并 |
| Evaluate AI Consensus | Code |
| AI Validator 1 - OpenAI | LLM Chain |
| AI Validator 2 - Anthropic | LLM Chain |
| AI Validator 3 - Gemini | LLM Chain |
| API Configuration | 数据设置 |
| Stock Data Fatch | HTTP Request |
| News Sentiment Fatch | HTTP Request |
| Analyst Ratings Fetch | HTTP Request |
| Social Media Sentiment Fetch | HTTP Request |
| xAI Grok Chat Model | lmChatXAiGrok |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：24
- 触发方式：定时触发

## 触发方式
- Daily Stock Check 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：18
- 输出节点：5
- 分类：workflow-automation
