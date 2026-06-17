## 简介
**Automate Patient Intake & Symptom Triage with AI, Cal.com and Google Services**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Automate Patient Intake & Symptom Triage with AI、（AI 增强)手动或子流程调用，通过 HTTP API 实现自动化。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- Check for new patient appointment Requests 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
