## 简介
**Qualify and Route Sales Leads with Mistral-Saba AI and MCDM Scoring**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10757

---

# Qualify and Route Sales Leads with Mistral-Saba AI and MCDM Scoring


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch Demographic Data | HTTP Request |
| Fetch Behavioral Data | HTTP Request |
| Fetch Transactional Data | HTTP Request |
| Merge Lead Data Sources | 数据聚合 |
| MCDM Scoring Engine (AHP-TOPSIS) | Code |
| AI Lead Qualification Agent | AI Agent |
| Lead Enrichment Tool | 代码工具 |
| Prepare Lead Scores | 数据设置 |
| Route by Lead Quality | Switch 路由 |
| Assign to Enterprise Sales Team | HTTP Request |
| Assign to Mid-Market Team | HTTP Request |
| Assign to SMB Team | HTTP Request |
| Send to Nurture Campaign | HTTP Request |
| Collect Routing Results | 数据聚合 |
| Update CRM with Lead Scores | HTTP Request |
| Calculate Performance KPIs | Code |
| Log KPIs to Analytics Dashboard | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：20
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：10
- 输出节点：9
- 分类：workflow-automation
