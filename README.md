# n8n-workflows-cn

> 整理了一些 n8n 工作流模板，加了中文说明，顺手把 AI 模型换成了国内能用的。
>
> 源数据来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)。

---

## 做了什么

社区模板很多用的都是 OpenAI、Slack、Gmail 这些海外服务，国内用起来不太方便。这里：

- **AI 模型替换**：OpenAI → DeepSeek，Claude → DeepSeek，Gemini → 通义千问（直接改了节点的 Base URL 和 Model）
- **消息服务替换**：Slack → 飞书群机器人，Gmail → Email(SMTP)，Google Sheets → 飞书多维表格
- **加了中文标注**：每个 JSON 里有个 `_cn_meta` 字段，写了中文标题和适配说明

---

## 目录结构

```
workflows/
  ├── ai-agent/          # AI Agent、多 Agent 协作、MCP
  ├── devops/            # Webhook、API、监控告警
  ├── finance-analysis/  # 加密货币、股票数据
  ├── knowledge-rag/     # Ollama、向量数据库、RAG
  ├── multimodal-ai/     # 图像、语音、视频
  └── workflow-automation/  # 飞书通知、消息推送、数据同步
```

每个工作流一个子目录，如 `类别/工作流名称-ID/workflow.json`。

---

## 导入到 n8n

打开 n8n 编辑器 → Import from File → 选 `workflow.json` 就行。

如果还没装 n8n：

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

---

## 服务替换对照

| 原服务 | 替换为 | 怎么改 |
|------|------|------|
| OpenAI (GPT-4/GPT-4o) | DeepSeek | 改 OpenAI Chat Model 节点的 Base URL 为 `https://api.deepseek.com` |
| Anthropic (Claude) | DeepSeek | 把 Anthropic Chat Model 节点换成 OpenAI Chat Model，Base URL 指到 DeepSeek |
| Google Gemini | 通义千问 | 换成 OpenAI Chat Model 节点，Base URL `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| Slack | 飞书群机器人 | Webhook URL 换成飞书机器人的地址，消息格式改成飞书的 |
| Gmail | QQ邮箱 / 网易企业邮箱 | 换成 Email (IMAP/SMTP) 节点，配置国内邮箱的 IMAP/SMTP 地址 |
| Google Sheets | 飞书多维表格 | 换成 HTTP Request 节点，调飞书 Bitable API |
| Google Drive | 阿里云 OSS / 腾讯云 COS | 换成 HTTP Request 节点 |
| Google Calendar | 飞书日历 | 换成 HTTP Request 节点 |
| Notion | 飞书文档 / 语雀 | 换成 HTTP Request 节点 |
| Twilio | 腾讯云短信 / 阿里云短信 | 换成 HTTP Request 节点 |
| Stripe / PayPal | 微信支付 / 支付宝 | 换成 HTTP Request 节点 |
| GitHub | Gitee | HTTP Request 调 Gitee API |
| Supabase | 腾讯云 CloudBase | HTTP Request |
| Zoom | 腾讯会议 | HTTP Request |

**通用方法**：n8n 的专用节点本质就是封装了 API 调用的 HTTP Request。即使没有中国服务的专用节点，用 `HTTP Request` 节点查对应服务的 API 文档自己配就行。

---

## 工作流里的标注

每个 `workflow.json` 末尾有个 `_cn_meta` 字段，比如：

```json
{
  "_cn_meta": {
    "title_zh": "AI 日历助手",
    "category": "ai-agent",
    "tier": "A-adapted",
    "adapted_count": 2,
    "adapted_summary": [
      "OpenAI→DeepSeek: OpenAI Chat Model",
      "Slack→飞书: Send Slack Message"
    ]
  }
}
```

被改过的节点里也有 `_cn_adapted` 字段，写着具体改了什么。

---

## 分类说明

| 分类 | 数量 | 说明 |
|------|:--:|------|
| workflow-automation | 988 | 飞书通知、消息推送、数据同步 |
| devops | 153 | Webhook、API、监控告警、备份 |
| ai-agent | 93 | AI Agent、多 Agent 协作、MCP |
| multimodal-ai | 52 | 图像生成、语音转文字、视频 |
| knowledge-rag | 47 | Ollama本地部署、PGVector、Qdrant |
| finance-analysis | 2 | 加密货币、股票数据 |

## 工作流索引
> 点击链接可直接在 GitHub 上查看 workflow.json 内容

### AI Agent（93 个）

- [AI Agent Integration for Bubble Apps with MCP Protocol Data ](workflows/ai-agent/AI Agent Integration for Bubble Apps with MCP Protocol Data Access-4952/workflow.json)
- [AI Agents can Create, Enrich leads with this Lemlist Tool MC](workflows/ai-agent/AI Agents can Create, Enrich leads with this Lemlist Tool MCP Server-5233/workflow.json)
- [AI Agent聊天](workflows/ai-agent/AI Agent聊天-1954/workflow.json)
- [AI Chatbot Agent with a Panel of Experts using InfraNodus Gr](workflows/ai-agent/AI Chatbot Agent with a Panel of Experts using InfraNodus GraphRAG Knowledge-4402/workflow.json)
- [AI Chatbot Call Center: Demo Call Back (Production-Ready, Pa](workflows/ai-agent/AI Chatbot Call Center- Demo Call Back (Production-Ready, Part 6)-4050/workflow.json)
- [AI Chatbot Call Center: Demo Call Center (Production-Ready, ](workflows/ai-agent/AI Chatbot Call Center- Demo Call Center (Production-Ready, Part 2)-4045/workflow.json)
- [AI Chatbot Call Center: General Exception Flow (Production-R](workflows/ai-agent/AI Chatbot Call Center- General Exception Flow (Production-Ready, Part 8)-4052/workflow.json)
- [AI Chatbot Call Center: Taxi Booking Support (Production-Rea](workflows/ai-agent/AI Chatbot Call Center- Taxi Booking Support (Production-Ready, Part 7)-4051/workflow.json)
- [AI Chatbot Call Center: Taxi Booking Worker (Production-Read](workflows/ai-agent/AI Chatbot Call Center- Taxi Booking Worker (Production-Ready, Part 5)-4048/workflow.json)
- [AI Chatbot Call Center: Taxi Service (Production-Ready, Part](workflows/ai-agent/AI Chatbot Call Center- Taxi Service (Production-Ready, Part 3)-4046/workflow.json)
- [AI Personal Assistant](workflows/ai-agent/AI Personal Assistant-4723/workflow.json)
- [AI agents can get end of day market data with this Marketsta](workflows/ai-agent/AI agents can get end of day market data with this Marketstack Tool MCP Server-5205/workflow.json)

### DevOps & IT运维（153 个）

- [AI Linux管理员](workflows/devops/AI Linux管理员-3020/workflow.json)
- [AI Privacy-Minded Router: PII Detection for Privacy, Securit](workflows/devops/AI Privacy-Minded Router- PII Detection for Privacy, Security, & Compliance-5874/workflow.json)
- [AI-Powered Domain & IP Security Check Automation](workflows/devops/AI-Powered Domain & IP Security Check Automation-7189/workflow.json)
- [API Schema Extractor](workflows/devops/API Schema Extractor-2658/workflow.json)
- [Access Rat Genome Database with 100+ Operations via REST API](workflows/devops/Access Rat Genome Database with 100+ Operations via REST API MCP Server-5621/workflow.json)
- [Add User Authorization Layer to Your Telegram Bot with Admin](workflows/devops/Add User Authorization Layer to Your Telegram Bot with Admin Alerts-9203/workflow.json)
- [Advanced Medium API MCP Server](workflows/devops/Advanced Medium API MCP Server-5689/workflow.json)
- [Aggregate News Articles from NewsAPI, Mediastack & CurrentsA](workflows/devops/Aggregate News Articles from NewsAPI, Mediastack & CurrentsAPI into Database-11572/workflow.json)
- [Answer infrastructure questions in Mattermost with OpenRoute](workflows/devops/Answer infrastructure questions in Mattermost with OpenRouter and Qdrant-15629/workflow.json)
- [Auto n8n Updater (Docker)](workflows/devops/Auto n8n Updater (Docker)-5198/workflow.json)
- [Auto-Start Tagged Workflows Using n8n API after Deployment](workflows/devops/Auto-Start Tagged Workflows Using n8n API after Deployment-3996/workflow.json)
- [Automate Docker Container Updates with Telegram Approval Sys](workflows/devops/Automate Docker Container Updates with Telegram Approval System-3386/workflow.json)

### 金融分析（25 个）

- [AAVE投资组合Agent](workflows/finance-analysis/AAVE投资组合Agent-4267/workflow.json)
- [AI-Powered Invoice Reminder & Payment Tracker for Finance & ](workflows/finance-analysis/AI-Powered Invoice Reminder & Payment Tracker for Finance & Accounting-10111/workflow.json)
- [AI-Powered Stock Market Summary Bot](workflows/finance-analysis/AI-Powered Stock Market Summary Bot-4867/workflow.json)
- [AI股票基本面分析](workflows/finance-analysis/AI股票基本面分析-2183/workflow.json)
- [Aggregate Crypto and Stock Market News Feed from Multiple So](workflows/finance-analysis/Aggregate Crypto and Stock Market News Feed from Multiple Sources-11103/workflow.json)
- [Analyze Crypto Market with CoinGecko: Volatility Metrics & I](workflows/finance-analysis/Analyze Crypto Market with CoinGecko- Volatility Metrics & Investment Signals-4115/workflow.json)
- [Automate Crypto News Posting to X & Telegram with AI Summari](workflows/finance-analysis/Automate Crypto News Posting to X & Telegram with AI Summarization-2961/workflow.json)
- [Automate Stock Trades with AI-Driven Technical Analysis & Al](workflows/finance-analysis/Automate Stock Trades with AI-Driven Technical Analysis & Alpaca Trading-7240/workflow.json)
- [Automated Forex and Gold Trading Signal Handler with MetaTra](workflows/finance-analysis/Automated Forex and Gold Trading Signal Handler with MetaTrader 5 via Webhooks-11439/workflow.json)
- [Automated Range Trading with Uniswap V3, Telegram Alerts & M](workflows/finance-analysis/Automated Range Trading with Uniswap V3, Telegram Alerts & MetaMask Delegation-8427/workflow.json)
- [Control AlphaInsider stock and crypto portfolios from Telegr](workflows/finance-analysis/Control AlphaInsider stock and crypto portfolios from Telegram text and voice-13816/workflow.json)
- [Create a cryptocurrency-powered API for selling resources wi](workflows/finance-analysis/Create a cryptocurrency-powered API for selling resources with AgentGatePay-11874/workflow.json)

### 知识库 & RAG（47 个）

- [AI Agent with Ollama for current weather and wiki](workflows/knowledge-rag/AI Agent with Ollama for current weather and wiki-2931/workflow.json)
- [AI-Powered Ticket Triage with Multi-Model Classification & K](workflows/knowledge-rag/AI-Powered Ticket Triage with Multi-Model Classification & Knowledge Base-11854/workflow.json)
- [AI-powered RAG configuration assistant: From form to email r](workflows/knowledge-rag/AI-powered RAG configuration assistant- From form to email recommendations-11990/workflow.json)
- [Automate Token Purchases with Dollar Cost Averaging on Unisw](workflows/knowledge-rag/Automate Token Purchases with Dollar Cost Averaging on Uniswap V3 & 1Shot API-8044/workflow.json)
- [Automated Document Compliance Validation with AI and Vector ](workflows/knowledge-rag/Automated Document Compliance Validation with AI and Vector Database-7662/workflow.json)
- [Automated Meta Token Renewal System with Graph API and Data ](workflows/knowledge-rag/Automated Meta Token Renewal System with Graph API and Data Storage-9604/workflow.json)
- [Average property value estimates from Zillow, Redfin, and Re](workflows/knowledge-rag/Average property value estimates from Zillow, Redfin, and Realtor.com-15477/workflow.json)
- [Basic RAG chat](workflows/knowledge-rag/Basic RAG chat-5028/workflow.json)
- [Build Document Q&A API with PDF Vector and Webhooks](workflows/knowledge-rag/Build Document Q&A API with PDF Vector and Webhooks-8498/workflow.json)
- [Build a Local AI Assistant with Llama 3.2, RAG, and Search u](workflows/knowledge-rag/Build a Local AI Assistant with Llama 3.2, RAG, and Search using Ollama & MCP-5398/workflow.json)
- [Build a local RAG chatbot with Ollama, Qwen, BGE-M3 and Post](workflows/knowledge-rag/Build a local RAG chatbot with Ollama, Qwen, BGE-M3 and Postgres PGVector-14782/workflow.json)
- [Build an AI-Powered Tech Radar Advisor with SQL DB, RAG, and](workflows/knowledge-rag/Build an AI-Powered Tech Radar Advisor with SQL DB, RAG, and Routing Agents-3151/workflow.json)

### 多模态AI（52 个）

- [3D手办生成](workflows/multimodal-ai/3D手办生成-3628/workflow.json)
- [AI Real Estate Agent: End-to-End Ops Automation (Web, Data, ](workflows/multimodal-ai/AI Real Estate Agent- End-to-End Ops Automation (Web, Data, Voice)-4368/workflow.json)
- [AI图片敏感内容检测](workflows/multimodal-ai/AI图片敏感内容检测-5661/workflow.json)
- [AI图片生成Telegram推送](workflows/multimodal-ai/AI图片生成Telegram推送-4049/workflow.json)
- [AI邮件附件分析](workflows/multimodal-ai/AI邮件附件分析-3169/workflow.json)
- [Airbnb Telegram Agent - AI-powered accommodation search with](workflows/multimodal-ai/Airbnb Telegram Agent - AI-powered accommodation search with voice support-4494/workflow.json)
- [Audio Transcription with Telegram and Groq Whisper](workflows/multimodal-ai/Audio Transcription with Telegram and Groq Whisper-10037/workflow.json)
- [Automate Blog Creation in Brand Voice with AI](workflows/multimodal-ai/Automate Blog Creation in Brand Voice with AI-2648/workflow.json)
- [Automate E-commerce Return Guides with Email Verification, P](workflows/multimodal-ai/Automate E-commerce Return Guides with Email Verification, PDF-Image Generation -8942/workflow.json)
- [Automate Image Validation Tasks using AI Vision](workflows/multimodal-ai/Automate Image Validation Tasks using AI Vision-2420/workflow.json)
- [Automate Order Confirmations with VAPI Voice AI & Timezone I](workflows/multimodal-ai/Automate Order Confirmations with VAPI Voice AI & Timezone Intelligence-7380/workflow.json)
- [Automate Outbound Voice Calls from Go High Level Opportuniti](workflows/multimodal-ai/Automate Outbound Voice Calls from Go High Level Opportunities with Vapi-6088/workflow.json)

### 工作流自动化（1110 个）

- [10X E-commerce Sales AI Product Photography That Makes your ](workflows/workflow-automation/10X E-commerce Sales AI Product Photography That Makes your product look Premium-6151/workflow.json)
- [3D Product Video Generator from 2D Image for E-Commerce Stor](workflows/workflow-automation/3D Product Video Generator from 2D Image for E-Commerce Stores-4987/workflow.json)
- [AI Agent for realtime insights on meetings](workflows/workflow-automation/AI Agent for realtime insights on meetings-2651/workflow.json)
- [AI Automated HR Workflow for CV Analysis and Candidate Evalu](workflows/workflow-automation/AI Automated HR Workflow for CV Analysis and Candidate Evaluation-2860/workflow.json)
- [AI Client Onboarding Agent: Auto Welcome Email Generator](workflows/workflow-automation/AI Client Onboarding Agent- Auto Welcome Email Generator-4377/workflow.json)
- [AI Client Onboarding Agent: Auto Welcome Email Generator](workflows/workflow-automation/AI Client Onboarding Agent- Auto Welcome Email Generator-4448/workflow.json)
- [AI Crew to Automate Fundamental Stock Analysis - Q&A Workflo](workflows/workflow-automation/AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow-2183/workflow.json)
- [AI Data Analyst Agent for Spreadsheets with NocoDB](workflows/workflow-automation/AI Data Analyst Agent for Spreadsheets with NocoDB-2653/workflow.json)
- [AI Data Extraction with Dynamic Prompts and Baserow](workflows/workflow-automation/AI Data Extraction with Dynamic Prompts and Baserow-2780/workflow.json)
- [AI Image Nudity Detection Tool with Image Moderation API](workflows/workflow-automation/AI Image Nudity Detection Tool with Image Moderation API-5661/workflow.json)
- [AI Invoice Agent](workflows/workflow-automation/AI Invoice Agent-7905/workflow.json)
- [AI Job Crawler with Suitability Scoring](workflows/workflow-automation/AI Job Crawler with Suitability Scoring-15412/workflow.json)
---

## 许可

模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。
