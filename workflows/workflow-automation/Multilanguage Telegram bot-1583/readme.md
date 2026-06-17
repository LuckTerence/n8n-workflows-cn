## 简介
**Multilanguage Telegram bot**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：16 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/1583

---

# Multilanguage Telegram bot


## 节点清单

| 节点 | 类型 |
|------|------|
| chatID | Function |
| Merge | 数据合并 |
| Switch | Switch 路由 |
| IF | IF 判断 |
| msg_greet | Telegram |
| msg_welcomeback | Telegram |
| msg_help | Telegram |
| msg_wrongcommand | Telegram |
| New user? | Function |
| CheckUser | NocoDB |
| LoadDictionary | NocoDB |
| botmessages | Function |
| Telegram Trigger | Telegram 触发器 |
| HTTP AddUser | HTTP Request |
| HTTP UpdateUser | HTTP Request |
| AddUser | NocoDB |
| UpdateUser | NocoDB |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：10
- 输出节点：6
- 分类：workflow-automation
