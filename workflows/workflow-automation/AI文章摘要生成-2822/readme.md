## 简介
**AI文章摘要生成**

WordPress文章AI摘要

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/2822

---

# AI文章摘要生成


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Text Classifier | 文本分类器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Loop Over Items | 分批处理 |
| If | IF 判断 |
| Webhook | Webhook |
| Schedule Trigger | 定时触发器 |
| Wordpress - Update Post | HTTP Request |
| Google Sheets - Get rows | Google Sheets |
| HTML to Markdown | Markdown |
| OpenAI | OpenAI |
| Google Sheets - Add Row | Google Sheets |
| Slack - Notify Channel | Slack |
| Set fields - From Webhook input | 数据设置 |
| Date & Time - Substract | 日期时间 |
| Set fields - Prepare data for Gsheets & Slack | 数据设置 |
| WordPress - Get Post2 | wordpress |
| No Operation, do nothing | 空操作 |
| WordPress - Get Last Posts | wordpress |
| WordPress - Get Post1 | wordpress |
| WordPress - Get All Posts | wordpress |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，定时执行。

定时触发、Webhook触发、手动触发，通过 在线表格 + Slack + HTTP API 实现自动化。

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

- 节点总数：21
- 触发方式：手动触发, Webhook 触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Webhook 触发
- Schedule Trigger 触发

## 统计
- 节点总数：21
- 触发节点：3
- 处理节点：16
- 输出节点：2
- 分类：workflow-automation
