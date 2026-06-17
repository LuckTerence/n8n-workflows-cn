# Automated GLPI Ticket Deadline Alerts via Microsoft Teams

https://n8nworkflows.xyz/workflows/7436

## 节点清单

| 节点 | 类型 |
|------|------|
| No Operation, do nothing3 | 空操作 |
| End session1 | HTTP Request |
| No Operation, do nothing2 | 空操作 |
| Configuration Variables | 数据设置 |
| Send a message to Support Technician 1 | Teams |
| Send a message to Support Technician 2 | Teams |
| Aggregate | 数据聚合 |
| Tickets about to expire | HTTP Request |
| Get session token | HTTP Request |
| Support Technician 1? | IF 判断 |
| Support Technician 2? | IF 判断 |
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| Split Out | 数据拆分 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：devops
