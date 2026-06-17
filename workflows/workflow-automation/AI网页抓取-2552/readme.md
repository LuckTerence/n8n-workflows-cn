## 简介
**AI网页抓取**

Jina+Google Sheets+OpenAI自动抓取网页数据

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/2552

---

# AI网页抓取


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Test workflow" | 手动触发 |
| Split Out | 数据拆分 |
| Save to Google Sheets | Google Sheets |
| OpenAI Chat Model | OpenAI Chat Model |
| Information Extractor | 信息提取器 |
| Jina Fetch | HTTP Request |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 在线表格 + HTTP API 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- When clicking "Test workflow" 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
