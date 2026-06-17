## 简介
**Automated Hugging Face Paper Summary Fetching & Categorization Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2765

---

# Automated Hugging Face Paper Summary Fetching & Categorization Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| If | IF 判断 |
| Loop Over Items | 分批处理 |
| Split Out | 数据拆分 |
| Request Hugging Face Paper | HTTP Request |
| Extract Hugging Face Paper | HTML |
| Check Paper URL Existed | Notion |
| Request Hugging Face Paper Detail | HTTP Request |
| Extract Hugging Face Paper Abstract | HTML |
| OpenAI Analysis Abstract | OpenAI |
| Store Abstract Notion | Notion |
| Send Analysis Result Slack | Slack |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，定时执行。

定时触发，通过 在线表格 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
