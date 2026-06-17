## 简介
**Automate Daily GLPI Pending Ticket Notifications to Microsoft Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/7018

---

# Automate Daily GLPI Pending Ticket Notifications to Microsoft Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Get pending cases | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| No Operation, do nothing | 空操作 |
| Create chat message | Teams |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| No Operation, do nothing1 | 空操作 |
| Get session token | HTTP Request |
| Are there any ongoing cases? | IF 判断 |
| End session | HTTP Request |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
