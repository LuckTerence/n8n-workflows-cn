## 简介
**Automated Forex News Alert System with Forex Factory and Telegram**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8340

---

# Automated Forex News Alert System with Forex Factory and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Calendar Trigger | googleCalendarTrigger |
| If | IF 判断 |
| To Number | 数据设置 |
| Get Actual Data? | IF 判断 |
| Actual, Forecast Value | 数据设置 |
| Delete %KMBT, To Number | 数据设置 |
| 'Actual' less than 'Forecast' is good for currency? | IF 判断 |
| IF Has Forecast | IF 判断 |
| No Operation, do nothing1 | 空操作 |
| Get News Details | 数据设置 |
| Scrape News Link | Airtop |
| Wait 10s | 等待 |
| Wait 5s | 等待 |
| Less Good | Telegram |
| Greater Good | Telegram |
| No Operation, do nothing | 空操作 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警。

手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：16
- 触发方式：手动或子流程调用

## 触发方式
- Google Calendar Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：devops
