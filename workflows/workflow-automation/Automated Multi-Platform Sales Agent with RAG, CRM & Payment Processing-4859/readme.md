## 简介
**Automated Multi-Platform Sales Agent with RAG, CRM & Payment Processing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4859

---

# Automated Multi-Platform Sales Agent with RAG, CRM & Payment Processing


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| No Operation, do nothing | 空操作 |
| Calendar Agent | 工作流工具 |
| CRM Agent | 工作流工具 |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| Handle Message Types | Switch 路由 |
| Reply To User1 | WhatsApp |
| Edit Fields - chat1 | 数据设置 |
| Reply To User | WhatsApp |
| WhatsApp | whatsAppTrigger |
| WhatsApp Business Cloud | WhatsApp |
| HTTP Request | HTTP Request |
| OpenAI | OpenAI |
| Edit Fields - chat2 | 数据设置 |
| Output - chat | 数据设置 |
| Postgres PGVector Store | PGVector 向量存储 |
| Get Lead | PostgreSQL |
| When chat message received | Chat 触发器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| Embeddings Google Gemini1 | Google Gemini Embeddings |
| Simple Memory | 记忆缓冲区 |
| Create Charge | stripeTool |
| Create Discount Coupon | stripeTool |
| Get Customer Card | stripeTool |
| Get Customer | stripeTool |
| Create Customer | stripeTool |
| Update Customer | stripeTool |
| Delete Customer | stripeTool |
| Google Gemini Chat Model4 | OpenAI Chat Model |
| Response1 | 数据设置 |
| Try Again2 | 数据设置 |
| Billing Agent | 工作流工具 |
| Billing Agent1 | AI Agent |
| technical_and_sales_knowledge | 向量存储工具 |
| Facebook Trigger | Webhook |
| Edit Fields - facebook | 数据设置 |
| Respond to Webhook - facebook post | 响应 Webhook |
| Respond to Webhook - facebook get | 响应 Webhook |
| Instagram Trigger | Webhook |
| Respond to Webhook - instagram get | 响应 Webhook |
| Respond to Webhook - instagram post | 响应 Webhook |
| Edit Fields - instagram | 数据设置 |
| If is not echo - facebook | IF 判断 |
| If is not echo - instagram | IF 判断 |
| Sales Agent Demo - typing_on | facebookGraphApi |
| Edit Fields - chat | 数据设置 |
| Facebook Graph API - Sales Agent Demo | facebookGraphApi |
| Instagram Graph API - smb.sales.agent.demo | HTTP Request |
| Switch1 | Switch 路由 |
| Send First Message | WhatsApp |
| Personalised First Message | AI Agent |
| Gemini | OpenAI Chat Model |
| Contact Form | 表单触发器 |
| Response | 数据设置 |
| Try Again | 数据设置 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Window Buffer Memory | 记忆缓冲区 |
| Success | 数据设置 |
| Create Event with Attendee | Google Calendar 工具 |
| Create Event | Google Calendar 工具 |
| Get Events | Google Calendar 工具 |
| Delete Event | Google Calendar 工具 |
| Update Event | Google Calendar 工具 |
| Try Again1 | 数据设置 |
| Calendar Agent1 | AI Agent |
| Google Gemini Chat Model2 | OpenAI Chat Model |
| Create Opportunity | PostgreSQL 工具 |
| List Records | PostgreSQL 工具 |
| Update Contact | PostgreSQL 工具 |
| Delete Contact | PostgreSQL 工具 |
| Delete Opportunity | PostgreSQL 工具 |
| Update Opportunity | PostgreSQL 工具 |
| Google Gemini Chat Model3 | OpenAI Chat Model |
| Create Contact | PostgreSQL 工具 |
| CRM Agent2 | AI Agent |
| Create Contact1 | PostgreSQL |



## 功能说明

多智能体协作系统，多个 AI Agent 协同完成任务，Webhook 触发。

Webhook触发、Chat 消息触发，通过 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：77
- 触发方式：Chat 消息触发, Webhook 触发, 表单提交触发

## 触发方式
- WhatsApp 触发
- When chat message received 触发
- Facebook Trigger 触发
- Instagram Trigger 触发
- Contact Form 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：77
- 触发节点：6
- 处理节点：61
- 输出节点：10
- 分类：workflow-automation
