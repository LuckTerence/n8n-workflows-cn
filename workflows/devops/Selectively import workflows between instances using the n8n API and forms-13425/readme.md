## 简介
**Selectively import workflows between instances using the n8n API and forms**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13425

---

# Selectively import workflows between instances using the n8n API and forms


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Strip Incompatible API Fields | Code |
| Filter Our Archived Items | 过滤器 |
| Aggregate Workflows | 数据聚合 |
| Select Workflows | 表单 |
| Select Matching Workflows | 数据合并 |
| Split Out Workflows | 数据拆分 |
| Create JSON Workflow Options | Code |
| Split Out | 数据拆分 |
| Route Mode | Switch 路由 |
| Strip Incompatible API Fields1 | Code |
| Filter Our Archived Items1 | 过滤器 |
| Select Workflows1 | 表单 |
| Select Matching Workflows1 | 数据合并 |
| Split Out Workflows1 | 数据拆分 |
| Create JSON Workflow Options1 | Code |
| Get Instance Information | Notion |
| Create JSON Workflow Options2 | Code |
| Set Source Name and URL | 数据设置 |
| Select Workflows2 | 表单 |
| Set Source | 数据设置 |
| Set Target | 数据设置 |
| Merge Source and Target | 数据合并 |
| Source and Target | 数据聚合 |
| Merge Source Instance | 数据合并 |
| Merge Target Instance | 数据合并 |
| Create Workflow(s) | HTTP Request |
| Create Workflow(s)1 | n8n |
| Set Workflow Display Name (Dynamic) | 数据设置 |
| Set Workflow Display Name (Static) | 数据设置 |
| Aggregate Workflows (Dynamic) | 数据聚合 |
| Aggregate Workflows (Static) | 数据聚合 |
| Results (Dynamic) | 表单 |
| Results (Static) | 表单 |
| Aggregate Workflow Options (Static) | 数据聚合 |
| Aggregate Workflow Options (Dynamic) | 数据聚合 |
| Get All Source Instance Workflows | n8n |
| Get Source Workflows With Pagination | HTTP Request |
| Get Workflow JSON(s) | n8n |
| Get Workflow JSON(s)1 | HTTP Request |



## 功能说明

表单问卷工具，自动收集和处理用户反馈（Selectively)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：40
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：40
- 触发节点：1
- 处理节点：36
- 输出节点：3
- 分类：devops
