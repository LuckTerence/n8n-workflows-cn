## 简介
**Receipt Scanning & Analysis Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7990

---

# Receipt Scanning & Analysis Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Drive Trigger | Google Drive 触发器 |
| HTTP Request | HTTP Request |
| Extract text | mistralAi |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Append row in sheet | Google Sheets |

## 触发方式
- Google Drive Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
