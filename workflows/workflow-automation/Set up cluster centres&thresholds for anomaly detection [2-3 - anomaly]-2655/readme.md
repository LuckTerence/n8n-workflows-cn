## 简介
**Set up cluster centres&thresholds for anomaly detection [2-3 - anomaly]**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2655

---

# Set up cluster centres&thresholds for anomaly detection [2-3 - anomaly]


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Total Points in Collection | HTTP Request |
| Cluster Distance Matrix | HTTP Request |
| Scipy Sparse Matrix | Code |
| Set medoid id | HTTP Request |
| Get Medoid Vector | HTTP Request |
| Prepare for Searching Threshold | 数据设置 |
| Searching Score | HTTP Request |
| Threshold Score | 数据设置 |
| Set medoid threshold score | HTTP Request |
| Split Out1 | 数据拆分 |
| Merge | 数据合并 |
| Textual (visual) crop descriptions | 数据设置 |
| Embed text | HTTP Request |
| Get Medoid by Text | HTTP Request |
| Set text medoid id | HTTP Request |
| Prepare for Searching Threshold1 | 数据设置 |
| Threshold Score1 | 数据设置 |
| Searching Text Medoid Score | HTTP Request |
| Medoids Variables | 数据设置 |
| Text Medoids Variables | 数据设置 |
| Qdrant cluster variables | 数据设置 |
| Info About Crop Clusters | 数据设置 |
| Crop Counts | HTTP Request |
| Split Out | 数据拆分 |
| Set text medoid threshold score | HTTP Request |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：13
- 输出节点：12
- 分类：workflow-automation
