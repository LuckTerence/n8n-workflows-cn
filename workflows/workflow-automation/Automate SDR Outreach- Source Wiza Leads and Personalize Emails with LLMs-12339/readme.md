## 简介
**Automate SDR Outreach: Source Wiza Leads and Personalize Emails with LLMs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12339

---

# Automate SDR Outreach: Source Wiza Leads and Personalize Emails with LLMs


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Smartlead Campaign | HTTP Request |
| Fetch Email Accounts | HTTP Request |
| Find Least Used Account | Code |
| Save Sequence Templates | HTTP Request |
| Update Campaign Settings | HTTP Request |
| Upload Lead to Smartlead | HTTP Request |
| Structured Output Parser9 | 结构化输出解析器 |
| Get Lists Contacts | HTTP Request |
| Simple Memory7 | 记忆缓冲区 |
| OpenRouter Chat Model7 | OpenRouter Chat Model |
| Search Prospects [Wiza-API] | HTTP Request |
| Loop Over Items | 分批处理 |
| Business Context | 数据设置 |
| Perplexity Research Tool | perplexityTool |
| Payload aggregator | Code |
| Ice Breaker Email | 数据设置 |
| Lead_info | 数据设置 |
| Schedule Campaign | HTTP Request |
| Start Campaign | HTTP Request |
| Set Campaign id | 数据设置 |
| Add Email Account to Campaign | HTTP Request |
| Campaign Generation Form | 表单触发器 |
| Set Campaign Details | 数据设置 |
| Build Sequence Templates | Code |
| Format Search Parameters | AI Agent |
| Get Lists | HTTP Request |
| Check If Finished | IF 判断 |
| Wait | 等待 |
| Standardize Data | Code |
| Update Leads | 数据表 |
| Research agent | AI Agent |
| Ice Breaker Email Generator | AI Agent |
| Follow-Up Sequence Generator | AI Agent |
| LLM | OpenRouter Chat Model |
| LLM1 | OpenRouter Chat Model |
| Memory 1 | 记忆缓冲区 |
| Memory 2 | 记忆缓冲区 |
| Get Case Studies | dataTableTool |
| Structured Output Parser - 1 | 结构化输出解析器 |
| LLM2 | OpenRouter Chat Model |
| Memory 3 | 记忆缓冲区 |
| Get Case Studies 2 | dataTableTool |
| Structured Output Parser - 2 | 结构化输出解析器 |
| Follow-up Sequence Generator set | 数据设置 |

## 触发方式
- Campaign Generation Form 触发

## 统计
- 节点总数：44
- 触发节点：1
- 处理节点：32
- 输出节点：11
- 分类：workflow-automation
