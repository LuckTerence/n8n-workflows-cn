## 简介
**AI-Powered Content Gap Analysis using ScrapeGraphAI and Strategic Planning**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6741

---

# AI-Powered Content Gap Analysis using ScrapeGraphAI and Strategic Planning


## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Content Analysis Trigger | 定时触发器 |
| AI-Powered Competitor Content Scraper | ScrapeGraph AI |
| Secondary Competitor Content Scraper | ScrapeGraph AI |
| Competitor Data Merger and Processor | Code |
| Our Content Library Analyzer | ScrapeGraph AI |
| Advanced Content Gap Identifier | Code |
| SEO Keyword Mapper and Strategy Builder | Code |
| Strategic Content Planner and Roadmap Generator | Code |
| Google Sheets Editorial Calendar | Google Sheets |
| Editorial Calendar Generator with Timeline | Code |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，定时执行。

定时触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- Weekly Content Analysis Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
