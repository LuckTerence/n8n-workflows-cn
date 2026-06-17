## 简介
**Domain-Specific Web Content Crawler with Depth Control & Text Extraction**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8852

---

# Domain-Specific Web Content Crawler with Depth Control & Text Extraction


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Loop Links (Batches) | 分批处理 |
| IF Crawl Depth OK? | IF 判断 |
| Extract Body & Links | HTML |
| Attach URL/Depth to HTML | Code |
| Fetch HTML Page | HTTP Request |
| Seed Root Crawl Item | 数据合并 |
| Collect Pages & Emit When Done | Code |
| Store Page Data | 数据设置 |
| Merge Web Pages | 数据合并 |
| Combine & Chunk | Code |
| Respond to Webhook | 响应 Webhook |
| Init Globals | Code |
| Init Crawl Params | 数据设置 |
| Requeue Link Item | Code |
| Queue & Dedup Links | Code |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：16
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
