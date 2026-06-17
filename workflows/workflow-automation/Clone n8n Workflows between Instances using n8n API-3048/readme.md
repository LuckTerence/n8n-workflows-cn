## 简介
**Clone n8n Workflows between Instances using n8n API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3048

---

# Clone n8n Workflows between Instances using n8n API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| GET - Workflows | n8n |
| CREATE - Workflow | n8n |
| n8n - GET - Projects | HTTP Request |
| SET Project ID | 数据设置 |
| PUT - Workflow in Project | HTTP Request |
| Loop Over Items | 分批处理 |
| GET - Destination Workflows | n8n |
| Code | Code |
| Split Out Workflows | 数据拆分 |
| Split Out Workflows1 | 数据拆分 |
| Merge Workflows | 数据合并 |
| Split Out Projects | 数据拆分 |
| Filter Project | 过滤器 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

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
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
