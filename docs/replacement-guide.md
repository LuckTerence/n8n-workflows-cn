# 西方服务 → 中国服务替换指南

## 为什么需要替换？

n8n 官方模板和社区模板大多使用西方 SaaS 服务（Google、Microsoft、Slack 等），这些服务在中国大陆要么无法访问，要么需要科学上网。本指南帮助你快速找到替代方案。

## 替换对照表

### 📧 邮件服务

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Gmail | Gmail Trigger / Gmail | QQ邮箱 / 网易企业邮箱 | 改用 Email (IMAP) 节点，配置国内邮箱的 IMAP/SMTP 地址 |
| Gmail SMTP | Gmail | 阿里云邮件推送 / SendCloud | 改用 HTTP Request 调用邮件 API |
| SendGrid | SendGrid | SendCloud / 阿里云邮件推送 | 改用 HTTP Request 节点 |

**示例 — Gmail → QQ邮箱：**
```
原工作流: Gmail Trigger → ... → Gmail Send
替换方案: Email Trigger (IMAP) → ... → Email Send (SMTP)
IMAP: imap.qq.com:993
SMTP: smtp.qq.com:465
```

### 💬 即时通讯 & 协作

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Slack | Slack | 飞书群机器人 / 企业微信群机器人 | 改用 Webhook 节点，POST 到飞书/企微 Webhook URL |
| Discord | Discord | QQ群机器人 / 飞书群 | 改用 HTTP Request |
| Microsoft Teams | Microsoft Teams | 飞书 / 钉钉 | 改用 Webhook |
| WhatsApp | WhatsApp | 微信公众号 / 企业微信应用 | 改用 HTTP Request 调用微信 API |

**示例 — Slack → 飞书群机器人：**
```
原工作流: Slack 发送消息
替换方案: Webhook POST → 飞书群机器人 webhook URL
Body: { "msg_type": "text", "content": { "text": "{{ $json.message }}" } }
```

### 📊 文档 & 表格

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Google Sheets | Google Sheets | 飞书多维表格 / 腾讯文档 | 改用 HTTP Request 调用飞书/腾讯文档 API |
| Google Docs | Google Docs | 飞书文档 / 语雀 | 改用 HTTP Request |
| Google Drive | Google Drive | 阿里云 OSS / 百度网盘 | 改用 HTTP Request |
| Notion | Notion | 飞书文档 / 语雀 / FlowUs | 改用 HTTP Request |
| Airtable | Airtable | 飞书多维表格 / 维格表 (Vika) | 改用 HTTP Request |

**示例 — Google Sheets → 飞书多维表格：**
```
原工作流: Google Sheets → 读取/写入
替换方案: HTTP Request → 飞书开放平台 API
GET https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records
Headers: Authorization: Bearer {tenant_access_token}
```

### 🗓️ 日历 & 会议

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Google Calendar | Google Calendar | 飞书日历 | 改用 HTTP Request 调用飞书日历 API |
| Zoom | Zoom | 腾讯会议 | 改用 HTTP Request 调用腾讯会议 API |
| Calendly | Calendly | 腾讯问卷预约 | 改用 HTTP Request |

### 🤖 AI / LLM

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| OpenAI (GPT-4/GPT-4o) | OpenAI Chat Model | DeepSeek / 通义千问 / Kimi | OpenAI 节点改 Base URL + API Key |
| Claude (Anthropic) | Anthropic Chat Model | DeepSeek / 通义千问 | OpenAI 节点改 Base URL |
| Google Gemini | Google Gemini | 通义千问 VL (视觉) | HTTP Request 调用 API |
| Pinecone | Pinecone Vector Store | Milvus / Qdrant 自建 | 替换 Vector Store 节点 |
| Replicate | Replicate | 硅基流动 (SiliconFlow) | HTTP Request |

**示例 — OpenAI → DeepSeek：**
```
原配置:
  Base URL: https://api.openai.com/v1
  API Key: sk-xxx
  Model: gpt-4o

替换为:
  Base URL: https://api.deepseek.com
  API Key: sk-your-deepseek-key
  Model: deepseek-chat

n8n 节点不需要改动，只需修改 OpenAI Chat Model 节点的配置即可！
```

### 💰 支付 & 电商

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Stripe | Stripe | 微信支付 / 支付宝 | HTTP Request 调用支付 API |
| PayPal | PayPal | 支付宝国际 | HTTP Request |
| Shopify | Shopify | 有赞 / 微盟 | HTTP Request |

### 📱 短信 & 通知

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Twilio | Twilio | 腾讯云短信 / 阿里云短信 | HTTP Request |
| Pushover | Pushover | 微信服务通知 / Server酱 | Webhook |

### 🔧 开发工具

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| GitHub | GitHub | Gitee | HTTP Request 调用 Gitee API |
| GitLab | GitLab | Gitee / Coding | HTTP Request |
| Jira | Jira | PingCode / ONES | HTTP Request |
| Sentry | Sentry | 腾讯 TAM / 阿里 ARMS | HTTP Request |

### ☁️ 云服务 & 存储

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| AWS S3 | AWS S3 | 阿里云 OSS / 腾讯云 COS | S3 兼容 API 改 Endpoint |
| AWS Lambda | AWS Lambda | 阿里云函数计算 FC | HTTP Request |
| MongoDB Atlas | MongoDB | 阿里云 MongoDB / 腾讯云 MongoDB | 改 MongoDB 连接字符串 |
| Supabase | Supabase | 腾讯云 CloudBase | HTTP Request |

### 🌐 社交媒体

| 西方服务 | n8n 节点 | 中国替代 | 替换方式 |
|------|------|------|------|
| Twitter (X) | Twitter | 微博 | HTTP Request |
| Facebook | Facebook | 微信朋友圈广告 | - |
| Instagram | Instagram | 小红书 | HTTP Request |
| LinkedIn | LinkedIn | 脉脉 / Boss直聘 | HTTP Request |
| YouTube | YouTube | B站 / 抖音 | HTTP Request |
| Reddit | Reddit | 知乎 / 贴吧 | HTTP Request |

---

## 🔧 通用替换技巧

### 1. 用 HTTP Request 替代专用节点

n8n 的专用节点本质上就是封装了 API 调用的 HTTP Request。即使没有中国服务的专用节点，你可以：

1. 查看中国服务的 API 文档
2. 使用 n8n 的 `HTTP Request` 节点
3. 配置正确的 URL、Headers（含认证 Token）、Body

### 2. 保持工作流逻辑不变

大多数情况下，只需要替换数据源和输出目标，工作流的核心处理逻辑（filter / code / if / loop）保持不变。

### 3. 渐进替换

不需要一次性替换所有节点。建议：
1. 先替换输入源（Trigger）
2. 再替换输出目标（通知、存储）
3. 最后替换中间处理节点

---

> 💡 有替换方案需要补充？欢迎提 PR！
