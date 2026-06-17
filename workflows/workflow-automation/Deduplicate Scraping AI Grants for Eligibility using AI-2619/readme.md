## 简介
**Deduplicate Scraping AI Grants for Eligibility using AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2619

---

# Deduplicate Scraping AI Grants for Eligibility using AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Grants to List | 数据拆分 |
| Get Grant Details | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| Summarize Synopsis | 信息提取器 |
| Eligibility Factors | 信息提取器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Merge | 数据合并 |
| Save to Tracker | Airtable |
| Only New Grants | 去重 |
| AI Grants since Yesterday | HTTP Request |
| Get New Eligible Grants Today | Airtable |
| Generate Email | HTML |
| Everyday @ 9am | 定时触发器 |
| Everyday @ 8.30am | 定时触发器 |
| Get Subscribers | Airtable |
| Send Subscriber Email | Email 发送 |

## 触发方式
- Everyday @ 9am 触发
- Everyday @ 8.30am 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
