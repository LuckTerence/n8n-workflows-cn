# Pull Square Sales Summary Reports for Automated Reporting and Analysis

https://n8nworkflows.xyz/workflows/6358

## 节点清单

| 节点 | 类型 |
|------|------|
| Get Square Locations | HTTP Request |
| Turn Locations Into List | 数据拆分 |
| Ignore Locations w/o Sales | IF 判断 |
| Get Sales from Square | HTTP Request |
| When Executed by Another Workflow | 执行工作流触发器 |
| Compile Sales Reports | Code |

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
