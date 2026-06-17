## 简介
**Automate n8n User Invitations from a Google Spreadsheet**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3233

---

# Automate n8n User Invitations from a Google Spreadsheet


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Get all Users | HTTP Request |
| Get all rows | Google Sheets |
| Get non-users | 数据合并 |
| Invite Users | HTTP Request |
| Schedule Trigger | 定时触发器 |
| Edit Fields | 数据设置 |
| Create users list | 数据设置 |
| Combine all paginated results | Code |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
