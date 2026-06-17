# Generate Sales Leads with Yelp & Trustpilot Scraping + AI-Powered Email Outreach

https://n8nworkflows.xyz/workflows/4912

## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger - Get User Input | 表单触发器 |
| AI Location Analyzer | AI Agent |
| Split Sub-locations | Code |
| Loop Yelp Locations | 分批处理 |
| Yelp Scraper | HTTP Request |
| Check Yelp Scrape Progress | HTTP Request |
| Wait (1 min) Yelp Completion | 等待 |
| Verify Yelp Ready | IF 判断 |
| If Yelp Has Records | IF 判断 |
| Fetch Yelp Results | HTTP Request |
| Save Yelp Data to Sheet | Google Sheets |
| Clean Unique Websites | Code |
| Read Yelp Sheet Websites | Google Sheets |
| Make Trustpilot URLs | Code |
| Remove Duplicate TP URLs | Code |
| Loop Trustpilot URLs | 分批处理 |
| Trigger Trustpilot Scraper | HTTP Request |
| Check Trustpilot Scrape Progress | HTTP Request |
| Verify Trustpilot Scraper Ready | IF 判断 |
| Wait (1 min) Trustpilot Completion | 等待 |
| If Trustpilot Has Records | IF 判断 |
| Download Trustpilot Data | HTTP Request |
| Save Trustpilot Data to Sheet | Google Sheets |
| Read Emails from Trustpilot Sheet | Google Sheets |
| Get Unique Emails | Code |
| AI Generate Email Content | AI Agent |
| Parse Email JSON | Code |
| Send Outreach Email | Email 发送 |
| Gemini - Location AI Model | OpenAI Chat Model |
| Claude - Email AI Model | OpenAI Chat Model |

## 触发方式
- Form Trigger - Get User Input 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：22
- 输出节点：7
- 分类：workflow-automation
