## 简介
**Send pre-meeting context briefings with Outlook, SharePoint, Entra ID and Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16107

---

# Send pre-meeting context briefings with Outlook, SharePoint, Entra ID and Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| When Every 30 Minutes | 定时触发器 |
| Set Config Parameters | 数据设置 |
| Loop Over VIP Mailboxes | 分批处理 |
| Extract VIP Mailbox Data | Code |
| Fetch Calendar Events | Outlook |
| Filter Events for Briefing | Code |
| Check Events to Brief | IF 判断 |
| No Events Switch Mailbox | 空操作 |
| Loop Through Events | 分批处理 |
| Extract Event Data | Code |
| Post to SharePoint Search API | HTTP Request |
| Build Attendee Request Payload | Code |
| Post to Graph API for Attendees | HTTP Request |
| Compile Event Briefing | Code |
| Dispatch Briefing to Teams | Teams |
| Proceed to Next Event | 空操作 |
| All Mailboxes Completed | 空操作 |
| Teams Briefing Error Notice | Teams |
| Check Briefing Sent Status | IF 判断 |
| Merge Data Before Next Event | 数据合并 |
| Mark Event as Briefed | Code |
| Combine Batch API Response | Code |
| Combine SP Search Response | Code |
| Check for Attendee Requests | IF 判断 |
| Skip Attendee Batch Processing | Code |
| Build SharePoint Query | Code |



## 功能说明

Send pre-meeting context briefings with Outlook、S。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：定时触发

## 触发方式
- When Every 30 Minutes 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
