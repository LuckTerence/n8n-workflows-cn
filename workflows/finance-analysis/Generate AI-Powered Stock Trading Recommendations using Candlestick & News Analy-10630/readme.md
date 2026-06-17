## 简介
**Generate AI-Powered Stock Trading Recommendations using Candlestick & News Analysis**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10630

---

# Generate AI-Powered Stock Trading Recommendations using Candlestick & News Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| 15 min Interval | HTTP Request |
| 1 min Interval | HTTP Request |
| 1 hour Interval | HTTP Request |
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| Code in JavaScript | Code |
| News Aggregator | HTTP Request |
| Message a model | OpenAI Chat Model |
| Merge1 | 数据合并 |
| Aggregate1 | 数据聚合 |
| AI Agent | AI Agent |
| Google Gemini Chat Model | OpenAI Chat Model |
| Send a text message | Telegram |
| Account Check | Switch 路由 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：15
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：9
- 输出节点：5
- 分类：finance-analysis
