## 简介
**Detect account and contact growth signals with Lusha bulk enrichment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13349

---

# Detect account and contact growth signals with Lusha bulk enrichment


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Signal Check | 定时触发器 |
| Get Target Accounts from CRM | hubspot |
| Format Companies for Bulk | Code |
| Enrich All Companies in Bulk | lusha |
| Detect Signals per Company | Code |
| Has Signals? | IF 判断 |
| Search for Key Contacts | lusha |
| Enrich Contacts from Search | lusha |
| Signal Alert to Sales | Slack |
| Update Account in CRM | hubspot |

## 触发方式
- Daily Signal Check 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
