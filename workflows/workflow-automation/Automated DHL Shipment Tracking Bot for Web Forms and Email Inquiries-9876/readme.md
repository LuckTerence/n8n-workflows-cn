## 简介
**Automated DHL Shipment Tracking Bot for Web Forms and Email Inquiries**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：8 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/9876

---

# Automated DHL Shipment Tracking Bot for Web Forms and Email Inquiries


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Form Trigger | Webhook |
| Gmail Email Trigger | Gmail 触发器 |
| Merge Triggers | 数据合并 |
| Extract Tracking Number | Code |
| Get DHL Tracking Status | HTTP Request |
| Format Response Message | Code |
| Check Source | IF 判断 |
| Webhook Response | 响应 Webhook |
| Send Gmail Response | Email 发送 |

## 触发方式
- Webhook Form Trigger 触发
- Gmail Email Trigger 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
