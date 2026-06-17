## 简介
**Send Telegram notifications for new Feedspace testimonials**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12152

---

# Send Telegram notifications for new Feedspace testimonials


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Feedspace Webhook | Webhook |
| Send Telegram Notification | Telegram |
| Has Error? | IF 判断 |
| Success Response | 响应 Webhook |
| Format Error Details | Code |
| Error Response | 响应 Webhook |

## 触发方式
- Receive Feedspace Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：2
- 输出节点：3
- 分类：workflow-automation
