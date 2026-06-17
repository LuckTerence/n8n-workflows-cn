## 简介
**AI新闻简报构建**

Dumpling AI爬站+GPT-4o摘要+简报

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（GPT-4o→DeepSeek，Gmail需手动替换）
> 原始来源：https://n8nworkflows.xyz/workflows/4030

---

# AI新闻简报构建


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Get Website URLs from Google Sheet | Google Sheets |
| Crawl and Extract Site Content with Dumpling AI | HTTP Request |
| Split Extracted Results into Individual Items | 数据拆分 |
| Map Title, URL, and Page Text | 数据设置 |
| Combine Articles into Single Prompt Format | Code |
| Generate HTML Newsletter with Subject Using GPT-4o | OpenAI |
| Send Newsletter via Gmail | Gmail |



## 功能说明

内容管理工具，自动生成或发布内容。

手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：手动触发

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
