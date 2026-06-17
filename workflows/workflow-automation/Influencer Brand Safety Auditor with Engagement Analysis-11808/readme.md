## 简介
**Influencer Brand Safety Auditor with Engagement Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/11808

---

# Influencer Brand Safety Auditor with Engagement Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Influencer Audit Form | 表单触发器 |
| Workflow Configuration | 数据设置 |
| Store Audit Request | Google Sheets |
| Apify Instagram Scraper | HTTP Request |
| Calculate Engagement Rate | Code |
| Aggregate Captions | 数据聚合 |
| AI Content Safety Audit | OpenAI |
| Send Audit Report to Slack | Slack |
| Store Audit Results | Google Sheets |

## 触发方式
- Influencer Audit Form 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
