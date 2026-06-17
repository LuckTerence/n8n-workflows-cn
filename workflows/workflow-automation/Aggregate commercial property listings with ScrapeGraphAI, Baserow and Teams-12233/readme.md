## 简介
**Aggregate commercial property listings with ScrapeGraphAI, Baserow and Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12233

---

# Aggregate commercial property listings with ScrapeGraphAI, Baserow and Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Trigger | 定时触发器 |
| Prepare URL List | Code |
| Split URLs | 分批处理 |
| Scrape Listings | ScrapeGraph AI |
| Collect Listings | 数据合并 |
| Normalise Listings | Code |
| Loop Listings | 分批处理 |
| Check Existing (Baserow List) | baserow |
| Merge Listing & Result | 数据合并 |
| Determine Action | Code |
| Need Create? | IF 判断 |
| Create Row | baserow |
| Create Message | 数据设置 |
| Teams – New Listing | Teams |
| Need Update? | IF 判断 |
| Update Row | baserow |
| Update Message | 数据设置 |
| Teams – Update | Teams |

## 触发方式
- Weekly Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
