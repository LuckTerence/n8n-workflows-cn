## 简介
**Find business emails from contact names and domains using ScraperCity**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13858

---

# Find business emails from contact names and domains using ScraperCity


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Execute workflow' | 手动触发 |
| Set Contact List | 数据设置 |
| Submit Email Finder Job | HTTP Request |
| Store Run ID | 数据设置 |
| Wait Before First Poll | 等待 |
| Polling Loop | 分批处理 |
| Check Job Status | HTTP Request |
| Is Job Complete? | IF 判断 |
| Wait 60 Seconds Before Retry | 等待 |
| Download Email Results | HTTP Request |
| Parse and Format Results | Code |
| Filter Emails Found | 过滤器 |
| Write Results to Google Sheets | Google Sheets |

## 触发方式
- When clicking 'Execute workflow' 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
