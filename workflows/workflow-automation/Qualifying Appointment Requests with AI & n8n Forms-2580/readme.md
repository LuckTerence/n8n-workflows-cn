## 简介
**Qualifying Appointment Requests with AI & n8n Forms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2580

---

# Qualifying Appointment Requests with AI & n8n Forms


## 节点清单

| 节点 | 类型 |
|------|------|
| n8n Form Trigger | 表单触发器 |
| Form End | 表单 |
| Enter Date & Time | 表单 |
| Get Form Values | 数据设置 |
| Terms & Conditions | 表单 |
| OpenAI Chat Model | OpenAI Chat Model |
| Has Accepted? | IF 判断 |
| Send Receipt | Email 发送 |
| Wait for Approval | Email 发送 |
| Has Approval? | IF 判断 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Create Appointment | Google Calendar |
| Send Rejection | Email 发送 |
| Decline | 表单 |
| Decline1 | 表单 |
| Trigger Approval Process | 执行工作流 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Summarise Enquiry | LLM Chain |
| Enquiry Classifier | 文本分类器 |

## 触发方式
- n8n Form Trigger 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：19
- 触发节点：2
- 处理节点：14
- 输出节点：3
- 分类：workflow-automation
