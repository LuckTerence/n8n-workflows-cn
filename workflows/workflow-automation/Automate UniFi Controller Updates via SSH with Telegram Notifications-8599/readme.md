## 简介
**Automate UniFi Controller Updates via SSH with Telegram Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8599

---

# Automate UniFi Controller Updates via SSH with Telegram Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| HTTP Request | HTTP Request |
| Extract Codename + Date + Time Comparison | Code |
| If: Changed within 24h? | IF 判断 |
| Update package lists | SSH |
| Upgrade UniFi | SSH |
| Message a model | OpenAI |
| Notify via Telegram | Telegram |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
