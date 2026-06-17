## 简介
**Manage Brevo contact lists with full CRUD and bulk membership control**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13639

---

# Manage Brevo contact lists with full CRUD and bulk membership control


## 节点清单

| 节点 | 类型 |
|------|------|
| Get All Lists | HTTP Request |
| Create a List | HTTP Request |
| Update a List | HTTP Request |
| Get a List’s Details | HTTP Request |
| Delete a List | HTTP Request |
| Get Contacts in a List | HTTP Request |
| Aggregate Lists Pages | 数据聚合 |
| Aggregate Contacts Pages | 数据聚合 |
| Add Existing Contacts to a List | HTTP Request |
| Delete Contacts from a List | HTTP Request |



## 功能说明

Manage Brevo contact lists with full CRUD and bulk。

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
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：10
- 触发节点：0
- 处理节点：2
- 输出节点：8
- 分类：workflow-automation
