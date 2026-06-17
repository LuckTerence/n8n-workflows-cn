## 简介
**Automated AI & LLM Newsletter with BrowserAI and email-Telegram Delivery**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7975

---

# Automated AI & LLM Newsletter with BrowserAI and email-Telegram Delivery


## 节点清单

| 节点 | 类型 |
|------|------|
| Get yesterday's date | Code |
| Create a new task | HTTP Request |
| Get task's metadata | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Send a text message | Telegram |
| Check if finished | Switch 路由 |
| Wait for BrowserAI status change | 等待 |
| Clean output | Code |
| Send email | Email 发送 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
