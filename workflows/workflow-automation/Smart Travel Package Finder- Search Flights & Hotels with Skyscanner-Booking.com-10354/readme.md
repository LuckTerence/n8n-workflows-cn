## 简介
**Smart Travel Package Finder: Search Flights & Hotels with Skyscanner-Booking.com**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10354

---

# Smart Travel Package Finder: Search Flights & Hotels with Skyscanner-Booking.com


## 节点清单

| 节点 | 类型 |
|------|------|
| 📥 Travel Request Webhook | Webhook |
| 📝 Parse & Validate Inputs | 数据设置 |
| ✈️ Search Flights (Skyscanner) | HTTP Request |
| 🏨 Search Hotels (Booking.com) | HTTP Request |
| 🔀 Merge Flight & Hotel Data | 数据合并 |
| 🧮 Generate Itinerary Combinations | Code |
| 🎨 Format HTML Email | Code |
| ✉️ Send via Gmail | Email 发送 |
| 📤 Webhook Response | 响应 Webhook |



## 功能说明

日历日程管理，自动创建事件或发送提醒，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- 📥 Travel Request Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
