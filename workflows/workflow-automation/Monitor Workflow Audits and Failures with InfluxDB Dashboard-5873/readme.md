## 简介
**Monitor Workflow Audits and Failures with InfluxDB Dashboard**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5873

---

# Monitor Workflow Audits and Failures with InfluxDB Dashboard


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Database Audit | n8n |
| Filesystem Audit | n8n |
| Instance Audit | n8n |
| Nodes Audit | n8n |
| Credentials Audit | n8n |
| Split Report Data | 数据拆分 |
| Prepare Influx Input Strings | 数据设置 |
| Contactenate with Commas | 文本摘要 |
| Pull Report Data and Risk Credentials | 数据设置 |
| Pull Report Data and Risk Database | 数据设置 |
| Pull Report Data and Risk Filesystem | 数据设置 |
| Pull Report Data and Risk Instance | 数据设置 |
| Pull Report Data and Risk Nodes | 数据设置 |
| Influx Globals | 数据设置 |
| Once a Day | 定时触发器 |
| Get Active Workflows | n8n |
| Get Failed Executions | n8n |
| Count Active | 文本摘要 |
| Count Failed | 文本摘要 |
| Merge Into One Reporting Line | 数据合并 |
| Adjust Field Name | 数据设置 |
| Send Workflows and Fails to InfluxDB | HTTP Request |
| Send Audit to InfluxDB | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Once a Day 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：20
- 输出节点：2
- 分类：workflow-automation
