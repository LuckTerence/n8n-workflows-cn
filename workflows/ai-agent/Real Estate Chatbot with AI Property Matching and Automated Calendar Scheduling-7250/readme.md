## 简介
**Real Estate Chatbot with AI Property Matching and Automated Calendar Scheduling**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7250

---

# Real Estate Chatbot with AI Property Matching and Automated Calendar Scheduling


## 节点清单

| 节点 | 类型 |
|------|------|
| LLM conversation | AI Agent |
| PostgreSQL Memory | PostgreSQL 聊天记忆 |
| Parse Data | Code |
| Save Personal Info | PostgreSQL |
| Query Properties | PostgreSQL |
| Ready Check | IF 判断 |
| OpenAI Chat Model | OpenAI Chat Model |
| Format Results with AI | AI Agent |
| Format Response | 数据设置 |
| Send Formatted Response | 响应 Webhook |
| Webhook | Webhook |
| SerpAPI | SerpApi 工具 |
| update_Calendar | Google Calendar 工具 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Gmail1 | Gmail 工具 |
| AI Agent | AI Agent |
| Google Calendar | Google Calendar 工具 |
| Gmail Trigger | Gmail 触发器 |
| Google Calendar1 | Google Calendar 工具 |
| Gmail | Gmail 工具 |
| get_Calendar | Google Calendar 工具 |
| create_Calendar1 | Google Calendar 工具 |
| Human agent | Gmail 工具 |
| Code | Code |
| If | IF 判断 |
| Postgres | PostgreSQL |
| Code1 | Code |
| Get Property Media | PostgreSQL |
| construct_image_url | Code |
| Merge | 数据合并 |
| If1 | IF 判断 |
| OpenAI Chat Model3 | OpenAI Chat Model |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复，Webhook 触发。

Webhook触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：32
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发
- Gmail Trigger 触发

## 统计
- 节点总数：32
- 触发节点：2
- 处理节点：29
- 输出节点：1
- 分类：ai-agent
