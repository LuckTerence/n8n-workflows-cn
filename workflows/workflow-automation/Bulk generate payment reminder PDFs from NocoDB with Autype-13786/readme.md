# Bulk generate payment reminder PDFs from NocoDB with Autype

https://n8nworkflows.xyz/workflows/13786

## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Schedule | 定时触发器 |
| Get Overdue Invoices | NocoDB |
| Build Bulk Items | Code |
| Bulk Render Payment Reminders | autype |
| Send ZIP via Email | Email 发送 |
| Run Setup Once | 手动触发 |
| Create Project | autype |
| Create Document | autype |

## 触发方式
- Weekly Schedule 触发
- Run Setup Once 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
