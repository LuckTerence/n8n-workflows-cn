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
| Get Crypto news from CryptoPanic | HTTP Request |
| Merge all the news together | 数据聚合 |
| Automatically post to X | Twitter |
| Send a news report to Telegram | Telegram |
| Visit the News Page | HTTP Request |
| Extract title and URL | Code |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

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

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- Set the posting interval 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：finance-analysis
