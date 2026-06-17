## 简介
**Manage attendee registrations and send emails**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/730

---

# Manage attendee registrations and send emails


## 节点清单

| 节点 | 类型 |
|------|------|
| Attendee Registrations | typeformTrigger |
| Add to Sheets | Google Sheets |
| Create Account | Mattermost |
| Add to team | Mattermost |
| Array to Rows | Function |
| Get Session Details | Google Sheets |
| Merge Data | 数据合并 |
| Add to channels | Mattermost |
| Add to Event | Google Calendar |
| Welcome Email | Email 发送 |

## 触发方式
- Attendee Registrations 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：5
- 输出节点：4
- 分类：workflow-automation
