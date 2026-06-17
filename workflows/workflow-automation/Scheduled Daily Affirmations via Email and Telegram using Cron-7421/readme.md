## 简介
**Scheduled Daily Affirmations via Email and Telegram using Cron**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/7421

---

# Scheduled Daily Affirmations via Email and Telegram using Cron


## 节点清单

| 节点 | 类型 |
|------|------|
| Cron: Trigger Daily at 7 AM | 定时触发器 |
| Set: Configuration (edit me) | 数据设置 |
| Code: Pick Random Affirmation | Code |
| IF: Telegram Enabled? | IF 判断 |
| Email: Send Affirmation | Email 发送 |
| Telegram: Send Affirmation | Telegram |

## 触发方式
- Cron: Trigger Daily at 7 AM 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
