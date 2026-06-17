## 简介
**Enhance Customer Support with RAG-Powered AI**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11807

---

# Enhance Customer Support with RAG-Powered AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Workflow Configuration | 数据设置 |
| Email Trigger (IMAP) | Email 读取 |
| Webhook Trigger (Live Chat) | Webhook |
| WhatsApp Trigger | whatsAppTrigger |
| Slack Trigger (Mentions) | slackTrigger |
| Discord Webhook Trigger | Webhook |
| Normalize Payload | 数据设置 |
| Preprocess Query | Code |
| OpenAI Chat Model (RAG) | OpenAI Chat Model |
| OpenAI Chat Model (Sentiment) | OpenAI Chat Model |
| OpenAI Chat Model (Escalation) | OpenAI Chat Model |
| Sentiment Analysis | LLM Chain |
| Confidence Scoring | Code |
| Check Confidence Threshold | IF 判断 |
| Check Sentiment | IF 判断 |
| Escalation Needed? | IF 判断 |
| Business Hours Check | IF 判断 |
| Channel Router | Switch 路由 |
| Format Email Response | 数据设置 |
| Send Email Reply | Email 发送 |
| Escalation Reasoning | LLM Chain |
| Prepare Ticket Object | 数据设置 |
| Create Zendesk Ticket | zendesk |
| Update Zendesk Ticket | zendesk |
| Escalation Alert to Support Team | Slack |
| Auto-Categorization | Code |
| Log Conversation to Sheets | Google Sheets |
| Weekly Maintenance Schedule | 定时触发器 |
| Fetch Weekly Metrics | Google Sheets |
| Supabase Vector Insert | Supabase 向量存储 |
| OpenAI Embeddings (Insert) | OpenAI Embeddings |
| Chat Memory | 记忆缓冲区 |
| Conversation History Manager | Code |
| New vs Existing Conversation | IF 判断 |
| Human Takeover Detection | IF 判断 |
| Log Conversation to Zendesk | zendesk |
| Send Weekly Summary | Slack |
| Check Message Scope | IF 判断 |
| Document Loader | 文档加载器 |
| Text Splitter | 文本分割器 |
| RAG Support Agent | AI Agent |
| Fetch Conversation History | Code |
| Merge History with Query | 数据合并 |
| Format Webhook Response | 数据设置 |
| Format WhatsApp Response | 数据设置 |
| Format Discord Response | 数据设置 |
| Format Slack Response | 数据设置 |
| End Workflow | 空操作 |
| Prepare Metrics for Vector Insert | 数据设置 |

## 触发方式
- Webhook Trigger (Live Chat) 触发
- WhatsApp Trigger 触发
- Slack Trigger (Mentions) 触发
- Discord Webhook Trigger 触发
- Weekly Maintenance Schedule 触发

## 统计
- 节点总数：49
- 触发节点：5
- 处理节点：40
- 输出节点：4
- 分类：knowledge-rag
