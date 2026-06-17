## 简介
**Automated Oncrawl Sitemap URL Submission to Google Indexing API & IndexNow**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11837

---

# Automated Oncrawl Sitemap URL Submission to Google Indexing API & IndexNow


## 节点清单

| 节点 | 类型 |
|------|------|
| Split In Batches (IndexNow ≤500)1 | 分批处理 |
| Wait (IndexNow jitter)1 | 等待 |
| Get Orphan Pages | HTTP Request |
| Webhook | Webhook |
| Post - Get Sitemaps | HTTP Request |
| Config | 数据设置 |
| Assign mandatory sitemap fields | 数据设置 |
| Filter: lastmod within DAYS_BACK | Code |
| Split Out | 数据拆分 |
| Get sitemap.xml | HTTP Request |
| Convert sitemap to JSON | XML |
| Get content-specific sitemaps | 数据拆分 |
| Get content of each sitemap | HTTP Request |
| convert page data to JSON | XML |
| Force urlset.url to array | 数据设置 |
| Sort | 数据排序 |
| Build IndexNow payload | Code |
| IndexNow Submit | HTTP Request |
| Gate: IndexNow | Code |
| Gate: Google | Code |
| Wait2 | 等待 |
| Switch | Switch 路由 |
| Loop Over Items | 分批处理 |
| Check status | HTTP Request |
| is new? | IF 判断 |
| URL Updated | HTTP Request |
| Config - Orphan | 数据设置 |
| Merge | 数据合并 |
| Get Crawl over crawl | HTTP Request |
| Split Out - Orphan1 | 数据拆分 |
| Split Out - Orphan2 | 数据拆分 |
| Split Out - Coc1 | 数据拆分 |
| Merge1 | 数据合并 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：33
- 触发节点：1
- 处理节点：24
- 输出节点：8
- 分类：devops
