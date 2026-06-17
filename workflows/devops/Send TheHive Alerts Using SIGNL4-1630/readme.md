## 简介
**Send TheHive Alerts Using SIGNL4**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：5 | 难度：⭐ 入门
> 原始来源：https://n8nworkflows.xyz/workflows/1630

---

# Send TheHive Alerts Using SIGNL4


## 节点清单

| 节点 | 类型 |
|------|------|
| TheHive Create Alert | theHive |
| TheHive Read Alerts | theHive |
| IF | IF 判断 |
| SIGNL4 Send Alert | signl4 |
| TheHive Webhook Request | Webhook |
| Start (Testing) | 手动触发 |
| SIGNL4 Resolve Alert | signl4 |

## 触发方式
- TheHive Webhook Request 触发
- Start (Testing) 触发

## 统计
- 节点总数：7
- 触发节点：2
- 处理节点：5
- 输出节点：0
- 分类：devops
