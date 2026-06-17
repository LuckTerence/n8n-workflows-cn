## 简介
**Plant Care Reminder with OpenWeather, Sheets and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9953

---

# Plant Care Reminder with OpenWeather, Sheets and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Read plants | Google Sheets |
| Read settings | Google Sheets |
| DecideDue | Code |
| OpenWeather request | HTTP Request |
| WeatherGate | Code |
| If | IF 判断 |
| Set Weather Tag | 数据设置 |
| Set DecideTag | 数据设置 |
| Merge | 数据合并 |
| ¿Pending task? | IF 判断 |
| Send Final Message No Dues | Telegram |
| Vacation Mode | IF 判断 |
| Send Final Message No Dues1 | Telegram |
| Send Dues | Telegram |
| Webhook | Webhook |
| Prepare Data | Code |
| Append Log | Google Sheets |
| Respond to Webhook | 响应 Webhook |
| HTML | Code |
| Edit Fields | 数据设置 |
| Update Water | Google Sheets |
| Update Fert | Google Sheets |
| If1 | IF 判断 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Webhook触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：24
- 触发方式：定时触发, Webhook 触发

## 触发方式
- Schedule Trigger 触发
- Webhook 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：17
- 输出节点：5
- 分类：workflow-automation
