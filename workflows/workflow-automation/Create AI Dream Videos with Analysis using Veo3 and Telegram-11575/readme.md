## 简介
**Create AI Dream Videos with Analysis using Veo3 and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11575

---

# Create AI Dream Videos with Analysis using Veo3 and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Parse Dream Command | Code |
| Route: Style Help Request | IF 判断 |
| Send Available Styles | Telegram |
| Route: Valid Dream Input | IF 判断 |
| Send Usage Instructions | Telegram |
| Send Processing Status | Telegram |
| Set API Configuration | 数据设置 |
| AI Dream Analyzer Agent | AI Agent |
| OpenRouter LLM | OpenRouter Chat Model |
| Extract Video Prompt & Analysis | Code |
| Generate Dream Video (Veo3) | HTTP Request |
| Wait for Video Generation | 等待 |
| Poll Generation Status | HTTP Request |
| Route: Generation Complete | IF 判断 |
| Log to Google Sheets | Google Sheets |
| Send Dream Video to User | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：17
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：10
- 输出节点：6
- 分类：workflow-automation
