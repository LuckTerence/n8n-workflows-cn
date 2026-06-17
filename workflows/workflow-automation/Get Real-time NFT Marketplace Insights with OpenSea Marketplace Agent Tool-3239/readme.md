## 简介
**Get Real-time NFT Marketplace Insights with OpenSea Marketplace Agent Tool**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3239

---

# Get Real-time NFT Marketplace Insights with OpenSea Marketplace Agent Tool


## 节点清单

| 节点 | 类型 |
|------|------|
| Marketplace Agent Brain | OpenAI Chat Model |
| Marketplace Agent Memory | 记忆缓冲区 |
| OpenSea Marketplace Agent | AI Agent |
| Workflow Input Trigger | 执行工作流触发器 |
| OpenSea Get All Listings by Collection | HTTP 工具 |
| OpenSea Get All Offers by Collection | HTTP 工具 |
| OpenSea Get Best Listing by NFT | HTTP 工具 |
| OpenSea Get Best Listings by Collection | HTTP 工具 |
| OpenSea Get Best Offer by NFT | HTTP 工具 |
| OpenSea Get Collection Offers | HTTP 工具 |
| OpenSea Get Item Offers | HTTP 工具 |
| OpenSea Get Listings | HTTP 工具 |
| OpenSea Get Trait Offers | HTTP 工具 |
| OpenSea Get Order | HTTP 工具 |



## 功能说明

Get Real-time NFT Marketplace Insights with OpenSe（AI 增强)手动或子流程调用，通过 n8n 内置节点实现自动化。

手动触发，通过 工作流编排 实现自动化。

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
- 触发方式：手动或子流程调用

## 触发方式
- Workflow Input Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：3
- 输出节点：10
- 分类：workflow-automation
