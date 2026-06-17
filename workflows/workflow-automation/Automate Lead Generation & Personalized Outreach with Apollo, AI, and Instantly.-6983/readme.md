## 简介
**Automate Lead Generation & Personalized Outreach with Apollo, AI, and Instantly.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6983

---

# Automate Lead Generation & Personalized Outreach with Apollo, AI, and Instantly.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| Emailable (Email Verifier) | HTTP Request |
| Webhook | Webhook |
| Get Agency Record ID | Airtable |
| Business Summary Writer | OpenAI |
| Get Jina Record | Airtable |
| Get Agency Business Information | 数据设置 |
| Update Agency Overview | Airtable |
| Switch | Switch 路由 |
| Get IDC Record | Airtable |
| Get IDC Records | 数据设置 |
| Apollo Search URL Generator | OpenAI |
| Get Apollo Search URL | 数据设置 |
| Update IDC-SearchURL | Airtable |
| Get Agency Record | Airtable |
| Get Email Account Instantly | HTTP Request |
| Split Emails | 数据拆分 |
| Loop Over Items1 | 分批处理 |
| Fill Email List Table | Airtable |
| Get Useful Email Data | 数据设置 |
| Only Active Email Pass | 过滤器 |
| Update Agency Instantly Email Status | Airtable |
| Get Campaign table Record-Instantly | Airtable |
| Get Campaign Details | 数据设置 |
| Create Instantly Campaign | HTTP Request |
| Get Email Acccount Record ID Array | 数据设置 |
| Get Apollo Scraper Record | Airtable |
| Get Scraper Paramter | 数据设置 |
| Apollo Lead Scraper 50k | HTTP Request |
| Get Lead Data | 数据设置 |
| Only Verifed Email | 过滤器 |
| Only with Website | 过滤器 |
| Only with Company Linkedin URL | 过滤器 |
| Only with Linkedin Profile URL | 过滤器 |
| Create Lead in Table | Airtable |
| Increase Limit > 500 | Airtable |
| Verify Dataset Availability1 | Code |
| If Status Empty | IF 判断 |
| Get IDC Record Data | Airtable |
| Get Lead Lists-Email Deliverability | Airtable |
| Get Leads Array | 数据设置 |
| Loop over the Lead Unverified | 分批处理 |
| Split the Leads Array | 数据拆分 |
| Get Lead Record -Email | Airtable |
| Wait 1s | 等待 |
| If deliverable | IF 判断 |
| Update Undeliverable Lead Email | Airtable |
| Update Deliverable Lead Email | Airtable |
| Update Email Verification Status | Airtable |
| Get Lead Lists -Lead Enrichment | Airtable |
| Get Leads Array - Enrichment | 数据设置 |
| Split the Leads Array - Enrichment | 数据拆分 |
| Loop Over Lead for Enrichment | 分批处理 |
| Get Non Enriched Lead Record | Airtable |
| Update Website Summary | Airtable |
| Update Lead Lists - Enrichment Status Record | Airtable |
| Update Lead Status Record -Enrichment | Airtable |
| Get Lead Record ID for Enrichment | Airtable |
| Get Personalization Record ID | Airtable |
| Information LLM | 数据设置 |
| Update Advice | Airtable |
| Get Leads List - For Personalization | Airtable |
| Get Leads For Personalization | 数据设置 |
| Split Leads into Item | 数据拆分 |
| Loop Over Lead for Personalization | 分批处理 |
| Get Lead Record ID for Personalization | Airtable |
| Information For LLM Writer | 数据设置 |
| Update Cold Email | Airtable |
| Cold Email Writer | OpenAI |
| Email Sequence Writer | OpenAI |
| Update Personlization Status Record Lead List | Airtable |
| Get Lead Record for Personalization | Airtable |
| Get Email Information | 数据设置 |
| Remake Update | Airtable |
| Cold Email Writer [Remake] | OpenAI |
| Create Lead Lists | HTTP Request |
| Split Lead Record Array | 数据拆分 |
| Updat Lead Instantly ID | Airtable |
| Get Lead List Record | 数据设置 |
| Get Lead List for Instantly Record | Airtable |
| Get Leads Arrays for Splitting | 数据设置 |
| Loop Over each Lead Record ID | 分批处理 |
| Get Lead Record - Instantly | Airtable |
| Add Lead to Intantly List | HTTP Request |
| Update Instantly Lead List Status | Airtable |
| One (items) Update is enough | 数据限制 |
| Get Campaign Record ID | Airtable |
| Move Leads List to Campaign | HTTP Request |
| If | IF 判断 |
| Get Campaign Records | 数据设置 |
| UpdateCampaign Record Table | Airtable |
| UpdateCampaign Record Table- Failed | Airtable |
| One is Enough for Update the Status | 数据限制 |
| Get Instantly Campaign Analytics ID | Airtable |
| Get Instantly Campaign Analytics | HTTP Request |
| If result available | IF 判断 |
| Arrange the Data | Code |
| Split Return Data Campaign Analytics | 数据拆分 |
| Update Campaign Analytics Table | Airtable |
| Update Campaign Analytics Table - Not Available | Airtable |
| Update Lead List Name-Success | Airtable |
| Update Lead List Name-Failure | Airtable |
| Split Out3 | 数据拆分 |
| Update Latest Linkedin Post - Lead | Airtable |
| Update Website Summary - Lead | Airtable |
| If Email Account Added | IF 判断 |
| Update Campaign Status - Not Email Account | Airtable |
| Get Lead List Record - Qualification | Airtable |
| Get Leads Array - Qualification | 数据设置 |
| Split Leads out for Qualification Loop | 数据拆分 |
| Loop Over Leads for Qualification | 分批处理 |
| Get a Lead for Qualification | Airtable |
| Get Lead Data For Qualification | 数据设置 |
| Qualifier Assistant | OpenAI |
| Qualification Results | 数据设置 |
| Qualified? yes / no | Switch 路由 |
| Update Qualification Status - Yes | Airtable |
| Update Qualification Status - No | Airtable |
| One Record Update is Enough | 数据限制 |
| One Records is Enough for Updates Qualification Status | 数据限制 |
| One Record is Enough to Update Verification Status | 数据限制 |
| If Status 400 Exists | IF 判断 |
| Update Campaign Record - Completed | Airtable |
| Update Campaign Record - Failed | Airtable |
| Get Agency Website Data | jinaAi |
| Scrape Blog Advice | jinaAi |
| Template Writer | OpenAI |
| Search Business Information | perplexity |
| Search Business Information - Lead | perplexity |
| Scrape Linkedin Profile Post - Lead | HTTP Request |
| Profile Post Details - Lead Lists | 数据设置 |
| Aggregate - LinkedIn Post Data | 数据聚合 |
| Turn Into String - LinkedIn Post Data | 数据设置 |
| Linkedin Post Summarizer | OpenAI |
| Merge Data Enrichment | 数据合并 |
| Limit Leads to Airtable - 300 | 数据限制 |
| Update Lead List Qualification Status | Airtable |
| If Qualified | IF 判断 |
| If Qualified & Deliverable? | IF 判断 |
| If qualified & Email Writing & Deliverable | IF 判断 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：139
- 触发节点：1
- 处理节点：129
- 输出节点：9
- 分类：workflow-automation
