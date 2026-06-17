## 简介
**Save Mastodon Bookmarks to Raindrop Automatically**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4800

---

# Save Mastodon Bookmarks to Raindrop Automatically


## 节点清单

| 节点 | 类型 |
|------|------|
| Allows manual testing of the workflow | 手动触发 |
| Triggers the workflow on a set interval | 定时触发器 |
| Retrieves the last processed min_id to avoid duplicates | Code |
| Makes authenticated request to Mastodon’s bookmarks API | HTTP Request |
| Ensures the response has bookmarks before continuing | IF 判断 |
| Extracts pagination data (like next min_id) from HTTP headers | Code |
| Saves the new min_id to workflow static data | Code |
| Splits API response into individual bookmark items | 数据拆分 |
| Filters out invalid or incomplete bookmark data | IF 判断 |
| Saves valid bookmark using post metadata (e.g., title, card.url) | raindrop |
| Saves bookmark using alternate fields if card data is missing | raindrop |



## 功能说明

Save Mastodon Bookmarks to Raindrop Automatically。

定时触发、手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：手动触发, 定时触发

## 触发方式
- Allows manual testing of the workflow 触发
- Triggers the workflow on a set interval 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
