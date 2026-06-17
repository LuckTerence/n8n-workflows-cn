# PRISM Elastic Alert Notification via Microsoft Graph API

https://n8nworkflows.xyz/workflows/2523

## 节点清单

| 节点 | 类型 |
|------|------|
| Get Elastic Alert | HTTP Request |
| Send Email Notification | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Response is not empty | IF 判断 |
| No Operation, do nothing | 空操作 |
| Loop Over Each Alert Items | 分批处理 |
| No Operation, end of loop | 空操作 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：devops
