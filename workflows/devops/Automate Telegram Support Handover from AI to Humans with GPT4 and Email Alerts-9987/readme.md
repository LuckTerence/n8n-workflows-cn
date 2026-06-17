## 简介
**Automate Telegram Support Handover from AI to Humans with GPT4 and Email Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9987

---

# Automate Telegram Support Handover from AI to Humans with GPT4 and Email Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Configuration | 数据设置 |
| Confirm Operator | Telegram |
| User Approved | IF 判断 |
| Alert Operator | Email 发送 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Operator Confirmed | IF 判断 |
| Operator Attendance | Telegram |
| Operator Declined Attendance | Telegram |
| AI Agent | AI Agent |
| Simple Memory | 记忆缓冲区 |
| Reply To User | Telegram 工具 |
| Human Requested | IF 判断 |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Update Last Message | 数据表 |
| Last Message Exists | 数据表 |
| Row is Empty | IF 判断 |
| Create Temporary Message | 数据表 |
| Update Temporary Message | 数据表 |
| Get Temporary Message | 数据表 |
| Message Router | Switch 路由 |
| Personal | 数据设置 |
| Create Topic | HTTP Request |
| Text Message | IF 判断 |
| Stop Workflow | 空操作 |
| Forward Message To Group | HTTP Request |
| Topic Message | IF 判断 |
| Chat Admins | HTTP Request |
| Forward Message | HTTP Request |
| Personal Trigger | Telegram 触发器 |
| Exit | IF 判断 |
| Close Topic | HTTP Request |
| Update Closed Topic | 数据表 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：33
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发
- Personal Trigger 触发

## 统计
- 节点总数：33
- 触发节点：2
- 处理节点：21
- 输出节点：10
- 分类：devops
