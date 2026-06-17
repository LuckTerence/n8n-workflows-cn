## 简介
**Create a cryptocurrency-powered API for selling resources with AgentGatePay**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11874

---

# Create a cryptocurrency-powered API for selling resources with AgentGatePay


## 节点清单

| 节点 | 类型 |
|------|------|
| 📡 GET /resource/{id} | Webhook |
| 1️⃣ Parse Request | Code |
| 2️⃣ Has Payment? | IF 判断 |
| 3️⃣ Generate 402 | Code |
| 4️⃣ Send 402 | 响应 Webhook |
| 5️⃣ Verify Payment | HTTP Request |
| 6️⃣ Validate Payment | Code |
| 6B️⃣ Route: Valid? | IF 判断 |
| 7️⃣ Deliver Resource | Code |
| 8️⃣ Send 200 OK | 响应 Webhook |
| 9️⃣ Send Error | 响应 Webhook |

## 触发方式
- 📡 GET /resource/{id} 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：finance-analysis
