## 简介
**Complete B2B Sales Pipeline: Apollo Lead Gen, Mailgun Outreach & AI Reply Management**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7410

---

# Complete B2B Sales Pipeline: Apollo Lead Gen, Mailgun Outreach & AI Reply Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Limit | 数据限制 |
| Merge | 数据合并 |
| Time Zone | Code |
| Sender Email | Code |
| Switch | Switch 路由 |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| Loop Over Items1 | 分批处理 |
| Wait1 | 等待 |
| Schedule Trigger1 | 定时触发器 |
| If3 | IF 判断 |
| Mailgun | mailgun |
| Mailgun1 | mailgun |
| General anlysis | OpenAI |
| Limit1 | 数据限制 |
| OpenAI Chat Model | OpenAI Chat Model |
| No Operation, do nothing | 空操作 |
| Supabase2 | Supabase |
| If2 | IF 判断 |
| No Operation, do nothing2 | 空操作 |
| Supabase3 | Supabase |
| Supabase4 | Supabase |
| Structured Output Parser | 结构化输出解析器 |
| Code | Code |
| Schedule Trigger3 | 定时触发器 |
| Supabase11 | Supabase |
| If1 | IF 判断 |
| Evualute when the mail was sent | Code |
| Sort | 数据排序 |
| Sort1 | 数据排序 |
| Sort2 | 数据排序 |
| Limit2 | 数据限制 |
| Switch5 | Switch 路由 |
| Loop Over Items7 | 分批处理 |
| Wait7 | 等待 |
| Loop Over Items10 | 分批处理 |
| Wait10 | 等待 |
| Mailgun6 | mailgun |
| Mailgun7 | mailgun |
| Supabase12 | Supabase |
| Supabase14 | Supabase |
| Schedule Trigger4 | 定时触发器 |
| No Operation, do nothing1 | 空操作 |
| Supabase13 | Supabase |
| If | IF 判断 |
| Evualute when the mail was sent1 | Code |
| Sort3 | 数据排序 |
| Limit4 | 数据限制 |
| Switch6 | Switch 路由 |
| Loop Over Items8 | 分批处理 |
| Wait8 | 等待 |
| Loop Over Items11 | 分批处理 |
| Wait11 | 等待 |
| Mailgun8 | mailgun |
| Mailgun9 | mailgun |
| Supabase15 | Supabase |
| Supabase16 | Supabase |
| Schedule Trigger6 | 定时触发器 |
| No Operation, do nothing4 | 空操作 |
| research about company | OpenAI |
| create email sequence | AI Agent |
| Get many rows | Supabase |
| Your leads table | Supabase |
| Create URL | Code |
| Extract Info | 数据设置 |
| Only Keep Verified Emails | 过滤器 |
| Download File1 | Telegram |
| Transcribe1 | OpenAI |
| Text1 | 数据设置 |
| Voice or Text1 | Switch 路由 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Select already scraped mails | PostgreSQL |
| Keep only the new leads | compareDatasets |
| Already scraped | 空操作 |
| Create rows with new leads | Supabase |
| Set Telegram message | 数据设置 |
| Confirmation message | Telegram |
| User message | Telegram 触发器 |
| Generate query payload | 数据设置 |
| Scraper agent | AI Agent |
| Run an Actor | apify |
| Limit3 | 数据限制 |
| Structured Output Parser1 | 结构化输出解析器 |
| Gmail Trigger | Gmail 触发器 |
| Get a message | Email 发送 |
| Execute a SQL query | PostgreSQL |
| Set replied = Yes | PostgreSQL |
| Only from email campaigns | 过滤器 |
| extract email | Code |
| Get Email History | Gmail 工具 |
| Check Sent History | Gmail 工具 |
| Email Response Parser | 结构化输出解析器 |
| Professional Email Response Agent | AI Agent |
| Create Draft Response | Email 发送 |
| Anthropic Chat Model1 | OpenAI Chat Model |



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
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：96
- 触发方式：定时触发, Telegram 消息触发

## 触发方式
- Schedule Trigger1 触发
- Schedule Trigger3 触发
- Schedule Trigger4 触发
- Schedule Trigger6 触发
- User message 触发
- Gmail Trigger 触发

## 统计
- 节点总数：96
- 触发节点：6
- 处理节点：86
- 输出节点：4
- 分类：workflow-automation
