## 简介
**Convert Gumroad Sales to Beehiiv Subscribers with Sheets & Telegram Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3715

---

# Convert Gumroad Sales to Beehiiv Subscribers with Sheets & Telegram Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Gumroad Sale Trigger | gumroadTrigger |
| append row in CRM | Google Sheets |
| List publications | HTTP Request |
| Post subscription | HTTP Request |
| Notify in channel | Telegram |
| Set ChatID | 数据设置 |

## 触发方式
- Gumroad Sale Trigger 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
