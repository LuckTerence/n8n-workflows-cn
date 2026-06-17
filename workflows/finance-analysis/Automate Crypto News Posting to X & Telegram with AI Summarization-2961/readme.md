## 简介
**Automate Crypto News Posting to X & Telegram with AI Summarization**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2961

---

# Automate Crypto News Posting to X & Telegram with AI Summarization


## 节点清单

| 节点 | 类型 |
|------|------|
| No Operation, do nothing | 空操作 |
| Summary news GPT | OpenAI |
| ContentExtraction GPT3.5 | OpenAI |
| Set the posting interval | 定时触发器 |
| Get Crypto news from  CryptoPanic | HTTP Request |
| Merge all the news together | 数据聚合 |
| Automatically post to X | Twitter |
| Send a news report to Telegram | Telegram |
| Visit the News Page | HTTP Request |
| Extract title and URL | Code |

## 触发方式
- Set the posting interval 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：finance-analysis
