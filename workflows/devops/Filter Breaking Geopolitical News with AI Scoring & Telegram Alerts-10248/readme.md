## 简介
**Filter Breaking Geopolitical News with AI Scoring & Telegram Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10248

---

# Filter Breaking Geopolitical News with AI Scoring & Telegram Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Every 30 Minutes | 定时触发器 |
| NYT RSS Feed | RSS Feed |
| TOI RSS Feed | RSS Feed |
| Al Jazeera RSS Feed | RSS Feed |
| BBC RSS Feed | RSS Feed |
| Dynamic Filter | Code |
| Send Breaking News Alert | Telegram |
| Breaking News Analyzer | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| If | IF 判断 |
| SCMP RSS Feed | RSS Feed |
| NDTV RSS Feed | RSS Feed |
| Check for Duplicates | 数据表 |
| Record Analyzed Article | 数据表 |
| Cleanup Old Records | 数据表 |
| Merge | 数据合并 |
| Aggregate Alerts | Code |
| Dynamic AI Prompt Generator | Code |
| RSS_Cleanup_Node | Code |
| Load Config from Google Drive | HTTP Request |
| Re-attach Config | Code |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

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

- 节点总数：22
- 触发方式：定时触发

## 触发方式
- Every 30 Minutes 触发
- NYT RSS Feed 触发
- TOI RSS Feed 触发
- Al Jazeera RSS Feed 触发
- BBC RSS Feed 触发
- SCMP RSS Feed 触发
- NDTV RSS Feed 触发

## 统计
- 节点总数：22
- 触发节点：7
- 处理节点：13
- 输出节点：2
- 分类：devops
