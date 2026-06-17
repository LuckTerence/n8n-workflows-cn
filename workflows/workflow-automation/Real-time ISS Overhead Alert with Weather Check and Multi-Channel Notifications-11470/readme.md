## 简介
**Real-time ISS Overhead Alert with Weather Check and Multi-Channel Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 节点数：31 | 难度：⭐⭐⭐ 高级
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
