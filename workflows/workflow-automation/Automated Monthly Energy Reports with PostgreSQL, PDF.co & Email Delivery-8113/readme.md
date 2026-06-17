## 简介
**Automated Monthly Energy Reports with PostgreSQL, PDF.co & Email Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8113

---

# Automated Monthly Energy Reports with PostgreSQL, PDF.co & Email Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| Transform data | Code |
| Convert data to pdf | HTTP Request |
| Send Report | Email 发送 |
| Get energy data | PostgreSQL |
| Monthly Trigger | 定时触发器 |

## 触发方式
- Monthly Trigger 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：workflow-automation
