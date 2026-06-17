## 简介
**Real Estate Cold Call Scripts for Price Reduced FSBO Properties (Zillow Data)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3143

---

# Real Estate Cold Call Scripts for Price Reduced FSBO Properties (Zillow Data)


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Zillow Search | HTTP Request |
| RentZestimate | HTTP Request |
| Split Out | 数据拆分 |
| market_overview | HTTP Request |
| Edit Fields1 | 数据设置 |
| FSBO | 执行工作流触发器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Execute Workflow | 执行工作流 |
| Investment Calculator | Code |
| FSBO Property Criteria Set | 数据设置 |
| Call Script Database Airtable | Airtable |
| Call Script Generator | OpenAI |
| Historical Market Summary | chainSummarization |
| Historical Market Results Indicator | Code |

## 触发方式
- On form submission 触发
- FSBO 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
