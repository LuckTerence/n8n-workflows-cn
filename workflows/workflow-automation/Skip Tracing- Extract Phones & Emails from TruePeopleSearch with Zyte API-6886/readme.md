## 简介
**Skip Tracing: Extract Phones & Emails from TruePeopleSearch with Zyte API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6886

---

# Skip Tracing: Extract Phones & Emails from TruePeopleSearch with Zyte API


## 节点清单

| 节点 | 类型 |
|------|------|
| Name | Code |
| Age | Code |
| Primary Phone | Code |
| Other numbers | Code |
| Emails | Code |
| Current Address | Code |
| RelativeProfile | Code |
| RelativeName | Code |
| RelativeAge | Code |
| RelativePrimaryPhone | Code |
| Relative Other numbers | Code |
| RelativeEmails | Code |
| Relative Current Address | Code |
| Webhook | Webhook |
| Get row(s) in sheet | Google Sheets |
| Add conditions to filter already processed rows | 过滤器 |
| Update Sheet on Errors | Google Sheets |
| Limit number of rows to process | 数据限制 |
| Make HTTP Request for SearchURL | HTTP Request |
| Find the matching person profile from search results | Code |
| If found | IF 判断 |
| Update row in sheet with PersonURL | Google Sheets |
| Update row in sheet with errors | Google Sheets |
| Make HTTP Request for PersonURL | HTTP Request |
| Update Errors in Google Sheets | Google Sheets |
| Set html to scrape data | 数据设置 |
| If phone numbers not found | IF 判断 |
| Update Scraped Data in sheet | Google Sheets |
| Update Scraped data with RelativeURL into Sheets | Google Sheets |
| Check if RelativeURL exists | IF 判断 |
| Update errors Google Sheets | Google Sheets |
| Make HTTP Request for RelativeURL | HTTP Request |
| Update row in sheet with http error | Google Sheets |
| Set relativeprofile page html to scrape data | 数据设置 |
| Update Relative scraped data to sheets | Google Sheets |
| Their RelativeProfile | Code |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：36
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：36
- 触发节点：1
- 处理节点：32
- 输出节点：3
- 分类：workflow-automation
