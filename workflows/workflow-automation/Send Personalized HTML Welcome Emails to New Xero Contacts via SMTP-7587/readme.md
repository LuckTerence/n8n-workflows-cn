## 简介
**Send Personalized HTML Welcome Emails to New Xero Contacts via SMTP**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7587

---

# Send Personalized HTML Welcome Emails to New Xero Contacts via SMTP


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Personalized Welcome Email | Email 发送 |
| New Contact in Xero | Webhook |
| Is it a NEW Contact? | IF 判断 |
| Fetch Full Contact Details from Xero | xero |
| Build Personalized HTML Email | Code |

## 触发方式
- New Contact in Xero 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
