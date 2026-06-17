## 简介
**CallForge - 04 - AI Workflow for Gong.io Sales Calls**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3034

---

# CallForge - 04 - AI Workflow for Gong.io Sales Calls


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop to next call | 空操作 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Create Notion DB Page | Notion |
| Post Slack Receipt | Slack |
| AI Team Processor | 执行工作流 |
| Update Slack Progress | Slack |
| Merge call data and parent notion id | 数据合并 |
| Reduce down to 1 object | 数据聚合 |
| Get all older Calls | Notion |
| Isolate Only Call IDs | 数据设置 |
| Only Process New Calls | compareDatasets |
| Reduce down to One object | 数据聚合 |
| Bundle Slack Message Data | 数据聚合 |
| Merge Slack and Call Data | 数据合并 |
| Loop Over Calls | 分批处理 |
| Bundle Notion Parent Object Data | 数据聚合 |
| Bundle Processed Calls | 数据聚合 |
| Post Completed Calls Message | Slack |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

手动触发，通过 在线表格 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：18
- 触发方式：手动或子流程调用

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：14
- 输出节点：3
- 分类：workflow-automation
