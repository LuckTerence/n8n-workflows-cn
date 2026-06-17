## 简介
**Singapore Lottery Predictive Analytics and Pattern Mining System**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10890

---

# Singapore Lottery Predictive Analytics and Pattern Mining System


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch TOTO Draw Data | HTTP Request |
| Fetch 4D Draw Data | HTTP Request |
| Fetch Historical TOTO Dataset | HTTP Request |
| Fetch Historical 4D Dataset | HTTP Request |
| Merge TOTO Data | 数据聚合 |
| Merge 4D Data | 数据聚合 |
| Statistical Pattern Mining - TOTO | Code |
| Statistical Pattern Mining - 4D | Code |
| OpenAI Chat Model | OpenAI Chat Model |
| Probabilistic Modeling Tool | 代码工具 |
| AI Predictive Analysis Agent | AI Agent |
| Format Predictions Output | 数据设置 |
| Advanced Markov Chain Analysis - TOTO | Code |
| Advanced Markov Chain Analysis - 4D | Code |
| Time Series Forecasting - TOTO | Code |
| Time Series Forecasting - 4D | Code |
| Ensemble Prediction Aggregator Tool | 代码工具 |
| Cross-Validation Scoring Tool | 代码工具 |
| Calculator Tool | 计算器工具 |
| Merge All Analysis Results | 数据聚合 |
| Check Data Quality | IF 判断 |
| Generate Quality Report | Code |



## 功能说明

Singapore Lottery Predictive Analytics and Pattern（AI 增强)定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：24
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：19
- 输出节点：4
- 分类：workflow-automation
