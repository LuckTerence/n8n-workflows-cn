## 简介
**Send birthday and anniversary reminders with Groq AI gift ideas to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15335

---

# Send birthday and anniversary reminders with Groq AI gift ideas to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| ⏰ Daily 8 AM | 定时触发器 |
| ▶️ Manual Test | 手动触发 |
| 📖 Read People | Google Sheets |
| 📅 Check Dates | Code |
| 🎁 Format Messages | Code |
| 🤖 AI Personalize | LLM Chain |
| Groq Chat Model | Groq Chat Model |
| 📝 Combine Message | Code |
| 📲 Send Telegram | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：9
- 触发方式：定时触发, 手动触发

## 触发方式
- ⏰ Daily 8 AM 触发
- ▶️ Manual Test 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
