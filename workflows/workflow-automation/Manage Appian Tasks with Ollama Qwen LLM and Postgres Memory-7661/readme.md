## 简介
**Manage Appian Tasks with Ollama Qwen LLM and Postgres Memory**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7661

---

# Manage Appian Tasks with Ollama Qwen LLM and Postgres Memory


## 节点清单

| 节点 | 类型 |
|------|------|
| Template Vars | 数据设置 |
| When chat message received | Chat 触发器 |
| Webhook | Webhook |
| Normalize Chat Input | 数据设置 |
| AI Agent | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| List Tasks (Appian) | HTTP Request 工具 |
| List Task Types (Appian) | HTTP Request 工具 |
| Create Task (Appian) | HTTP Request 工具 |
| Prepare Response | 数据设置 |
| Respond to Webhook | 响应 Webhook |



## 功能说明

内容管理工具，自动生成或发布内容，Webhook 触发。

Webhook触发、Chat 消息触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：Chat 消息触发, Webhook 触发

## 触发方式
- When chat message received 触发
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
