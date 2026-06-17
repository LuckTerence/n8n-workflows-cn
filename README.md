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

---

## 许可

模板来自 [nusquama/n8nworkflows.xyz](https://github.com/nusquama/n8nworkflows.xyz)，MIT 许可。
