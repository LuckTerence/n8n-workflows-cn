## 简介
**Convert Markdown Content to Contentful Rich Text with AI Formatting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4078

---

# Convert Markdown Content to Contentful Rich Text with AI Formatting


## 节点清单

| 节点 | 类型 |
|------|------|
| Create newly formatted Contentful Entry | HTTP Request |
| When Executed by Another Workflow | 执行工作流触发器 |
| Merge1 | 数据合并 |
| Format1 | Code |
| Markdown to Contentful format | AI Agent |
| Split by Headings | Code |
| Combine Rich Text Objects | Code |
| OpenAI Chat Model2 | OpenAI Chat Model |

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
