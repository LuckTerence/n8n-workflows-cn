## 简介
**Automate Peer Review Assignments with Sonar Pro AI & Multi-Channel Deadline Reminders**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：18 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10312

---

# Automate Peer Review Assignments with Sonar Pro AI & Multi-Channel Deadline Reminders


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Schedule Trigger | 定时触发器 |
| Webhook - Assignment Submission | Webhook |
| Extract Submission Data | 数据设置 |
| Read Assignment File | readPDF |
| AI Evaluation - Technical Criteria | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Store Evaluation Results | 数据设置 |
| Split Peer Reviewers | 数据拆分 |
| Create Evaluation Template | 数据设置 |
| Send Teams Notification | Teams |
| Send Discord Notification | Discord |
| Send Email with Template | Email 发送 |
| Save to Google Sheets - Grading | Google Sheets |
| Check Review Deadlines | Google Sheets |
| Filter Approaching Deadlines | 过滤器 |
| Send Deadline Reminder - Teams | Teams |
| Send Deadline Reminder - Discord | Discord |
| Send Deadline Reminder - Email | Email 发送 |
| Webhook Response | 响应 Webhook |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Manual Trigger 触发
- Schedule Trigger 触发
- Webhook - Assignment Submission 触发

## 统计
- 节点总数：21
- 触发节点：3
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
