## 简介
**Create autonomous payment agents using AgentGatePay and multi-chain tokens**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11873

---

# Create autonomous payment agents using AgentGatePay and multi-chain tokens


## 节点清单

| 节点 | 类型 |
|------|------|
| ▶️ START | 手动触发 |
| 1️⃣ Load Config | Code |
| 2️⃣ 📊 Get Mandate Token | 数据表 |
| 2B️⃣ Normalize Result | Code |
| 3️⃣ Has Token? | IF 判断 |
| 4️⃣ ✅ Verify Existing Token | HTTP Request |
| 4B️⃣ Check Verification | Code |
| 5️⃣ 🆕 Create New Mandate | HTTP Request |
| 5B️⃣ Parse New Mandate | Code |
| 6️⃣ ✅ Verify New Mandate | HTTP Request |
| 6B️⃣ Check New Mandate | Code |
| 7️⃣ 💾 Insert Token | 数据表 |
| 7B️⃣ Restore Data | Code |
| 8️⃣ 🔀 Merge Paths | Code |
| 9️⃣ Request Resource (x402) | HTTP Request |
| 9B️⃣ Parse 402 Response | Code |
| 🔟 🔒 Sign Payment (Render) | HTTP Request |
| 1️⃣1️⃣ Extract TX Hashes | Code |
| 1️⃣2️⃣ Submit Payment (MCP) | HTTP Request |
| 1️⃣3️⃣ Receive Resource | HTTP Request |
| 1️⃣4️⃣ Complete Task | Code |



## 功能说明

多智能体协作系统，多个 AI Agent 协同完成任务。

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

- 节点总数：21
- 触发方式：手动触发

## 触发方式
- ▶️ START 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：13
- 输出节点：7
- 分类：ai-agent
