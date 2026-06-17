## 简介
**Google Autocomplete Keyword Scraper**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3836

---

# Google Autocomplete Keyword Scraper


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate A-Z Queries | Code |
| Google Autocomplete | HTTP Request |
| Loop Over Items | 分批处理 |
| Wait 1s | 等待 |
| Code | Code |
| Get Keyword | Chat 触发器 |
| Extract Keywords | Code |
| Return Keywords | 响应 Webhook |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：Chat 消息触发

## 触发方式
- Get Keyword 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
