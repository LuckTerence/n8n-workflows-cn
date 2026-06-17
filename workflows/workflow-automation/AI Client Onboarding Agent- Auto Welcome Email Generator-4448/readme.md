# AI Client Onboarding Agent: Auto Welcome Email Generator

https://n8nworkflows.xyz/workflows/4448

## 节点清单

| 节点 | 类型 |
|------|------|
| Start | start |
| Error Handler | 错误触发器 |
| Execution Completed | 空操作 |
| Execution Failure | 空操作 |
| Client Checklist | 数据设置 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Trigger on New Client Form Submission | Google Sheets 触发器 |
| Extract and Structure Client Data | 数据设置 |
| Personalize Using Gemini | LLM Chain |
| Send Email to Client | Email 发送 |

## 触发方式
- Error Handler 触发
- Trigger on New Client Form Submission 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
