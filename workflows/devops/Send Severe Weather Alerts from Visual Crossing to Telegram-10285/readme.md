## 简介
**Send Severe Weather Alerts from Visual Crossing to Telegram**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：4 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/10285

---

# Send Severe Weather Alerts from Visual Crossing to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Home Weather | HTTP Request |
| Check for Home Weather Alerts | Function |
| Send Home Weather Alert | Telegram |
| Hourly Trigger | 定时触发器 |
| If | IF 判断 |

## 触发方式
- Hourly Trigger 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：2
- 输出节点：2
- 分类：devops
