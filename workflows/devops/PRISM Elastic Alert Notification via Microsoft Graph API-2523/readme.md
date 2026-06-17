## 简介
**PRISM Elastic Alert Notification via Microsoft Graph API**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2523

---

# PRISM Elastic Alert Notification via Microsoft Graph API


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
