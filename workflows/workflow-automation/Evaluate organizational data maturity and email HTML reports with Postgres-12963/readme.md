## 简介
**Evaluate organizational data maturity and email HTML reports with Postgres**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12963

---

# Evaluate organizational data maturity and email HTML reports with Postgres


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook1 | Webhook |
| Send Email seek chart wtith overall | Email 发送 |
| Calculate & Generate Charts | Code |
| Save Results | PostgreSQL |
| Save Form Details | PostgreSQL |
| Collect Step | 数据合并 |
| Collect Ranks | 数据合并 |
| Rank_Data_Strategy_Governance | PostgreSQL |
| Rank_Data_Quality_Integrity | PostgreSQL |
| Rank_Data_DrivenDecision_Intelligence | PostgreSQL |
| Rank_Data_Management_Operations | PostgreSQL |
| Rank_Data_Ethics_Privacy | PostgreSQL |
| Rank_AI_Maturity_Assessment | PostgreSQL |
| Rank_Overall_Avg | PostgreSQL |
| Create HTML FIle | 转换为文件 |
| HTML Body | 数据设置 |
| Merge | 数据合并 |
| DataCollector | 数据设置 |
| Generate Email styling and Formats | Code |
| Wait Save Form Details | 等待 |
| Wait Save Results | 等待 |

## 触发方式
- Webhook1 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：19
- 输出节点：1
- 分类：workflow-automation
