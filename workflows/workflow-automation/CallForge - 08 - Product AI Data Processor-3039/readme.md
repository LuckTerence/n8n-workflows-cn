## 简介
**CallForge - 08 - Product AI Data Processor**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3039

---

# CallForge - 08 - Product AI Data Processor


## 节点清单

| 节点 | 类型 |
|------|------|
| Execute Workflow Trigger | 执行工作流触发器 |
| Check if Product Data Found | IF 判断 |
| Create Product Data Object1 | Notion |
| Create Product Feedback Data Object | Notion |
| Check if AI Use Case Data Found | IF 判断 |
| Check if AI Mentioned On Call | IF 判断 |
| Wait for rate limiting - AI Use Case | 等待 |
| Wait for rate limiting - Product Data | 等待 |
| Split Out Product Data | 数据拆分 |
| Bundle AI Use Case Data to 1 object | 数据聚合 |
| Bundle Product Feedback Data to 1 object | 数据聚合 |
| Merge AI Use Case Thread | 数据设置 |
| Merge Product Feedback Thread | 数据设置 |
| Update Call with AI Data Summary | Notion |



## 功能说明

电商自动化，订单处理或商品管理。

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
- 触发方式：手动或子流程调用

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
