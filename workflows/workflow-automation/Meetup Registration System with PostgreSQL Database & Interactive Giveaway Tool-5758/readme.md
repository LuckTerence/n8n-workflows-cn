## 简介
**Meetup Registration System with PostgreSQL Database & Interactive Giveaway Tool**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5758

---

# Meetup Registration System with PostgreSQL Database & Interactive Giveaway Tool


## 节点清单

| 节点 | 类型 |
|------|------|
| Thank you screen | 表单 |
| Format participant list | Code |
| Mapping form to database | 数据设置 |
| Get all participants | PostgreSQL |
| Giveaway App | Webhook |
| Respond to Giveaway App | 响应 Webhook |
| Participant Form | 表单触发器 |
| Save Participant to Database | PostgreSQL |

## 触发方式
- Giveaway App 触发
- Participant Form 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
