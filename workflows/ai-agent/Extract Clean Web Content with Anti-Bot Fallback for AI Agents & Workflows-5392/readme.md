## 简介
**Extract Clean Web Content with Anti-Bot Fallback for AI Agents & Workflows**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5392

---

# Extract Clean Web Content with Anti-Bot Fallback for AI Agents & Workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| Content Extractor | webpageContentExtractor |
| Try Antibot Evasion | IF 判断 |
| Scrape.do | HTTP Request |
| Server Error | 停止并报错 |
| Not 404 | IF 判断 |
| Not Found | 停止并报错 |
| Simple Scraper | HTTP Request |
| Full Text | IF 判断 |
| Fulltext Output | 数据设置 |
| Summary Output | 数据设置 |
| Is Binary | IF 判断 |
| ContentType Error | 停止并报错 |
| Workflow Call | 执行工作流触发器 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动或子流程调用

## 触发方式
- Workflow Call 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：10
- 输出节点：2
- 分类：ai-agent
