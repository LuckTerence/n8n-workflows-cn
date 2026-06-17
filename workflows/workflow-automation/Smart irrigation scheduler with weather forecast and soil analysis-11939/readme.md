## 简介
**Smart irrigation scheduler with weather forecast and soil analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11939

---

# Smart irrigation scheduler with weather forecast and soil analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Morning Check | 定时触发器 |
| Manual Override Trigger | Webhook |
| Merge Triggers | 数据合并 |
| Define Irrigation Zones | 数据设置 |
| Split Zones | 数据拆分 |
| Get Current Weather | openWeatherMap |
| Get 5-Day Forecast | openWeatherMap |
| Merge Weather Data | 数据合并 |
| Analyze Irrigation Need | Code |
| Filter Zones Needing Water | 过滤器 |
| Aggregate All Results | 数据聚合 |
| Generate Irrigation Schedule | Code |
| Has Irrigation Tasks? | IF 判断 |
| Log to Google Sheets | Google Sheets |
| Send IoT Commands | HTTP Request |
| Send Slack Report | Slack |
| Log No Action | 数据设置 |
| Respond to Webhook | 响应 Webhook |



## 功能说明

日历日程管理，自动创建事件或发送提醒，定时执行。

定时触发、Webhook触发，通过 在线表格 + Slack + HTTP API 实现自动化。

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
- 触发方式：定时触发, Webhook 触发

## 触发方式
- Daily Morning Check 触发
- Manual Override Trigger 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：13
- 输出节点：3
- 分类：workflow-automation
