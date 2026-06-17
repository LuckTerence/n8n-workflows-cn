## 简介
**Manage Cloudflare DNS Records with AI-powered Chat Assistant**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6844

---

# Manage Cloudflare DNS Records with AI-powered Chat Assistant


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Chat Agent | AI Agent |
| Get TLDs | HTTP Request |
| Json | Code |
| Switch | Switch 路由 |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| CloudFlare tool | 工作流工具 |
| End | 空操作 |
| SubCall | 执行工作流触发器 |
| Host details | 数据拆分 |
| Getter | HTTP Request |
| Setter | HTTP Request |



## 功能说明

Manage Cloudflare DNS Records with AI-powered Chat（AI 增强)Chat 消息触发，通过 数据库 + HTTP API 实现自动化。

Chat 消息触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发
- SubCall 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
