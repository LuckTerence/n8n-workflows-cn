## 简介
**Forex News & Sentiment Telegram Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4659

---

# Forex News & Sentiment Telegram Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Merge | 数据合并 |
| RSS Read - GOOGLE | RSS Feed |
| RSS Read - FXSTREET | RSS Feed |
| RSS Read - fxstreet news | RSS Feed |
| RSS Read - DAILYFX technical | RSS Feed |
| RSS Read - DAILYFX fundamental | RSS Feed |
| RSS Read - DAILYFX forexnews | RSS Feed |
| RSS Read - DAILYFX forex articles | RSS Feed |
| RSS Read - FOREX LIVE technicals | RSS Feed |
| RSS Read - FOREX LIVE central banks | RSS Feed |
| RSS Read - FOREX LIVE forexorders | RSS Feed |
| Filter | 过滤器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Code | Code |
| Telegram | Telegram |
| EURUSD News and Sentiment Analyst | AI Agent |
| Schedule Trigger | 定时触发器 |



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

- 节点总数：17
- 触发方式：定时触发

## 触发方式
- RSS Read - GOOGLE 触发
- RSS Read - FXSTREET 触发
- RSS Read - fxstreet news 触发
- RSS Read - DAILYFX technical 触发
- RSS Read - DAILYFX fundamental 触发
- RSS Read - DAILYFX forexnews 触发
- RSS Read - DAILYFX forex articles 触发
- RSS Read - FOREX LIVE technicals 触发
- RSS Read - FOREX LIVE central banks 触发
- RSS Read - FOREX LIVE forexorders 触发
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：11
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
