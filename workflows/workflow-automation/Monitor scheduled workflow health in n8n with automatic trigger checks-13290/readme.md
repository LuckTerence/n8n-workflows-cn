## 简介
**Monitor scheduled workflow health in n8n with automatic trigger checks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13290

---

# Monitor scheduled workflow health in n8n with automatic trigger checks


## 节点清单

| 节点 | 类型 |
|------|------|
| Test Run | 手动触发 |
| Daily Check at 9am | 定时触发器 |
| Fetch All Active Workflows | n8n |
| Discover Scheduled Workflows | Code |
| Get Latest Execution | n8n |
| Check for Stale Workflows | Code |
| Any Stale? | IF 判断 |
| Alert — Workflows Missed Schedule | 停止并报错 |
| All Healthy | 空操作 |

## 触发方式
- Test Run 触发
- Daily Check at 9am 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：workflow-automation
