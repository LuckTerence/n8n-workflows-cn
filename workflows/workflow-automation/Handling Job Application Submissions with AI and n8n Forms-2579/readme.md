# Handling Job Application Submissions with AI and n8n Forms

https://n8nworkflows.xyz/workflows/2579

## 节点清单

| 节点 | 类型 |
|------|------|
| Extract from File | 从文件提取 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Step 1 of 2 - Upload CV | 表单触发器 |
| Save to Airtable | Airtable |
| Classify Document | 文本分类器 |
| Upload File to Record | HTTP Request |
| Form Success | 表单 |
| Save to Airtable1 | Airtable |
| Step 2 of 2 - Application Form | 表单触发器 |
| Application Suitability Agent | LLM Chain |
| File Upload Retry | 表单 |
| Redirect To Step 2 of 2 | 表单 |
| Submission Success | 表单 |

## 触发方式
- Step 1 of 2 - Upload CV 触发
- Step 2 of 2 - Application Form 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
