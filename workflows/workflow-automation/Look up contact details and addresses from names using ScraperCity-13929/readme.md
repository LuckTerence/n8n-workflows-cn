## 简介
**Look up contact details and addresses from names using ScraperCity**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/13929

---

# Look up contact details and addresses from names using ScraperCity


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Execute workflow' | 手动触发 |
| Configure Search Inputs | 数据设置 |
| Start People Finder Scrape | HTTP Request |
| Store Run ID | 数据设置 |
| Wait Before First Status Check | 等待 |
| Poll Loop | 分批处理 |
| Check Scrape Status | HTTP Request |
| Is Scrape Complete? | IF 判断 |
| Wait 60 Seconds Before Retry | 等待 |
| Download Results | HTTP Request |
| Parse CSV Results | Code |
| Remove Duplicate Contacts | 去重 |
| Save Results to Google Sheets | Google Sheets |

## 触发方式
- When clicking 'Execute workflow' 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
