## 简介
**Automate Order Confirmations with VAPI Voice AI & Timezone Intelligence**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7380

---

# Automate Order Confirmations with VAPI Voice AI & Timezone Intelligence


## 节点清单

| 节点 | 类型 |
|------|------|
| Order Webhook | Webhook |
| Validate Order Data | IF 判断 |
| Check Timezone & Calling Hours | Code |
| Can Call Now? | IF 判断 |
| Format Order Data | Code |
| Initiate VAPI Call | HTTP Request |
| Check Call Status | IF 判断 |
| Update Order Status | Airtable |
| Schedule Call for Later | Airtable |
| Scheduled Call Checker | schedule |
| Get Scheduled Calls | Airtable |
| VAPI Webhook Handler | Webhook |
| Check Webhook Type | IF 判断 |
| Process Call Results | Code |
| Update Final Status | Airtable |
| Check if Followup Needed | IF 判断 |
| Send Follow-up Alert | Email 发送 |
| Send Confirmation Email | Email 发送 |
| Validation Error Response | 响应 Webhook |
| Call Error Response | 响应 Webhook |
| Success Response | 响应 Webhook |
| Scheduled Response | 响应 Webhook |
| Webhook Response | 响应 Webhook |
| Increment Call Attempts | Airtable |



## 功能说明

AI 语音处理工作流，语音合成或转录，定时执行。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：Webhook 触发

## 触发方式
- Order Webhook 触发
- VAPI Webhook Handler 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：14
- 输出节点：8
- 分类：multimodal-ai
