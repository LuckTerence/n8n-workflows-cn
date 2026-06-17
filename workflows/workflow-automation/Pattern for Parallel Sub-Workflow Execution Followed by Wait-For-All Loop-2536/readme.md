## 简介
**Pattern for Parallel Sub-Workflow Execution Followed by Wait-For-All Loop**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2536

---

# Pattern for Parallel Sub-Workflow Execution Followed by Wait-For-All Loop


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Webhook Callback Wait | 等待 |
| Update finishedSet | Code |
| Initialize finishedSet | 数据设置 |
| Simulate Multi-Item for Parallel Processing | Code |
| If All Finished | IF 判断 |
| Start Sub-Workflow via Webhook | HTTP Request |
| Acknowledge Finished | 响应 Webhook |
| Continue Workflow (noop) | 空操作 |
| Wait | 等待 |
| Call Resume on Parent Workflow | HTTP Request |
| Respond to Webhook | 响应 Webhook |
| Webhook | Webhook |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，Webhook 触发。

Webhook触发、手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：手动触发, Webhook 触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
