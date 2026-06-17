## 简介
**Get a daily financial news digest on Telegram with Mistral and RSS feeds**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14172

---

# Get a daily financial news digest on Telegram with Mistral and RSS feeds


## 节点清单

| 节点 | 类型 |
|------|------|
| Digest Complete | 数据设置 |
| Log Digest to Sheets | Google Sheets |
| Send to Telegram | HTTP Request |
| Extract Digest | 数据设置 |
| Generate Digest (NIM) | HTTP Request |
| No Stories Alert | HTTP Request |
| Any Stories Today? | IF 判断 |
| 📋 RSS Feed Config1 | 数据设置 |
| ⏰ Schedule Trigger1 | 定时触发器 |
| Generate Feed Items | Code |
| Loop Over Feeds | 分批处理 |
| Read RSS Feed | RSS Feed |
| Tag Articles | Code |
| Aggregate and Rank | Code |
| Is Processing Done? | IF 判断 |
| Build NIM Payload | Code |
| Build Telegram Payload | Code |
| Telegram Send OK? | IF 判断 |
| Build Error Log Row | 数据设置 |
| Log Error to Sheets | Google Sheets |
| Digest Failed | 数据设置 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：21
- 触发方式：定时触发

## 触发方式
- ⏰ Schedule Trigger1 触发
- Read RSS Feed 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：16
- 输出节点：3
- 分类：finance-analysis
