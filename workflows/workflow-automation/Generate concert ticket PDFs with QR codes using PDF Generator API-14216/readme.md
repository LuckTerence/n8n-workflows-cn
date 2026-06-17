# Generate concert ticket PDFs with QR codes using PDF Generator API

https://n8nworkflows.xyz/workflows/14216

## 节点清单

| 节点 | 类型 |
|------|------|
| Concert Ticket Form | 表单触发器 |
| Prepare Ticket Data | Code |
| Generate Concert Ticket PDF | pdfGeneratorApi |
| Build Confirmation Email | Code |
| Send Ticket to Attendee | Email 发送 |
| Log Ticket Sale | Google Sheets |
| Notify Event Organizer | Slack |

## 触发方式
- Concert Ticket Form 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
