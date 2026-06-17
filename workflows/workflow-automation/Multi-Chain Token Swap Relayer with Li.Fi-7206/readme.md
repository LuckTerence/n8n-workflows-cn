# Multi-Chain Token Swap Relayer with Li.Fi

https://n8nworkflows.xyz/workflows/7206

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

## 触发方式
- Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：8
- 输出节点：8
- 分类：workflow-automation
