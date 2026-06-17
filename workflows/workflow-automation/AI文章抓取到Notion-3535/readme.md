## 简介
**AI文章抓取到Notion**

Gemini+浏览器抓取文章摘要保存

> 分类：工作流自动化 | 适配等级：A（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/3535

---

# AI文章抓取到Notion


## 节点清单

| 节点 | 类型 |
|------|------|
| Gemini 2.5 PRO | Google Gemini |
| website_scraper | HTTP 工具 |
| save_to_notion | notionTool |
| discord_notification | discordTool |
| Save Article To Notion | AI Agent |
| When chat message received | Chat 触发器 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

Chat 消息触发，通过 在线表格 + Discord 实现自动化。

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

- 节点总数：6
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
