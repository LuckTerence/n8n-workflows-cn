## 简介
**Enrich creator handles with cross-platform social data from influencers.club**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13227

---

# Enrich creator handles with cross-platform social data from influencers.club


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Refresh Schedule | 定时触发器 |
| Process in Batches | 分批处理 |
| Wait 5 Second | 等待 |
| Update Null Values Only | HTTP Request |
| Update a row | Supabase |
| List Influencers Without Enrichment | Supabase |
| Influencers.club Enrichment API By Handle | HTTP Request |
| Normalize Creator Enrichment Payload | Code |



## 功能说明

社交媒体管理，多平台内容发布和监听，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：定时触发

## 触发方式
- Daily Refresh Schedule 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
