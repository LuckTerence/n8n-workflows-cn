## 简介
**Prevent Duplicate Processing with Redis Item State Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6828

---

# Prevent Duplicate Processing with Redis Item State Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| Handle Invalid Action | 停止并报错 |
| Set CHECK Output | 数据设置 |
| Set ADD Output | 数据设置 |
| Redis: GET (Check Processed) | Redis |
| Redis: SET (Add to Processed) | Redis |
| Switch Action | Switch 路由 |
| Trigger (from other workflows) | 执行工作流触发器 |
| Redis: DELETE (Untrack Item) | Redis |
| To_redis-audit-log | Redis |
| Set DELETE Output | 数据设置 |
| Code: Prepare Audit Log & Response | Code |
| Set: Context for Response | 数据设置 |
| Redis: SET (Update Result)2 | Redis |
| Set UPDATE Output2 | 数据设置 |
| Parse Log Message | Code |
| redis-audit-log | Google Sheets |
| On new Redis event | redisTrigger |

## 触发方式
- Trigger (from other workflows) 触发
- On new Redis event 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：15
- 输出节点：0
- 分类：workflow-automation
