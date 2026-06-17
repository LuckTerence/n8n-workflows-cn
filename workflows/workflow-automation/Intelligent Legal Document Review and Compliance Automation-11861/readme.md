## 简介
**Intelligent Legal Document Review and Compliance Automation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11861

---

# Intelligent Legal Document Review and Compliance Automation


## 节点清单

| 节点 | 类型 |
|------|------|
| Document Upload Webhook | Webhook |
| Workflow Configuration | 数据设置 |
| Extract Document Text | 从文件提取 |
| Clause Analysis Agent | AI Agent |
| OpenAI Model - Clause Analysis | OpenAI Chat Model |
| Clause Analysis Output Parser | 结构化输出解析器 |
| Compliance Check Agent | AI Agent |
| OpenAI Model - Compliance | OpenAI Chat Model |
| Compliance Output Parser | 结构化输出解析器 |
| Alternative Wording Agent | AI Agent |
| OpenAI Model - Alternative Wording | OpenAI Chat Model |
| Alternative Wording Output Parser | 结构化输出解析器 |
| Summary Report Generator | AI Agent |
| OpenAI Model - Summary | OpenAI Chat Model |
| Prepare Database Record | 数据设置 |
| Log to Contract Database | PostgreSQL |
| Send Notification | HTTP Request |

## 触发方式
- Document Upload Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：15
- 输出节点：1
- 分类：workflow-automation
