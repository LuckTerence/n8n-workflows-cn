## 简介
**Allow Users to Send a Sequence of Messages to an AI Agent in Telegram**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2917

---

# Allow Users to Send a Sequence of Messages to an AI Agent in Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Reply | Telegram |
| Receive Message | Telegram 触发器 |
| Wait 10 Seconds | 等待 |
| Add to Queued Messages | Supabase |
| No Operation, do nothing | 空操作 |
| Aggregate | 数据聚合 |
| Delete Queued Messages | Supabase |
| OpenAI Chat Model | OpenAI Chat Model |
| Sort by Message ID | 数据排序 |
| Get Queued Messages | Supabase |
| Check Most Recent Message | IF 判断 |
| AI Agent | AI Agent |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：Telegram 消息触发

## 触发方式
- Receive Message 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：ai-agent
