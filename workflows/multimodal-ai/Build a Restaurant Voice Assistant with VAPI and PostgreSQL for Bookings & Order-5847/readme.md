## 简介
**Build a Restaurant Voice Assistant with VAPI and PostgreSQL for Bookings & Orders**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5847

---

# Build a Restaurant Voice Assistant with VAPI and PostgreSQL for Bookings & Orders


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger: Voice Request (VAPI) | Webhook |
| Update Data (Table Booking / Orders) | PostgreSQL |
| Respond: Booking/Order Confirmation (VAPI) | 响应 Webhook |
| Wait For Response | 等待 |
| Wait For Response1 | 等待 |
| Trigger: Info Request (VAPI) | Webhook |
| Get Restaurant Info (Postgres) | PostgreSQL |
| Respond: Restaurant Details (VAPI) | 响应 Webhook |



## 功能说明

AI 语音处理工作流，语音合成或转录，Webhook 触发。

Webhook触发，通过 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：8
- 触发方式：Webhook 触发

## 触发方式
- Trigger: Voice Request (VAPI) 触发
- Trigger: Info Request (VAPI) 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：4
- 输出节点：2
- 分类：multimodal-ai
