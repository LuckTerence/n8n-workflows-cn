## 简介
**AI-Powered Restaurant Booking System with Telegram, Calendar & Email Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7769

---

# AI-Powered Restaurant Booking System with Telegram, Calendar & Email Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Switch | Switch 路由 |
| Telegram | Telegram |
| Edit Fields | 数据设置 |
| Google Calendar | Google Calendar |
| Booking Agent | AI Agent |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| Telegram3 | Telegram |
| Telegram1 | Telegram |
| Simple Memory | 记忆缓冲区 |
| Send a message | Email 发送 |
| Information Gathering Agent | AI Agent |



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

- 节点总数：17
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：12
- 输出节点：4
- 分类：workflow-automation
