## 简介
**Scrape every url on the web without getting blocked by Anti-Bot technologies with Scrappey**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2299

---

# Scrape every url on the web without getting blocked by Anti-Bot technologies with Scrappey


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Test Data | 数据设置 |
| Scrape website with Scrappey | HTTP Request |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：3
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：3
- 触发节点：1
- 处理节点：1
- 输出节点：1
- 分类：devops
