## 简介
**Multi-Chain Token Swap Relayer with Li.Fi**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7206

---

# Multi-Chain Token Swap Relayer with Li.Fi


## 节点清单

| 节点 | 类型 |
|------|------|
| Response: 200 - Payment Successful | 响应 Webhook |
| Response: Payment Invalid | 响应 Webhook |
| Ensure Well Formatted Payment Payload | IF 判断 |
| 1Shot API Submit & Wait | 一次性同步 |
| On Successful Payment Simulation | IF 判断 |
| Simulate Payment | 一次性执行 |
| Decode & Validate X-Payment | Code |
| Check for presence of X-HEADER | IF 判断 |
| Webhook | Webhook |
| Fetch Li.Fi Quote | HTTP Request |
| Ensure Request Body Parameters | IF 判断 |
| Response: Missing or Invalid Request Body Params | 响应 Webhook |
| Response: No X-Payment Header | 响应 Webhook |
| Response: Missing or Invalid X-Payment Header | 响应 Webhook |
| Lookup Payment Configs | Code |
| Response: Bad Token Address | 响应 Webhook |
| Response: Failed to Get Quote | 响应 Webhook |



## 功能说明

Multi-Chain Token Swap Relayer with Li.Fi。

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

- 节点总数：17
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：8
- 输出节点：8
- 分类：workflow-automation
