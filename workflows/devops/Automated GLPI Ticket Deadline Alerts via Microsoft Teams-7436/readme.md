## 简介
**Automated GLPI Ticket Deadline Alerts via Microsoft Teams**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7436

---

# Automated GLPI Ticket Deadline Alerts via Microsoft Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| No Operation, do nothing3 | 空操作 |
| End session1 | HTTP Request |
| No Operation, do nothing2 | 空操作 |
| Configuration Variables | 数据设置 |
| Send a message to Support Technician 1 | Teams |
| Send a message to Support Technician 2 | Teams |
| Aggregate | 数据聚合 |
| Tickets about to expire | HTTP Request |
| Get session token | HTTP Request |
| Support Technician 1? | IF 判断 |
| Support Technician 2? | IF 判断 |
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| Split Out | 数据拆分 |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：devops
