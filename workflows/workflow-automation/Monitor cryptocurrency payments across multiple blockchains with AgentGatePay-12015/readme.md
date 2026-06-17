## 简介
**Monitor cryptocurrency payments across multiple blockchains with AgentGatePay**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：30 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/12015

---

# Monitor cryptocurrency payments across multiple blockchains with AgentGatePay


## 节点清单

| 节点 | 类型 |
|------|------|
| ▶️ Manual Trigger | 手动触发 |
| 2️⃣ Load Config | Code |
| 3️⃣ 📈 Get User Analytics | HTTP Request |
| 4️⃣ 💳 Get Payment History | HTTP Request |
| 5️⃣ 📋 Get Audit Logs (24h) | HTTP Request |
| 6️⃣ 🔑 Get Active Mandates | HTTP Request |
| 7️⃣ 🔍 Prepare Verification | Code |
| 7B️⃣ Has TX Hash? | IF 判断 |
| 8️⃣ ✅ Verify on Blockchain | HTTP Request |
| 8B️⃣ Skip Verification | Code |
| 9️⃣ Merge Verification | 数据合并 |
| 🔟 📊 Calculate Statistics | Code |
| 1️⃣1️⃣ 🚨 Check Alerts | Code |
| 1️⃣2️⃣ 📱 Format Dashboard | Code |
| 1️⃣3️⃣ 📄 Generate CSV Export | Code |
| 1️⃣4️⃣ 📋 Final Report | Code |
| 3️⃣ 💰 Get Merchant Revenue | HTTP Request |
| 4️⃣ 💳 Get Payment List | HTTP Request |
| 5️⃣ 🔗 Get Webhooks | HTTP Request |
| 6️⃣ 📋 Get Audit Logs (24h) | HTTP Request |
| 2️⃣ Load Config1 | Code |
| 7️⃣ 🔍 Prepare Verification1 | Code |
| 7B️⃣ Has TX Hash?1 | IF 判断 |
| 8️⃣ ✅ Verify on Blockchain1 | HTTP Request |
| 8B️⃣ Skip Verification1 | Code |
| 9️⃣ Merge Verification1 | 数据合并 |
| 🔟 📊 Calculate Statistics1 | Code |
| 1️⃣1️⃣ 🚨 Check Alerts1 | Code |
| 1️⃣2️⃣ 📱 Format Dashboard1 | Code |
| 1️⃣3️⃣ 📄 Generate CSV Export1 | Code |
| 1️⃣4️⃣ 📋 Final Report1 | Code |

## 触发方式
- ▶️ Manual Trigger 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：20
- 输出节点：10
- 分类：workflow-automation
