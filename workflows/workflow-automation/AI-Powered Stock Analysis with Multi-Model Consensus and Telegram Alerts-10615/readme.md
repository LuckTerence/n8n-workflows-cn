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

## 触发方式
- Daily Stock Check 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：18
- 输出节点：5
- 分类：workflow-automation
