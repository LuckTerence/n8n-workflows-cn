# 弃购挽回分析

https://n8nworkflows.xyz/workflows/6045

## 节点清单

| 节点 | 类型 |
|------|------|
| Cart Abandoned Webhook | Webhook |
| Recovery Settings | 数据设置 |
| Qualify Cart | IF 判断 |
| Generate Recovery Data | Code |
| Wait 1 Hour | 等待 |
| Send First Recovery Email | Gmail |
| Wait 23 Hours More | 等待 |
| Send Second Recovery Email | Gmail |
| Wait 48 Hours More | 等待 |
| Send Final Recovery Email | Gmail |
| Track Recovery Start | Google Sheets |

## 触发方式
- Cart Abandoned Webhook 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
