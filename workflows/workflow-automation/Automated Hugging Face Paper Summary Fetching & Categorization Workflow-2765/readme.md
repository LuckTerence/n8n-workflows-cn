# Automated Hugging Face Paper Summary Fetching & Categorization Workflow

https://n8nworkflows.xyz/workflows/2765

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| If | IF 判断 |
| Loop Over Items | 分批处理 |
| Split Out | 数据拆分 |
| Request Hugging Face Paper | HTTP Request |
| Extract Hugging Face Paper | HTML |
| Check Paper URL Existed | Notion |
| Request Hugging Face Paper Detail | HTTP Request |
| Extract Hugging Face Paper Abstract | HTML |
| OpenAI Analysis Abstract | OpenAI |
| Store Abstract Notion | Notion |
| Send Analysis Result Slack | Slack |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
