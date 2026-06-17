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



## 功能说明

数据采集工具，自动抓取网页或 API 数据，定时执行。

定时触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：定时触发

## 触发方式
- Weekly Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
