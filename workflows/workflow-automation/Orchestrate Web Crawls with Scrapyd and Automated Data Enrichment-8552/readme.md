## 简介
**Orchestrate Web Crawls with Scrapyd and Automated Data Enrichment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8552

---

# Orchestrate Web Crawls with Scrapyd and Automated Data Enrichment


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| job_list | HTTP Request |
| filter_job | Code |
| check_job_status | IF 判断 |
| Wait3 | 等待 |
| check_items | HTTP Request |
| run_job | HTTP Request |
| screenshots | HTTP Request |
| job_log | HTTP Request |
| DL-html | HTTP Request |
| HTML | HTTP Request |
| loop-html | 分批处理 |
| DL-screenshots | HTTP Request |
| loop-screenshots | 分批处理 |
| combine-screenshots | 数据聚合 |
| combine-html | 数据聚合 |
| Split HTML | 数据拆分 |
| Split-screenshot | 数据拆分 |
| Respond to Webhook | 响应 Webhook |
| If-job-check | IF 判断 |
| Filter-result | Code |



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

- 节点总数：21
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：11
- 输出节点：9
- 分类：workflow-automation
