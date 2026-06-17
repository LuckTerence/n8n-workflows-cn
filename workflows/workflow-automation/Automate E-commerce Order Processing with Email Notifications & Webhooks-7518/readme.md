## 简介
**Automate E-commerce Order Processing with Email Notifications & Webhooks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7518

---

# Automate E-commerce Order Processing with Email Notifications & Webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| New Order Webhook | Webhook |
| Store Configuration | 数据设置 |
| Extract Order Details | 数据设置 |
| Validate Order Data | IF 判断 |
| Send Customer Confirmation | Email 发送 |
| Send Team Notification | Email 发送 |
| Log Processing Details | 数据设置 |
| Send Success Response | 响应 Webhook |
| Send Error Response | 响应 Webhook |

## 触发方式
- New Order Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
