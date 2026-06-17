# n8n-workflows-cn

[中文](README.md) | English

[![Workflows](https://img.shields.io/badge/Workflows-1480-brightgreen)](INDEX.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![n8n](https://img.shields.io/badge/n8n-%3E%3D1.0-red)](https://n8n.io)

---

> **1,480 n8n workflow templates · adapted for DeepSeek / Feishu / WeChat Pay / Alibaba Cloud · 1,031 ready-to-use**

[Browse Online](https://luckterence.github.io/n8n-workflows-cn/) · [Full Index](INDEX.md) · [Curated Picks](CURATED.md) · [Quick Start](#quick-start)

---

## What is this?

A collection of 1,480 n8n workflow templates from the [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz) community, with all overseas services (OpenAI, Slack, Google Workspace, etc.) replaced by China-friendly alternatives (DeepSeek, Tongyi Qianwen, Feishu/Lark, WeChat Pay, Alibaba Cloud, etc.). Every workflow includes a Chinese readme with adaptation notes.

**Who is this for? Developers using n8n who want production-ready automations without dealing with overseas accounts and payment methods.**

## Quick Start

```bash
# Start n8n with one command
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
# Open http://localhost:5678 → Import from File → pick any workflow.json → add your API key
```

**Start with these:**

| Workflow | Description | Difficulty | Link |
|----------|-------------|:----------:|------|
| AI Agent Chat | Basic AI chat agent, 5 nodes, DeepSeek key ready |  | [ Open](workflows/ai-agent/AI%20Agent聊天-1954/) |
| AI Helpdesk (Telegram) | Full Telegram customer service bot |  | [ Open](workflows/ai-agent/AI客服中心Telegram呼入-4044/) |
| Smart Email Classifier | AI auto-tags and archives emails |  | [ Open](workflows/workflow-automation/Gmail智能分类归档-3686/) |
| Stock Fundamental Analysis | Multi-dimensional stock analysis |  | [ Open](workflows/finance-analysis/AI股票基本面分析-2183/) |
| Auto Start/Stop n8n Flows | Manage n8n with n8n itself |  | [ Open](workflows/devops/定时启停n8n工作流-3229/) |

## Workflow Categories

### AI Agent (93 templates)

AI agents, chatbots, multi-agent collaboration.

| Subcategory | Count | Description |
|-------------|:-----:|-------------|
| Chatbots | 26 | AI chat, multi-turn dialogue, emotional support |
| MCP Tools & Integration | 19 | MCP servers exposing API tools for AI agents |
| Messaging Platform Bots | 5 | AI bots on Telegram, WhatsApp, LINE |
| Multi-Agent | 5 | Agent collaboration, debate, orchestration |
| Personal Assistant | 3 | AI-driven personal productivity |
| Tutorials | 2 | Build Your First AI Agent series |
| Finance Agent | 2 | Financial analysis & investment agents |
| Agent Framework | 2 | LangChain, custom agent frameworks |
| Search & Research Agent | 2 | Web search & information retrieval |
| Multimodal Agent | 1 | Image/voice capable agents |
| Others | 26 | Customer service, HR, coding, calendar agents |

### DevOps (153 templates)

Server management, API development, MCP servers, monitoring, deployment.

### Finance Analysis (25 templates)

Stock analysis, cryptocurrency, trading signals, fraud detection.

### Knowledge RAG (47 templates)

Retrieval-augmented generation — knowledge base Q&A, vector databases (Qdrant, Milvus, Pinecone).

### Multimodal AI (52 templates)

Voice & audio (TTS, Whisper transcription), image generation (Stable Diffusion, DALL-E, Flux), video generation, 3D content.

### Workflow Automation (1,110 templates)

Email processing, messaging bots, data scraping, CRM & customer service, social media, ERP & finance, e-commerce, forms & surveys, notifications, calendars, project management, and more.

## Service Replacements

| Original | Replacement | How |
|----------|-------------|-----|
| OpenAI (GPT-4o) | DeepSeek | Base URL → `https://api.deepseek.com` |
| Anthropic (Claude) | DeepSeek | Same as above |
| Google Gemini | Tongyi Qianwen | OpenAI-compatible endpoint |
| Slack | Feishu/Lark Bot | Webhook URL + message format |
| Gmail | QQ Mail / NetEase | IMAP/SMTP node |
| Google Sheets | Feishu Bitable | HTTP Request → Bitable API |
| Google Drive | Alibaba Cloud OSS | HTTP Request node |
| Twilio | Tencent Cloud SMS | HTTP Request node |
| Stripe / PayPal | WeChat Pay / Alipay | HTTP Request node |

## License

MIT. Original templates from [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz), also MIT.
