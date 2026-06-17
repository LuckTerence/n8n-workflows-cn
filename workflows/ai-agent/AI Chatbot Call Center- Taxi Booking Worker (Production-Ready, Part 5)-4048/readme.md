## 简介
**AI Chatbot Call Center: Taxi Booking Worker (Production-Ready, Part 5)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4048

---

# AI Chatbot Call Center: Taxi Booking Worker (Production-Ready, Part 5)


## 节点清单

| 节点 | 类型 |
|------|------|
| Flow Trigger | 执行工作流触发器 |
| Input | 数据设置 |
| Test Trigger | Chat 触发器 |
| Test Fields | 数据设置 |
| Reset Session | Redis |
| Error Output | 数据设置 |
| Set Open Booking | PostgreSQL |
| Save User Memory | PostgreSQL |
| Delete Route Data | Redis |
| Delete Provider Number | Redis |
| If Booking | IF 判断 |
| If Not Zero | IF 判断 |
| Cancel Output | 数据设置 |
| Reset Session 2 | Redis |
| Switch | Switch 路由 |
| English | 数据设置 |
| Chinese | 数据设置 |
| Japanese | 数据设置 |
| Booking | PostgreSQL |
| Wait Call Back | 执行工作流 |
| Wait Output | 数据设置 |
| Create Event | Google Calendar |
| Call Back | 执行工作流 |
| Delete Chat Memory | PostgreSQL |
| Sync Booking Google Cal | PostgreSQL |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复。

Chat 消息触发，通过 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：Chat 消息触发

## 触发方式
- Flow Trigger 触发
- Test Trigger 触发

## 统计
- 节点总数：25
- 触发节点：2
- 处理节点：23
- 输出节点：0
- 分类：ai-agent
