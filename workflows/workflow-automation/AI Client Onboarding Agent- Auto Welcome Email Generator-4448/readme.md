## 简介
**AI Client Onboarding Agent: Auto Welcome Email Generator**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4448

---

# AI Client Onboarding Agent: Auto Welcome Email Generator


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
