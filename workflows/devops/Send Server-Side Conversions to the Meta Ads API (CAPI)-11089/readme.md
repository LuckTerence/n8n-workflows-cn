## 简介
**Send Server-Side Conversions to the Meta Ads API (CAPI)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11089

---

# Send Server-Side Conversions to the Meta Ads API (CAPI)


## 节点清单

| 节点 | 类型 |
|------|------|
| Edit Normalize PII | 数据设置 |
| Crypto - Hash Email | 加密 |
| Crypto - Hash Phone | 加密 |
| Set - Compute Timestamps & Map Fields | 数据设置 |
| Crypto - First Name | 加密 |
| Crypto - Last Name | 加密 |
| Sending Events To Facebook Pixel | HTTP Request |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Preparing for HTTP Request Payload | Code |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：devops
