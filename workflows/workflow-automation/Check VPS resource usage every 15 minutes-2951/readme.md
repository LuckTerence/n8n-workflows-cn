# Check VPS resource usage every 15 minutes

https://n8nworkflows.xyz/workflows/2951

## 节点清单

| 节点 | 类型 |
|------|------|
| Send Email | Email 发送 |
| Check RAM usage | SSH |
| Check Disk usage | SSH |
| Check CPU usage | SSH |
| Merge check results | 数据合并 |
| Check results against thresholds | IF 判断 |
| Schedule Trigger | 定时触发器 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
