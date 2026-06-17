## 简介
**Import Research Papers from Telegram to Zotero with AI Abstract Summaries**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7676

---

# Import Research Papers from Telegram to Zotero with AI Abstract Summaries


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Code | Code |
| HTTP Request2 | HTTP Request |
| HTTP Request3 | HTTP Request |
| HTTP Request4 | HTTP Request |
| HTTP Request | HTTP Request |
| Edit Fields | 数据设置 |
| Code4 | Code |
| Merge | 数据合并 |
| If3 | IF 判断 |
| HTTP Request9 | HTTP Request |
| Edit Fields1 | 数据设置 |
| Edit Fields2 | 数据设置 |
| Edit Fields3 | 数据设置 |
| HTTP Request1 | HTTP Request |
| Basic LLM Chain | LLM Chain |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Send a text message | Telegram |
| Send a text message1 | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

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

- 节点总数：19
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：10
- 输出节点：8
- 分类：workflow-automation
