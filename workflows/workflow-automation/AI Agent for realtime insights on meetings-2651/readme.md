## 简介
**AI Agent for realtime insights on meetings**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2651

---

# AI Agent for realtime insights on meetings


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI1 | OpenAI |
| Insert Transcription Part | PostgreSQL |
| Create Note | PostgreSQL 工具 |
| Create Recall bot | HTTP Request |
| Create OpenAI thread | HTTP Request |
| Create data record | Supabase |
| Scenario 1 Start - Edit Fields | 数据设置 |
| Scenario 2 Start - Webhook | Webhook |
| If Jimmy word | IF 判断 |



## 功能说明

AI Agent for realtime insights on meetings（AI 增强)Webhook 触发，通过 数据库 + HTTP API 实现自动化。

Webhook触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- Scenario 2 Start - Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
