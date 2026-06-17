## 简介
**Add User Authorization Layer to Your Telegram Bot with Admin Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9203

---

# Add User Authorization Layer to Your Telegram Bot with Admin Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| BotGuard Authorization | Code |
| Check Authorization | IF 判断 |
| Send Success | Telegram |
| Send Denied | Telegram |
| Check Admin Notify | IF 判断 |
| Prepare Admin Notifications | Code |
| Telegram Trigger | Telegram 触发器 |
| Notify Admin | Telegram |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：devops
