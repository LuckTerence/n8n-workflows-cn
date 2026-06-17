## 简介
**Automate Restaurant Marketing & Booking with Excel, VAPI Voice Agent & Calendar**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5890

---

# Automate Restaurant Marketing & Booking with Excel, VAPI Voice Agent & Calendar


## 节点清单

| 节点 | 类型 |
|------|------|
| New Lead Trigger (Excel) | Google Sheets 触发器 |
| Prepare Lead Data | 数据设置 |
| Loop Through Leads | 分批处理 |
| Start Marketing Call (VAPI) | HTTP Request |
| VAPI Call Response Webhook | Webhook |
| Store User Response (Sheet) | Google Sheets |
| Extract Booking/Order Info | Code |
| Schedule Delivery/Table Booking | Google Calendar |
| Send Response to VAPI | 响应 Webhook |



## 功能说明

AI 语音处理工作流，语音合成或转录，Webhook 触发。

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

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- New Lead Trigger (Excel) 触发
- VAPI Call Response Webhook 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：multimodal-ai
