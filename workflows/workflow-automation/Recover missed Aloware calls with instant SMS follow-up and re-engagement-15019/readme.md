# Recover missed Aloware calls with instant SMS follow-up and re-engagement

https://n8nworkflows.xyz/workflows/15019

## 节点清单

| 节点 | 类型 |
|------|------|
| Aloware: Missed Call Event | Webhook |
| Extract Caller Data | 数据设置 |
| Aloware: Send Missed-Call SMS | HTTP Request |
| Wait 2 Hours | 等待 |
| Aloware: Lookup Contact Status | HTTP Request |
| Did Contact Reply? | IF 判断 |
| Already Engaged — No Action | 空操作 |
| Aloware: Send Follow-up SMS | HTTP Request |
| Aloware: Enroll in Re-engagement Sequence | HTTP Request |

## 触发方式
- Aloware: Missed Call Event 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
