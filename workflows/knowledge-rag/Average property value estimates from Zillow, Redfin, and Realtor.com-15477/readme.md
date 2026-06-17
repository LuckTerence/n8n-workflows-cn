## 简介
**Average property value estimates from Zillow, Redfin, and Realtor.com**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15477

---

# Average property value estimates from Zillow, Redfin, and Realtor.com


## 节点清单

| 节点 | 类型 |
|------|------|
| When Execute Workflow | 手动触发 |
| Fetch Zillow Zestimate | HTTP Request |
| Fetch Redfin Property Data | HTTP Request |
| Fetch Realtor Property Data | HTTP Request |
| Set Property Address | 数据设置 |
| Fetch Redfin Estimate | HTTP Request |
| Merge Property Estimates | 数据合并 |
| Set Estimated Values | 数据设置 |
| Calculate Average Estimate | Code |
| Fetch Detailed Realtor Info | HTTP Request |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

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

- 节点总数：10
- 触发方式：手动触发

## 触发方式
- When Execute Workflow 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：4
- 输出节点：5
- 分类：knowledge-rag
