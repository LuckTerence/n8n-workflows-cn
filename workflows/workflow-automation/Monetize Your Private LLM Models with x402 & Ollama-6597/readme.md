## 简介
**Monetize Your Private LLM Models with x402 & Ollama**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/6597

---

# Monetize Your Private LLM Models with x402 & Ollama


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
| Private Model Inference | LLM Chain |
| Ollama Engine | lmOllama |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
