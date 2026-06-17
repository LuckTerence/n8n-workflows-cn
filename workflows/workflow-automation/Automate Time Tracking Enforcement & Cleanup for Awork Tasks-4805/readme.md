## 简介
**Automate Time Tracking Enforcement & Cleanup for Awork Tasks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4805

---

# Automate Time Tracking Enforcement & Cleanup for Awork Tasks


## 节点清单

| 节点 | 类型 |
|------|------|
| Workflow config | 数据设置 |
| Fetch task changes | 数据设置 |
| Split out task changes | 数据拆分 |
| Filter task status change | 过滤器 |
| Check if task done | IF 判断 |
| Webhook call by Awork | Webhook |
| Check if force time tracking enabled | IF 判断 |
| Process tags and check if found in configured tags | Code |
| Check if tags listed in config node | IF 判断 |
| Check if comments are enabled | IF 判断 |
| Add comment to tasks | HTTP Request |
| Roll back task status from done to previous state | HTTP Request |
| Check tag restriction | IF 判断 |
| Check tracked time | IF 判断 |
| Check if comments are enabled1 | IF 判断 |
| Add comment to tasks1 | HTTP Request |
| Roll back task status from done to previous state1 | HTTP Request |
| Calculate time for added time tracking | Code |
| Calculate time for added time tracking1 | Code |
| Roll back task status from done to previous state4 | HTTP Request |
| Check if min time tracking OR time tracking cleanup is enabled | IF 判断 |
| Check tag restriction1 | IF 判断 |
| Process tags and check if found in configured tags1 | Code |
| If | IF 判断 |
| Switch | Switch 路由 |
| Load task details for time tracking item | HTTP Request |
| If1 | IF 判断 |
| Load system type of work | HTTP Request |
| Add tracked time to match min time settings | HTTP Request |
| If2 | IF 判断 |
| Add start time to time tracking entry | HTTP Request |

## 触发方式
- Webhook call by Awork 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：21
- 输出节点：9
- 分类：workflow-automation
