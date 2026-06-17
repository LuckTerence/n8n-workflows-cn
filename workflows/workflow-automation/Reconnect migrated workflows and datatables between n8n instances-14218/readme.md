## 简介
**Reconnect migrated workflows and datatables between n8n instances**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14218

---

# Reconnect migrated workflows and datatables between n8n instances


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| orig datatables | HTTP Request |
| orig workflows | HTTP Request |
| new datatables | HTTP Request |
| new workflows | HTTP Request |
| config | Code |
| map | Code |
| update flow nodes | Code |
| update new workflows | n8n |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：4
- 输出节点：4
- 分类：workflow-automation
