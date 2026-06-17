## 简介
**Filter URLs with AI-Powered robots.txt Compliance & Source Verification**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8138

---

# Filter URLs with AI-Powered robots.txt Compliance & Source Verification


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Get Base URL | Code |
| Prepare Robots.txt Check | 数据设置 |
| Assume Disallow | 数据设置 |
| Information Extractor | 信息提取器 |
| Model Selector | modelSelector |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Groq Chat Model | Groq Chat Model |
| Google Gemini Chat Model | OpenAI Chat Model |
| Get Robots.txt | HTTP Request |
| Check Robots.txt | Code |
| Prepare Robots.txt Check 2 | 数据设置 |
| If Link Allowed | IF 判断 |
| Prepare Output for Link Disallowed | 数据设置 |
| If Link Allowed 2 | IF 判断 |
| Create robots.txt Table | PostgreSQL |
| Check robots.txt Table | PostgreSQL |
| If robots.txt Found and Updated | IF 判断 |
| Output | 数据设置 |
| Prepare Output | 数据设置 |
| Prepare Output for Link Allowed | 数据设置 |
| Upsert robots.txt Table | PostgreSQL |
| Delete robots.txt Table | PostgreSQL |
| Start | 执行工作流触发器 |
| Check all robots.txt Table | PostgreSQL |
| Assume False Output | 数据设置 |
| Create forbidden urls table | PostgreSQL |
| Check forbidden urls table | PostgreSQL |
| If forbidden url Detected | IF 判断 |
| Return Disallow | 数据设置 |
| Check all forbidden urls Table | PostgreSQL |
| Delete forbidden urls Table | PostgreSQL |
| Manual Upsert robots.txt Table | PostgreSQL |
| Manual Upsert forbidden urls Table | PostgreSQL |
| Start (Tests) | 数据设置 |
| Manual Create forbidden urls table | PostgreSQL |
| Manually Create robots.txt Table | PostgreSQL |



## 功能说明

Filter URLs with AI-Powered robots.txt Compliance （AI 增强)定时触发，通过 数据库 + HTTP API 实现自动化。

定时触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：37
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发
- Start 触发

## 统计
- 节点总数：37
- 触发节点：2
- 处理节点：34
- 输出节点：1
- 分类：workflow-automation
