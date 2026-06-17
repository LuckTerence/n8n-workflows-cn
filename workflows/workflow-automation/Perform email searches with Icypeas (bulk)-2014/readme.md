## 简介
**Perform email searches with Icypeas (bulk)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2014

---

# Perform email searches with Icypeas (bulk)


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Authenticates to your Icypeas account | Code |
| Reads lastname,firstname and company from your sheet | Google Sheets |
| Run bulk search (email-search) | HTTP Request |

## 触发方式
- When clicking "Execute Workflow" 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：2
- 输出节点：1
- 分类：workflow-automation
