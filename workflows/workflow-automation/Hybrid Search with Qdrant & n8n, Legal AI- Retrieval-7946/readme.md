## 简介
**Hybrid Search with Qdrant & n8n, Legal AI: Retrieval**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7946

---

# Hybrid Search with Qdrant & n8n, Legal AI: Retrieval


## 节点清单

| 节点 | 类型 |
|------|------|
| Index Dataset from HuggingFace | 手动触发 |
| Split Them All Out | 数据拆分 |
| Get Dataset Splits | HTTP Request |
| Divide Per Row | 数据拆分 |
| Keep Test Split | 过滤器 |
| Get Test Queries | HTTP Request |
| Query Points | qdrant |
| Merge | 数据合并 |
| Loop Over Items | 分批处理 |
| Keep Questions with Answers in the Dataset | 过滤器 |
| Keep Questions & IDs | 数据设置 |
| Aggregate Evals | 数据聚合 |
| Percentage of isHits in Evals | 数据设置 |
| isHit = If we Found the Correct Answer | 数据设置 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：手动触发

## 触发方式
- Index Dataset from HuggingFace 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
