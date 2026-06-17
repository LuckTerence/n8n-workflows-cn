## 简介
**Get data from multiple RSS feeds to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/1554

---

# Get data from multiple RSS feeds to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| RSS Feed Read | RSS Feed |
| SplitInBatches | 分批处理 |
| Cron | 定时触发器 |
| only get new RSS | Function |
| Telegram_IT | Telegram |
| Telegram_Security | Telegram |
| RSS Source | Function |
| Telegram_M365 | Telegram |
| IF-2 | IF 判断 |
| IF-1 | IF 判断 |
| Clear Function | Function |

## 触发方式
- RSS Feed Read 触发
- Cron 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
