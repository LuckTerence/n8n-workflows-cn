## 简介
**Automated Hugging Face Paper Summary Fetching & Categorization Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2765

---

# Automated Hugging Face Paper Summary Fetching & Categorization Workflow


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
