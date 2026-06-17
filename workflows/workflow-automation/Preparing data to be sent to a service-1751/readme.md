## 简介
**Preparing data to be sent to a service**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/1751

---

# Preparing data to be sent to a service


## 节点清单

| 节点 | 类型 |
|------|------|
| On clicking 'execute' | 手动触发 |
| Create or Update record in Google Sheet | Google Sheets |
| Set - Prepare fields | 数据设置 |
| Customer Datastore - Generate some data | n8nTrainingCustomerDatastore |



## 功能说明

Preparing data to be sent to a service。

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

- 节点总数：4
- 触发方式：手动触发

## 触发方式
- On clicking 'execute' 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：3
- 输出节点：0
- 分类：workflow-automation
