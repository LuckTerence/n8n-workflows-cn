## 简介
**AI Prompt Generator Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5045

---

# AI Prompt Generator Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| BaseQuestions | 表单 |
| LoopQuestions | 分批处理 |
| RelevantQuestions | 表单 |
| MergeUserIntent | 数据合并 |
| PromptGenerator | LLM Chain |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| RelatedQuestionAI | LLM Chain |
| SplitQuestions | 数据拆分 |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Structured Output Parser1 | 结构化输出解析器 |
| SendingPrompt | 表单 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
