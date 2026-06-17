# Automated error monitoring and reporting system using data tables

https://n8nworkflows.xyz/workflows/12724

## 节点清单

| 节点 | 类型 |
|------|------|
| Error Trigger | 错误触发器 |
| Ignore Manual Failures | 过滤器 |
| Aggregate | 数据聚合 |
| Time Saved | timeSaved |
| Split Out | 数据拆分 |
| Update Last Emailed At | 数据表 |
| Get Errors that were not Emailed | 数据表 |
| map fields to data table | 数据设置 |
| OpenAI Chat Model | OpenAI Chat Model |
| AI Error Summarizer | AI Agent |
| Email Error Details | Email 发送 |
| Insert Error Details | 数据表 |
| Calculator | 计算器工具 |
| Sort | 数据排序 |
| high error count or been a day1 | 过滤器 |
| Run every hour | 定时触发器 |
| Generate Workflow Errors Table HTML | HTML |

## 触发方式
- Error Trigger 触发
- Run every hour 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：14
- 输出节点：1
- 分类：workflow-automation
