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



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发、手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Once a Day 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：20
- 输出节点：2
- 分类：workflow-automation
