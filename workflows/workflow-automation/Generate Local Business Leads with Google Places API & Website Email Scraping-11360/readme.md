# Generate Local Business Leads with Google Places API & Website Email Scraping

https://n8nworkflows.xyz/workflows/11360

## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger | 表单触发器 |
| Parse Form Data | 数据设置 |
| Create Search Combinations | 数据设置 |
| Split Into Searches | 数据拆分 |
| Extract Place Info | Code |
| Wait (Rate Limit) | 等待 |
| Get Business Details | HTTP Request |
| Merge Details | 数据设置 |
| Has Website? | IF 判断 |
| Extract Emails & Clean | Code |
| No Website Fallback | 数据设置 |
| Convert to CSV | 转换为文件 |
| Google Places Search1 | HTTP Request |
| Scrape Website1 | HTTP Request |
| Merge | 数据合并 |
| Final Data | 数据设置 |
| Loop Over Items | 分批处理 |
| Loop Over Items1 | 分批处理 |
| Wait | 等待 |

## 触发方式
- Form Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：15
- 输出节点：3
- 分类：workflow-automation
