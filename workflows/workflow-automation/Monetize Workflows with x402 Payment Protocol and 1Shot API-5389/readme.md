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

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
