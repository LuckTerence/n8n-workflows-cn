## 简介
**Automated Daily Customer Win-Back Campaign with AI Offers**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4001

---

# Automated Daily Customer Win-Back Campaign with AI Offers


## 节点清单

| 节点 | 类型 |
|------|------|
| Scheduled Start: Daily Churn Check | 定时触发器 |
| Fetch Customer Data from Sheet | Google Sheets |
| Filter High Churn Risk & No Campaign Customers | 过滤器 |
| Check if Eligible Customers Found | IF 判断 |
| Process Each Eligible Customer | 分批处理 |
| Generate Win-Back Offer | LLM Chain |
| (LLM Model for Offer Generation) | OpenAI Chat Model |
| (Parse Offer JSON) | 结构化输出解析器 |
| Log Sent Offer in System Log | Google Sheets |
| Send Win-Back Offer via Email | Email 发送 |
| Set 'Not Found' Status | 数据设置 |
| Log 'Not Found' in System Log | Google Sheets |

## 触发方式
- Scheduled Start: Daily Churn Check 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
