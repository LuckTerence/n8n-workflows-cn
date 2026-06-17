## 简介
**Real-Time Cryptocurrency Price Monitor with CoinGecko & Multi-Channel Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7705

---

# Real-Time Cryptocurrency Price Monitor with CoinGecko & Multi-Channel Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| 24/7 Crypto Trigger | 定时触发器 |
| Read Crypto Watchlist | Google Sheets |
| Parse Crypto Data | Code |
| Fetch Live Crypto Price | HTTP Request |
| Smart Crypto Alert Logic | Code |
| Check Crypto Alert Conditions | IF 判断 |
| Send Crypto Email Alert | Email 发送 |
| Send Telegram Crypto Alert | Telegram |
| Send Discord Crypto Alert | Discord |
| Update Crypto Alert History | Google Sheets |
| Crypto Alert Status Check | IF 判断 |
| Success Notification | Email 发送 |
| Error Notification | Email 发送 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警。

手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动或子流程调用

## 触发方式
- 24/7 Crypto Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：6
- 输出节点：6
- 分类：workflow-automation
