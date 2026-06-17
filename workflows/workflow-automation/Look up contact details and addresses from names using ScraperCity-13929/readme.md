## 简介
**Look up contact details and addresses from names using ScraperCity**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- When clicking 'Execute workflow' 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
