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

## 触发方式
- New Lead Trigger (Excel) 触发
- VAPI Call Response Webhook 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：multimodal-ai
