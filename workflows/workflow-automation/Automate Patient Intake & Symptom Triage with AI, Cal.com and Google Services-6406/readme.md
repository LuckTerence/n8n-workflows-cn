## 简介
**Automate Patient Intake & Symptom Triage with AI, Cal.com and Google Services**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6406

---

# Automate Patient Intake & Symptom Triage with AI, Cal.com and Google Services


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
