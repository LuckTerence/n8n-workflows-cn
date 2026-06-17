## 简介
**Retrieve Deadlock Game Match Statistics and Send to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：6 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4571

---

# Retrieve Deadlock Game Match Statistics and Send to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Send Telegram Message | Telegram |
| Fetch Profile HTML | HTTP Request |
| Extract Match ID | Function |
| Fetch Match HTML | HTTP Request |
| Parse Players | Function |
| Format Message | Function |
| Telegram Trigger | Telegram 触发器 |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
