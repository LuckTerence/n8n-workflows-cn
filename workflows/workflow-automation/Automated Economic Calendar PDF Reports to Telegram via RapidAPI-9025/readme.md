## 简介
**Automated Economic Calendar PDF Reports to Telegram via RapidAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9025

---

# Automated Economic Calendar PDF Reports to Telegram via RapidAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Dynamically Sets the Date | Code |
| Schedule Every 7  Days | 定时触发器 |
| Set API Key for RapidAPI & Dates | 数据设置 |
| Gets Upcoming News | HTTP Request |
| Filter Medium & High Impact News | Code |
| Convert All Items Into One Array | Code |
| Edit & Update Template | HTTP Request |
| Download PDF Report | HTTP Request |
| Organize Data for API Template | Code |
| Send Economic Calendar Events PDF to Telegram | Telegram |

## 触发方式
- Schedule Every 7  Days 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：5
- 输出节点：4
- 分类：workflow-automation
