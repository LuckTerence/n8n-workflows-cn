## 简介
**AI Automated HR Workflow for CV Analysis and Candidate Evaluation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2860

---

# AI Automated HR Workflow for CV Analysis and Candidate Evaluation


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Extract from File | 从文件提取 |
| Qualifications | 信息提取器 |
| Summarization Chain | chainSummarization |
| Merge | 数据合并 |
| Profile Wanted | 数据设置 |
| Google Sheets | Google Sheets |
| Structured Output Parser | 结构化输出解析器 |
| HR Expert | LLM Chain |
| Personal Data | 信息提取器 |
| Upload CV | Google Drive |
| OpenAI | OpenAI Chat Model |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
