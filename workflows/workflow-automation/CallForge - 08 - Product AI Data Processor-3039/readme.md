# CallForge - 08 - Product AI Data Processor

https://n8nworkflows.xyz/workflows/3039

## 节点清单

| 节点 | 类型 |
|------|------|
| Execute Workflow Trigger | 执行工作流触发器 |
| Check if Product Data Found | IF 判断 |
| Create Product Data Object1 | Notion |
| Create Product Feedback Data Object | Notion |
| Check if AI Use Case Data Found | IF 判断 |
| Check if AI Mentioned On Call | IF 判断 |
| Wait for rate limiting - AI Use Case | 等待 |
| Wait for rate limiting - Product Data | 等待 |
| Split Out Product Data | 数据拆分 |
| Bundle AI Use Case Data to 1 object | 数据聚合 |
| Bundle Product Feedback Data to 1 object | 数据聚合 |
| Merge AI Use Case Thread | 数据设置 |
| Merge Product Feedback Thread | 数据设置 |
| Update Call with AI Data Summary | Notion |

## 触发方式
- Execute Workflow Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
