## 简介
**AI SEO Readability Audit: Check Website Friendliness for LLMs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4151

---

# AI SEO Readability Audit: Check Website Friendliness for LLMs


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Get HTML from Website | HTTP Request |
| Sanitize Website URL | Code |
| Extract HTML Features | Code |
| AI SEO Analysis | LLM Chain |
| OpenAI Chat Model | OpenAI Chat Model |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
