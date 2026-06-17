## 简介
**Automate Docker Container Updates with Telegram Approval System**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3386

---

# Automate Docker Container Updates with Telegram Approval System


## 节点清单

| 节点 | 类型 |
|------|------|
| Pull n8n Image | SSH |
| docker compose pull | SSH |
| check n8n installed version | SSH |
| When clicking ‘Test workflow’ | 手动触发 |
| Schedule Trigger | 定时触发器 |
| docker compose up | SSH |
| Set Default variable | 数据设置 |
| Github HTTP Request | HTTP Request |
| Merge Results | 数据合并 |
| Edit Version String | 数据设置 |
| Comapre Two Input | IF 判断 |
| Telegram Notif | Telegram |
| Telegram Approve | Telegram |
| Telegram Notif1 | Telegram |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：8
- 输出节点：4
- 分类：devops
