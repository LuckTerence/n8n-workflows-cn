## 简介
**Discover & Enrich Decision-Makers with Apollo and Human Verification**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3830

---

# Discover & Enrich Decision-Makers with Apollo and Human Verification


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Sheets Trigger | Google Sheets 触发器 |
| Apollo Organization Enrichment | HTTP Request |
| Create Apollo People Search URL | Code |
| Loop Over Items (1000 per Batch) | 分批处理 |
| Apollo Find Decision Makers | HTTP Request |
| Add Contacts | Google Sheets |
| Apollo Enrich Decision Makers | HTTP Request |
| Create Apollo People Enrichment Payload | Code |
| Enrich Contacts | Google Sheets |
| Loop Over Items For Bulk Enrichment (10 per batch) | 分批处理 |
| Determine Contact's Department | OpenAI |
| Apollo Organization Search | HTTP Request |
| Add Company Website | Google Sheets |
| Approve Company Website | Slack |
| Add Company Details | Google Sheets |
| Select Unprocessed Companies | 过滤器 |
| Is Domain Already Provided? | IF 判断 |
| Summarize Core Business | OpenAI |
| Split Out Batched Decision Maker Response | 数据拆分 |
| Split Out Batched Enrichment Response | 数据拆分 |
| Send Weekly Report | Slack |
| Retrieve Verified Leads | Google Sheets |
| Derive Past Week's Lead Gen. Metrics | Code |
| Weekly Report Trigger | 定时触发器 |
| Merge Rows Which Now All Contain Domains | 数据合并 |

## 触发方式
- Google Sheets Trigger 触发
- Weekly Report Trigger 触发

## 统计
- 节点总数：25
- 触发节点：2
- 处理节点：17
- 输出节点：6
- 分类：workflow-automation
