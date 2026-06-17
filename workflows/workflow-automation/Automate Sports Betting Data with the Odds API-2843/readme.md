## 简介
**Automate Sports Betting Data with the Odds API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2843

---

# Automate Sports Betting Data with the Odds API


## 节点清单

| 节点 | 类型 |
|------|------|
| Morning Trigger To Pull Data At 7:00am | 定时触发器 |
| Evening Trigger To Pull Data At 11:00pm | 定时触发器 |
| Retrieve Data Of Upcoming Sport Events For The Day | HTTP Request |
| Create Records Of Upcoming Events For The Day | Airtable |
| Retrieve Sport Results Data At The End Of The Day | HTTP Request |
| Combine Sport Results With Upcoming Events Records By Matching ID | 数据合并 |
| Update Table Records With Scores And Results For Sport Events | Airtable |



## 功能说明

API 集成接口，连接和编排多个第三方服务，定时执行。

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

- 节点总数：7
- 触发方式：定时触发

## 触发方式
- Morning Trigger To Pull Data At 7:00am 触发
- Evening Trigger To Pull Data At 11:00pm 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
