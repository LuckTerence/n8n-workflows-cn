## 简介
**Automate demand forecasting & inventory ordering with AI, MySQL & optimal supplier selection**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12158

---

# Automate demand forecasting & inventory ordering with AI, MySQL & optimal supplier selection


## 节点清单

| 节点 | 类型 |
|------|------|
| Run Daily at 03:00 | 定时触发器 |
| Fetch POS Data | HTTP Request |
| Fetch Historical Sales | MySQL |
| Fetch Weather Forecast | HTTP Request |
| Fetch SNS Trends | HTTP Request |
| Fetch Inventory Master | HTTP Request |
| Merge Data 1 | 数据合并 |
| Merge Data 2 | 数据合并 |
| Format Prediction Dataset | Code |
| Call AI Prediction API | HTTP Request |
| Calculate Stock Shortage | Code |
| Finalize Order Qty | Code |
| Check Order Necessity | IF 判断 |
| Split by Product | 分批处理 |
| Get Quote Supplier A | HTTP Request |
| Get Quote Supplier B | HTTP Request |
| Get Quote Supplier C | HTTP Request |
| Merge Quotes | 数据合并 |
| Select Best Supplier | Code |
| Execute Auto Order | HTTP Request |
| Update Inventory System | HTTP Request |
| Save Order Log | MySQL |
| Check Anomalies | IF 判断 |
| Slack Anomaly Alert | Slack |

## 触发方式
- Run Daily at 03:00 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：12
- 输出节点：11
- 分类：workflow-automation
