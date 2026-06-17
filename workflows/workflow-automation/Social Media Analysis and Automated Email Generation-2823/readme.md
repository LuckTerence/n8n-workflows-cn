## 简介
**Social Media Analysis and Automated Email Generation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：13 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2823

---

# Social Media Analysis and Automated Email Generation


## 节点清单

| 节点 | 类型 |
|------|------|
| Set your company's variables | 数据设置 |
| Get linkedin Posts | HTTP Request |
| Get twitter ID | HTTP Request |
| Get tweets | HTTP Request |
| Extract and limit Linkedin | Code |
| Exract and limit X | Code |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Generate Subject and cover letter based on match | LLM Chain |
| Send Cover letter and CC me | Email 发送 |
| Google Sheets Trigger | Google Sheets 触发器 |
| Google Sheets | Google Sheets |
| If | IF 判断 |

## 触发方式
- Google Sheets Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
