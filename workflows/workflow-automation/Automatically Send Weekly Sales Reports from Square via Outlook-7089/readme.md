# Automatically Send Weekly Sales Reports from Square via Outlook

https://n8nworkflows.xyz/workflows/7089

## 节点清单

| 节点 | 类型 |
|------|------|
| Get Square Locations | HTTP Request |
| Turn Locations Into List | 数据拆分 |
| Ignore Locations w/o Sales | IF 判断 |
| Get Sales from Square | HTTP Request |
| Compile Sales Reports | Code |
| Schedule Trigger | 定时触发器 |
| Convert Sales Summary to CSV File | 转换为文件 |
| Get Dates From Last Week | Code |
| Send Report | Outlook |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：5
- 输出节点：3
- 分类：workflow-automation
