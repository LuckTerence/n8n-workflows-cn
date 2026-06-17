## 简介
**Create Personalized Email Outreach with AI, Telegram Bot & Website Scraping**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10143

---

# Create Personalized Email Outreach with AI, Telegram Bot & Website Scraping


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Edit Fields | 数据设置 |
| HTTP Request | HTTP Request |
| Markdown | Markdown |
| getting link | OpenAI |
| Split Out | 数据拆分 |
| HTTP Request1 | HTTP Request |
| Markdown1 | Markdown |
| Page Sumarize | OpenAI |
| Aggregate | 数据聚合 |
| Send email | Email 发送 |
| Email Craft | OpenAI |
| Delete row(s) | 数据表 |
| Schedule Trigger | 定时触发器 |
| Get row(s)1 | 数据表 |
| If1 | IF 判断 |
| OpenAI Chat Model | OpenAI Chat Model |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| RAG AI Agent | AI Agent |
| List Documents | PostgreSQL 工具 |
| Get File Contents | PostgreSQL 工具 |
| Query Document Rows | PostgreSQL 工具 |
| Embeddings OpenAI2 | OpenAI Embeddings |
| Postgres PGVector Store | PGVector 向量存储 |
| Edit Fields5 | 数据设置 |
| If2 | IF 判断 |
| XML | XML |
| sitemap.xml request | HTTP Request |
| sitemap_index.xml request | HTTP Request |
| crawl4ai | HTTP Request |
| Check how many email created by id | 数据表 |
| answer query | Telegram |
| set maximum email per id | Switch 路由 |
| apologize message | Telegram |
| Code in JavaScript | Code |
| notif email creating | Telegram |
| missing input notif | Telegram |
| make link array to string | Code |
| extract link | Code |
| Links ranking | OpenAI |
| crawl4ai1 | HTTP Request |
| Merge | 数据合并 |
| Edit Fields3 | 数据设置 |
| broken links notif | Telegram |
| flattext | 数据设置 |
| trim markdown to less token | Code |
| sender + signature | 数据设置 |
| calculate how many session | 数据聚合 |
| Finish notif | Telegram |
| insert log | 数据表 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：50
- 触发方式：Telegram 消息触发, 定时触发

## 触发方式
- Telegram Trigger 触发
- Schedule Trigger 触发

## 统计
- 节点总数：50
- 触发节点：2
- 处理节点：35
- 输出节点：13
- 分类：workflow-automation
