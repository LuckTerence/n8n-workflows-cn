## 简介
**Auto-Generate Social Media Posts from URLs with AI, Telegram & Multi-Platform Posting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Supabase)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9059

---

# Auto-Generate Social Media Posts from URLs with AI, Telegram & Multi-Platform Posting


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Bot Trigger | Telegram 触发器 |
| Extract URL | Function |
| Fetch URL Content | HTTP Request |
| Extract Text Content | Function |
| Post to Facebook | HTTP Request |
| Post to Instagram | HTTP Request |
| Final Status Update | Google Sheets |
| Post to Instagram1 | HTTP Request |
| Facebook Post | OpenAI |
| Instagram Post | OpenAI |
| LinkedIn Post | OpenAI |
| Merge | 数据合并 |
| Merge1 | 数据合并 |
| Merge2 | 数据合并 |
| If message contains URL | IF 判断 |
| Telegram | Telegram |
| Code | Code |
| Code1 | Code |
| LinkedIn | linkedIn |
| Binary File | HTTP Request |
| Merge3 | 数据合并 |
| Get Post URL | HTTP Request |
| Code2 | Code |
| Code3 | Code |
| Edit Fields | 数据设置 |
| Generate an image1 | OpenAI |
| Basic LLM Chain2 | LLM Chain |
| Send a photo message | Telegram |
| Append or update row in sheet | Google Sheets |
| Google Gemini | OpenAI Chat Model |
| Upload to Supabase (uses credentials) | HTTP Request |
| Supabase Config | 数据设置 |
| Supabase Public URL | 数据设置 |



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

- 节点总数：33
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Bot Trigger 触发

## 统计
- 节点总数：33
- 触发节点：1
- 处理节点：23
- 输出节点：9
- 分类：workflow-automation
