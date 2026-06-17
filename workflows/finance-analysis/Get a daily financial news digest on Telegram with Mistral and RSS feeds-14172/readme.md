## 简介
**Get a daily financial news digest on Telegram with Mistral and RSS feeds**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：20 | 难度：⭐⭐⭐ 高级
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

## 触发方式
- ⏰ Schedule Trigger1 触发
- Read RSS Feed 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：16
- 输出节点：3
- 分类：finance-analysis
