## 简介
**AI Chatbot Call Center: Demo Call Back (Production-Ready, Part 6)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4050

---

# AI Chatbot Call Center: Demo Call Back (Production-Ready, Part 6)


## 节点清单

| 节点 | 类型 |
|------|------|
| Media Switch | Switch 路由 |
| Flow Trigger | 执行工作流触发器 |
| Input | 数据设置 |
| Test Trigger | Chat 触发器 |
| Test Fields | 数据设置 |
| Download Minimax Audio | HTTP Request |
| Telegram Voice Output | Telegram |
| If Provider No | IF 判断 |
| Provider Cache | Redis |
| Save Provider Cache | Redis |
| If Provider Cache | IF 判断 |
| Provider | 数据设置 |
| Load Provider Data | PostgreSQL |
| If Provider Voice | IF 判断 |
| Switch | Switch 路由 |
| Create Chat Log Output | PostgreSQL |
| Create Chat Log Input | PostgreSQL |
| If Input | IF 判断 |
| Output | 数据设置 |
| Media Switch1 | Switch 路由 |
| Chinese,Yue | 数据设置 |
| Minimax TTS | HTTP Request |
| Chinese | 数据设置 |
| Japanese | 数据设置 |
| English | 数据设置 |
| If Reply | IF 判断 |
| Telegram Reply Output | Telegram |
| Telegram Output | Telegram |
| Parse Cache | Code |



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复。

Chat 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：29
- 触发方式：Chat 消息触发

## 触发方式
- Flow Trigger 触发
- Test Trigger 触发

## 统计
- 节点总数：29
- 触发节点：2
- 处理节点：22
- 输出节点：5
- 分类：ai-agent
