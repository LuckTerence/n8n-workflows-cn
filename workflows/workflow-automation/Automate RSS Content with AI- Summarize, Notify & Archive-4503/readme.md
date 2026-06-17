## 简介
**Automate RSS Content with AI: Summarize, Notify & Archive**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4503

---

# Automate RSS Content with AI: Summarize, Notify & Archive


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Markdown | Markdown |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| Loop Over Items1 | 分批处理 |
| RSS | RSS Feed |
| Save News | Google Sheets |
| Set Tech News RSS Feeds | 数据设置 |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Discord | discordTool |
| Map Fields | 数据设置 |
| filterYesterdayNews | Code |
| aggregateNews | Code |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，定时执行。

定时触发，通过 Discord + HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发
- RSS 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：14
- 输出节点：0
- 分类：workflow-automation
