## 简介
**Automated Hotel Price Drop Alerts with Email Notifications and Database Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10390

---

# Automated Hotel Price Drop Alerts with Email Notifications and Database Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule - Every 6 Hours | 定时触发器 |
| Load Hotel List | Code |
| Fetch Current Price from API | HTTP Request |
| Parse Price Data | Code |
| Get Previous Price from DB | HTTP Request |
| Compare Prices | Code |
| Check if Price Reduced | IF 判断 |
| Format Alert Email | Code |
| Send Email to Travel Agent | Email 发送 |
| Log Alert Sent | Code |
| Log No Alert Needed | Code |
| Merge All Logs | 数据合并 |
| Update Price in Database | HTTP Request |
| Create Execution Summary | Code |

## 触发方式
- Schedule - Every 6 Hours 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：9
- 输出节点：4
- 分类：workflow-automation
