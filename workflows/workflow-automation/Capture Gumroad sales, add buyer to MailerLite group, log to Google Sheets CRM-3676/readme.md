## 简介
**Capture Gumroad sales, add buyer to MailerLite group, log to Google Sheets CRM**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3676

---

# Capture Gumroad sales, add buyer to MailerLite group, log to Google Sheets CRM


## 节点清单

| 节点 | 类型 |
|------|------|
| Assign to group | HTTP Request |
| Gumroad Sale Trigger | gumroadTrigger |
| append row in CRM | Google Sheets |
| add subscriber to MailerLite | mailerLite |

## 触发方式
- Gumroad Sale Trigger 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：2
- 输出节点：1
- 分类：workflow-automation
