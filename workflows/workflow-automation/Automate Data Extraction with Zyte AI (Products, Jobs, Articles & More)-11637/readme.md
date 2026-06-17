## 简介
**Automate Data Extraction with Zyte AI (Products, Jobs, Articles & More)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11637

---

# Automate Data Extraction with Zyte AI (Products, Jobs, Articles & More)


## 节点清单

| 节点 | 类型 |
|------|------|
| Main form submission | 表单触发器 |
| Product Extraction Goal | Switch 路由 |
| Format Output [ Single || List ] | 数据设置 |
| HTTP Node: [List] Get Current Page | HTTP Request |
| HTTP Node: [Current Page] Get Item URLs | HTTP Request |
| [Current Page] Split Items | 数据拆分 |
| [Current Page] Item Loop | 分批处理 |
| HTTP Node: [Current Page] Get Item Details | HTTP Request |
| [Details-All] Init State | 数据设置 |
| [Details-All] Merge Pages | 数据合并 |
| HTTP Node: [Details-All] Crawler (Phase 1) | HTTP Request |
| [Details-All] URL Collector | Code |
| [Details-All] More Pages? | IF 判断 |
| [Details-All] Set Next URL | 数据设置 |
| [Details-All] Unpack List (Phase 2) | Code |
| [Details-All] Batch Processor | 分批处理 |
| HTTP Node: [Details-All] Get Details | HTTP Request |
| [Details-All] Accumulator | Code |
| [Details-All] Final Output | Code |
| HTTP Node: [Single Item] Get Details | HTTP Request |
| Route by Category | Switch 路由 |
| Zyte Config Generator | Code |
| [List-All] Get Item List | HTTP Request |
| [List-All] List Accumulator | Code |
| [List-All] Init State | 数据设置 |
| [List-All] Merge Pages | 数据合并 |
| HTTP Node: [List-All] Get Page URLs | HTTP Request |
| [List-All] Page Controller | Code |
| [List-All] Check Next Page | IF 判断 |
| [List-All] Final Output | Code |
| [List-All] Set Next URL | 数据设置 |
| HTTP BrowserHtml | HTTP Request |
| HTTP Google Search: Serp | HTTP Request |
| HTTP Response Body | HTTP Request |
| HTTP Node: Capture Page Screenshot | HTTP Request |
| HTTP Node: Capture Network API | HTTP Request |
| Convert to File ( Image ) | 转换为文件 |
| Custom Output | 数据设置 |
| HTTP Node: Infinite Scroll | HTTP Request |
| serp response | 数据设置 |
| Extracted AI Output | 转换为文件 |
| General Extract Goal | Switch 路由 |
| General Extraction Goal Form | 表单 |
| AI Extraction Goal Form | 表单 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据（Data)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：44
- 触发方式：表单提交触发

## 触发方式
- Main form submission 触发

## 统计
- 节点总数：44
- 触发节点：1
- 处理节点：29
- 输出节点：14
- 分类：workflow-automation
