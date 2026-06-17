## 简介
**Monetize Workflows with x402 Payment Protocol and 1Shot API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5389

---

# Monetize Workflows with x402 Payment Protocol and 1Shot API


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Check for presence of X-HEADER | IF 判断 |
| Decode & Validate X-Payment | Code |
| Simulate Payment | 一次性执行 |
| On Successful Payment Simulation | IF 判断 |
| 1Shot API Submit & Wait | 一次性同步 |
| Ensure Well Formatted Payment Payload | IF 判断 |
| Response: Missing or Invalid Payment Headers | 响应 Webhook |
| Response: Payment Invalid | 响应 Webhook |
| Response: 200 - Payment Successful | 响应 Webhook |



## 功能说明

财务自动化，发票处理或支付流程管理，Webhook 触发。

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

- 节点总数：10
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
