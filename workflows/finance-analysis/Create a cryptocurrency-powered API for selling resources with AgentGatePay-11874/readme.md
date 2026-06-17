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



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，Webhook 触发。

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

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- 📡 GET /resource/{id} 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：finance-analysis
