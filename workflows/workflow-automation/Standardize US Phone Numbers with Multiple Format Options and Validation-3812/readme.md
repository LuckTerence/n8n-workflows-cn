# Standardize US Phone Numbers with Multiple Format Options and Validation

https://n8nworkflows.xyz/workflows/3812

## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Check if first digit is valid country code | IF 判断 |
| Add valid country code | 数据设置 |
| Strip phone number formatting | 数据设置 |
| Check number of digits in phone number | Switch 路由 |
| Format phone numbers | 数据设置 |
| Clear invalid number | 数据设置 |

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
