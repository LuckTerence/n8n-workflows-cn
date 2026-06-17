## 简介
**Create a Self-Hosted Blockchain Payment Processor with x402 and 1Shot API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7364

---

# Create a Self-Hosted Blockchain Payment Processor with x402 and 1Shot API


## 节点清单

| 节点 | 类型 |
|------|------|
| Simulate Payment | 一次性执行 |
| Lookup Payment Configs | Code |
| /verify | Webhook |
| /settle | Webhook |
| Settlement Response | 响应 Webhook |
| Verify Response | 响应 Webhook |
| Response: Bad POST Body (/verify) | 响应 Webhook |
| Response: Bad POST Body (/settle) | 响应 Webhook |
| 1Shot API Submit & Wait | 一次性同步 |
| Check POST Payload | IF 判断 |
| Decode & Validate X-Payment | Code |
| Ensure Payment Payload | IF 判断 |
| /supported | Webhook |
| Response: Return Supported Networks | 响应 Webhook |
| Supported Networks Config | Code |
| Bad Payload or Header | IF 判断 |
| Unsupported Token | IF 判断 |
| verify or settle | IF 判断 |
| Response: Unsupported Token (/verify) | 响应 Webhook |
| Response: Unsupported Token (/settle) | 响应 Webhook |

## 触发方式
- /verify 触发
- /settle 触发
- /supported 触发

## 统计
- 节点总数：20
- 触发节点：3
- 处理节点：10
- 输出节点：7
- 分类：workflow-automation
