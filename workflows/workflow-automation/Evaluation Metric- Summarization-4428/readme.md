## 简介
**Evaluation Metric: Summarization**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4428

---

# Evaluation Metric: Summarization


## 节点清单

| 节点 | 类型 |
|------|------|
| Is Evaluating? | 条件评估 |
| OpenAI Chat Model | OpenAI Chat Model |
| When fetching a dataset row | evaluationTrigger |
| Respond to User | 空操作 |
| LLM | OpenAI Chat Model |
| Output | 结构化输出解析器 |
| Set Outputs | 条件评估 |
| Set Metrics | 条件评估 |
| Download Transcript | Google Drive |
| Summarise Agent | LLM Chain |
| Extract from File | 从文件提取 |
| Webhook | Webhook |
| Get Gdrive URL | 数据设置 |
| Evaluate Summarisation | LLM Chain |

## 触发方式
- When fetching a dataset row 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：12
- 输出节点：0
- 分类：workflow-automation
