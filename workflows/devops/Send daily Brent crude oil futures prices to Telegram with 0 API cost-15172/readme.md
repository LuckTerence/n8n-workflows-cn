## 简介
**Send daily Brent crude oil futures prices to Telegram with 0 API cost**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/15172

---

# Send daily Brent crude oil futures prices to Telegram with 0 API cost


## 节点清单

| 节点 | 类型 |
|------|------|
| Market Hours Trigger1 | 定时触发器 |
| Fetch Brent Page1 | HTTP Request |
| Parse 10 Contracts1 | Code |
| Aggregate Items1 | 数据聚合 |
| Send Telegram Table1 | Telegram |

## 触发方式
- Market Hours Trigger1 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：devops
