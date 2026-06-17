# Skip Tracing: Extract Phones & Emails from TruePeopleSearch with Zyte API

https://n8nworkflows.xyz/workflows/6886

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

## 触发方式
- Webhook 触发

## 统计
- 节点总数：36
- 触发节点：1
- 处理节点：32
- 输出节点：3
- 分类：workflow-automation
