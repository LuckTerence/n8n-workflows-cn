## 简介
**Automated Real Estate Property Lead Scoring with BatchData**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3664

---

# Automated Real Estate Property Lead Scoring with BatchData


## 节点清单

| 节点 | 类型 |
|------|------|
| CRM New Lead Webhook | Webhook |
| Fetch Lead Data | HTTP Request |
| BatchData Property Lookup | HTTP Request |
| Score And Qualify Lead | Code |
| Update CRM Lead | HTTP Request |
| Is High-Value Lead? | IF 判断 |
| Create Immediate Follow-up Task | HTTP Request |
| Send Slack Notification | Slack |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，Webhook 触发。

Webhook触发，通过 Slack + HTTP API 实现自动化。

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
- 触发方式：Webhook 触发

## 触发方式
- CRM New Lead Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：2
- 输出节点：5
- 分类：workflow-automation
