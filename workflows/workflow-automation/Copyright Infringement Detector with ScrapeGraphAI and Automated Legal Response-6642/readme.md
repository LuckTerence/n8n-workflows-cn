## 简介
**Copyright Infringement Detector with ScrapeGraphAI and Automated Legal Response**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6642

---

# Copyright Infringement Detector with ScrapeGraphAI and Automated Legal Response


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| ScrapeGraphAI Web Search | ScrapeGraph AI |
| Content Comparer | Code |
| Infringement Detector | Code |
| Legal Action Trigger | IF 判断 |
| Brand Protection Alert | Telegram |
| Monitoring Alert | Telegram |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
