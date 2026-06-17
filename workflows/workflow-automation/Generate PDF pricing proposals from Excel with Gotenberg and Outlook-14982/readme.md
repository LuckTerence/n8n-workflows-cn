## 简介
**Generate PDF pricing proposals from Excel with Gotenberg and Outlook**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14982

---

# Generate PDF pricing proposals from Excel with Gotenberg and Outlook


## 节点清单

| 节点 | 类型 |
|------|------|
| Pricing Request Webhook | Webhook |
| Fetch Pricing Sheet | microsoftExcel |
| Process & Price | Code |
| Build HTML Proposal | Code |
| Gotenberg → PDF | HTTP Request |
| Send a message | Outlook |

## 触发方式
- Pricing Request Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
