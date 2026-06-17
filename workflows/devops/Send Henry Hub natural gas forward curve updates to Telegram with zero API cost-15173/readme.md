## 简介
**Send Henry Hub natural gas forward curve updates to Telegram with zero API cost**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/15173

---

# Send Henry Hub natural gas forward curve updates to Telegram with zero API cost


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Natural Gas Page1 | HTTP Request |
| Market Hours Trigger1 | 定时触发器 |
| Extract Spot & Futures1 | Code |
| Build HTML Table1 | Code |
| Send Telegram Update1 | Telegram |

## 触发方式
- Market Hours Trigger1 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：devops
