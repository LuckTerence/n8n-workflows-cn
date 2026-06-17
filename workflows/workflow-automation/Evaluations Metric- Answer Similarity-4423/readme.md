## 简介
**Evaluations Metric: Answer Similarity**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4423

---

# Evaluations Metric: Answer Similarity


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model1 | OpenAI Chat Model |
| When fetching a dataset row | evaluationTrigger |
| Remap Input | 数据设置 |
| Evaluation | 条件评估 |
| Set Input Fields | 数据设置 |
| No Operation, do nothing | 空操作 |
| AI Agent | AI Agent |
| When chat message received | Chat 触发器 |
| Update Output | 条件评估 |
| Update Metrics | 条件评估 |
| Get Embeddings | HTTP Request |
| GroundTruth to Items | 数据拆分 |
| Get Embeddings1 | HTTP Request |
| Aggregate | 数据聚合 |
| Remap Embeddings | 数据设置 |
| Remap Embeddings1 | 数据设置 |
| Create Embeddings Result | 数据合并 |
| Calculate Similarity Score | Code |



## 功能说明

Evaluations Metric- Answer Similarity（AI 增强)Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：18
- 触发方式：Chat 消息触发

## 触发方式
- When fetching a dataset row 触发
- When chat message received 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：14
- 输出节点：2
- 分类：workflow-automation
