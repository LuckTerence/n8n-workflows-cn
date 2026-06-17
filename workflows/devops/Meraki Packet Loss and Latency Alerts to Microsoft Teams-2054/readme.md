# Meraki Packet Loss and Latency Alerts to Microsoft Teams

https://n8nworkflows.xyz/workflows/2054

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Get Meraki Organizations | HTTP Request |
| Get Network IDs | HTTP Request |
| Get Org Name & ID | 数据设置 |
| Combine latency to its respective Network | 数据合并 |
| Makes Latency and Loss Filterable | 数据设置 |
| Filters Problematic sites | Code |
| Average Latency & Loss over 5m | Code |
| Get Uplink Loss and Latency | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Sets Network Variables | 数据设置 |
| Merge | 数据合并 |
| Check if Alert Exists | Redis |
| Create Response | Code |
| Message Techs | Teams |
| Log the Alert | Redis |

## 触发方式
- When clicking "Execute Workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：10
- 输出节点：4
- 分类：devops
