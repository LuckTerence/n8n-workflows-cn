# n8n-workflows-cn

> 整理了 n8n 工作流模板，加了中文说明，顺手把 AI 模型换成了国内能用的。
>
> 源数据来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)。

---

## 做了什么

社区模板大多用的 OpenAI、Slack、Gmail 这些海外服务，国内用起来不太方便。这里：

- **AI 模型替换**：OpenAI → DeepSeek，Claude → DeepSeek，Gemini → 通义千问（直接改了节点的 Base URL 和 Model）
- **消息服务替换**：Slack → 飞书群机器人，Gmail → Email(SMTP)，Google Sheets → 飞书多维表格
- **加了中文标注**：每个 JSON 里有个 `_cn_meta` 字段，写了中文标题和适配说明

---

## 分类速览

| 分类 | 数量 | 说明 |
|------|:--:|------|
| [workflow-automation](workflows/workflow-automation/) | 1110 | 飞书通知、消息推送、数据同步 |
| [devops](workflows/devops/) | 153 | Webhook、API、监控告警、备份 |
| [ai-agent](workflows/ai-agent/) | 93 | AI Agent、多 Agent 协作、MCP |
| [multimodal-ai](workflows/multimodal-ai/) | 52 | 图像生成、语音转文字、视频 |
| [knowledge-rag](workflows/knowledge-rag/) | 47 | Ollama本地部署、PGVector、Qdrant |
| [finance-analysis](workflows/finance-analysis/) | 25 | 加密货币、股票数据 |

> [查看全部 1480 个工作流](INDEX.md)

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

## 导入到 n8n

打开 n8n 编辑器 → Import from File → 选 `workflow.json` 就行。

如果还没装 n8n：

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

---

## 许可

模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。
