## 简介
**Meeting Management Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7904

---

# Meeting Management Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| AI Agent | AI Agent |
| Gmail | Gmail 工具 |
| Telegram | Telegram |
| Date & Time | dateTimeTool |
| Get | Google Calendar 工具 |
| Update | Google Calendar 工具 |
| Delete | Google Calendar 工具 |
| Create | Google Calendar 工具 |
| OpenAI | OpenAI Chat Model |
| Memory | 记忆缓冲区 |



## 功能说明

Meeting Management Agent（AI 增强)Telegram 消息触发，通过 Telegram + 邮箱 + HTTP API 实现自动化。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
