## 简介
**Generate Self-Documenting API Portal for Webhooks with n8n API & Bootstrap**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7706

---

# Generate Self-Documenting API Portal for Webhooks with n8n API & Bootstrap


## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| Webhook | Webhook |
| Configs | 数据设置 |
| Respond | 响应 Webhook |
| RespondHTML | 响应 Webhook |
| MakeFullHTML | HTML |
| ExecuteSubWorkflow | 执行工作流 |
| Execute | 执行工作流触发器 |
| GetWorkflows | n8n |
| FilterWorkflows | Code |
| Webhook1 | Webhook |
| API_DOCS | 数据设置 |
| FakeResponse | Code |



## 功能说明

API 集成接口，连接和编排多个第三方服务，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发
- Execute 触发
- Webhook1 触发

## 统计
- 节点总数：13
- 触发节点：3
- 处理节点：8
- 输出节点：2
- 分类：devops
