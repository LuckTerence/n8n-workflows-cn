## 简介
**Real-time ISS Overhead Alert with Weather Check and Multi-Channel Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11470

---

# Real-time ISS Overhead Alert with Weather Check and Multi-Channel Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Real-time Check (5 min) | 定时触发器 |
| Daily Predictions (6 AM) | 定时触发器 |
| Weekly Report (Sunday 8 PM) | 定时触发器 |
| Get ISS Detailed (N2YO) | HTTP Request |
| Get Tiangong Position | HTTP Request |
| Calculate All Satellites | Code |
| Any Satellite Nearby? | IF 判断 |
| Get Weather Conditions | HTTP Request |
| Get Astronauts in Space | HTTP Request |
| Observable Conditions? | IF 判断 |
| OpenAI Trivia | OpenAI Chat Model |
| Generate Space Trivia | LLM Chain |
| Format Rich Notification | Code |
| Log to History | Google Sheets |
| Get ISS Pass Predictions | HTTP Request |
| Get Tiangong Predictions | HTTP Request |
| Process All Predictions | Code |
| Format Prediction Report | Code |
| Send Predictions to Telegram | Telegram |
| Send Predictions to Discord | Discord |
| Loop Calendar Events | 分批处理 |
| Add to Google Calendar | Google Calendar |
| Get History Data | Google Sheets |
| Calculate Weekly Statistics | Code |
| OpenAI Report | OpenAI Chat Model |
| Generate Weekly Report | LLM Chain |
| Format Weekly Report | Code |
| Send Weekly to Telegram | Telegram |
| Send Weekly to Discord | Discord |
| Get ISS Position1 | HTTP Request |
| Analyze Observation Conditions1 | Code |
| Send to Discord2 | Discord |
| Send to Telegram3 | Telegram |
| Send to Slack1 | Slack |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：34
- 触发方式：定时触发

## 触发方式
- Real-time Check (5 min) 触发
- Daily Predictions (6 AM) 触发
- Weekly Report (Sunday 8 PM) 触发

## 统计
- 节点总数：34
- 触发节点：3
- 处理节点：17
- 输出节点：14
- 分类：workflow-automation
