## 简介
**Screen Applicants With AI, notify HR and save them in a Google Sheet**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2632

---

# Screen Applicants With AI, notify HR and save them in a Google Sheet


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Gemini Chat Model | OpenAI Chat Model |
| Confirmation of CV Submission | Email 发送 |
| Inform HR New CV Received | Email 发送 |
| Using AI Analysis & Rating | LLM Chain |
| Convert Binary to Json | 从文件提取 |
| Application Form | 表单触发器 |
| Candidate Lists | Google Sheets |

## 触发方式
- Application Form 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
