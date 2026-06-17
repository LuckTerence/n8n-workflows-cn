## 简介
**AI web researcher for sales**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2324

---

# AI web researcher for sales


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Test workflow" | 手动触发 |
| Input | 数据设置 |
| OpenAI Chat Model | OpenAI Chat Model |
| Get website content | 工作流工具 |
| SerpAPI - Search Google | SerpApi 工具 |
| Structured Output Parser | 结构化输出解析器 |
| Loop Over Items | 分批处理 |
| AI Researcher Output Data | 数据设置 |
| Google Sheets - Update Row with data | Google Sheets |
| Merge data | 数据合并 |
| Get rows to enrich | Google Sheets |
| Schedule Trigger | 定时触发器 |
| AI company researcher | AI Agent |
| Search Google with ScrapingBee | 工作流工具 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，定时执行。

定时触发、手动触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking "Test workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：12
- 输出节点：0
- 分类：workflow-automation
