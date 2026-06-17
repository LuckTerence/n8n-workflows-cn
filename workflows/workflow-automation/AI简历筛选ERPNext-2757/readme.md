# AI简历筛选ERPNext

https://n8nworkflows.xyz/workflows/2757

## 节点清单

| 节点 | 类型 |
|------|------|
| Code | Code |
| ApplicantData | 数据设置 |
| ERPNext - Reject if Resume not Attached | erpNext |
| Applied Against Job | IF 判断 |
| ERPNext - Hold Applicant | erpNext |
| Get Job Opening | erpNext |
| Google Gemini Chat Model | Google Gemini |
| Convert to Fields | Code |
| If score less than 80 | IF 判断 |
| Reject Applicant | HTTP Request |
| Update Applicant Data | HTTP Request |
| Reume Attachment Link | 数据设置 |
| Resume Link Provided | IF 判断 |
| Accept Applicant | HTTP Request |
| Webhook | Webhook |
| File Type | Switch 路由 |
| Download PDF Resume | HTTP Request |
| PDF to Text | 从文件提取 |
| Txt File to Text (Example) | 从文件提取 |
| Merge1 | 数据合并 |
| Recruitment AI Agent | AI Agent |
| Microsoft Outlook | Outlook |
| WhatsApp Business Cloud | WhatsApp |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：16
- 输出节点：6
- 分类：workflow-automation
