## 简介
**Intelligent Purchase Order Generator with AI Supplier Selection**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10680

---

# Intelligent Purchase Order Generator with AI Supplier Selection


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Validate Request | Code |
| Prepare AI Context | 数据设置 |
| AI Supplier Selector | AI Agent |
| Enrich with Supplier Data | Code |
| Needs Approval? | IF 判断 |
| Request Approval | Email 发送 |
| Generate PO Document | Code |
| HTML to PDF | htmlcsstopdf |
| Archive in Drive | Google Drive |
| Email to Supplier | Email 发送 |
| Log in Procurement System | Code |
| Notify Procurement Team | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
