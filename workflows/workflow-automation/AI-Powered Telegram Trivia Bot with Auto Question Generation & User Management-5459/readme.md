## 简介
**AI-Powered Telegram Trivia Bot with Auto Question Generation & User Management**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5459

---

# AI-Powered Telegram Trivia Bot with Auto Question Generation & User Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Parse Telegram Data | Code |
| Check Existing User | NocoDB |
| User Exists? | IF 判断 |
| Create New User | NocoDB |
| Merge User Data | Code |
| Is Command? | IF 判断 |
| Command Router | Switch 路由 |
| Handle Basic Commands | Code |
| Format Question | Code |
| Update User Game State | NocoDB |
| Get Leaderboard | NocoDB |
| Format Leaderboard | Code |
| Valid Answer? | IF 判断 |
| Get Current Question | NocoDB |
| Process Answer | Code |
| Update User Stats | NocoDB |
| Handle Unknown Text | Code |
| Telegram | Telegram |
| Merge | 数据合并 |
| OpenAI | OpenAI |
| NocoDB | nocoDbTool |
| Daily Question Generator | 定时触发器 |
| Get Possible Categories | Code |
| Send New Questions Available Notification | Telegram |
| Merge1 | 数据合并 |
| Aggregate | 数据聚合 |
| Get User History | NocoDB |
| Mark Question As Answered | NocoDB |
| Aggregate1 | 数据聚合 |
| Get Random Question | NocoDB |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：31
- 触发方式：Telegram 消息触发, 定时触发

## 触发方式
- Telegram Trigger 触发
- Daily Question Generator 触发

## 统计
- 节点总数：31
- 触发节点：2
- 处理节点：27
- 输出节点：2
- 分类：workflow-automation
