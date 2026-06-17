# Automate Patient Intake & Symptom Triage with AI, Cal.com and Google Services

https://n8nworkflows.xyz/workflows/6406

## 节点清单

| 节点 | 类型 |
|------|------|
| Intelligent Doctor Routing | LLM Chain |
| Grab Appointment Time | 日期时间 |
| Extract Patient Info and AI Diagnosis | 数据设置 |
| AI Diagnosis | OpenRouter Chat Model |
| Get Present Appointments | Google Sheets |
| Return Unique Appointments | Code |
| Save new appointments | Google Sheets |
| Map departments with their respective calendars | Code |
| Check for new patient appointment Requests | calTrigger |
| Create Appointment in Respective Department's calender | Google Calendar |
| Parse Output in our preferred structure | Code |

## 触发方式
- Check for new patient appointment Requests 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
