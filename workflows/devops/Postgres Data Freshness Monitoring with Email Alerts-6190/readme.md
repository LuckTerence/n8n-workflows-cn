## 简介
**Postgres Data Freshness Monitoring with Email Alerts**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6190

---

# Postgres Data Freshness Monitoring with Email Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| Aggregate Stale Tables | 数据聚合 |
| Get most recent row from table | PostgreSQL |
| Calculate lag | 日期时间 |
| Add back table name | 数据设置 |
| Remove fresh tables | 过滤器 |
| Produce tables + date columns | Code |
| Send alerts | 执行工作流 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：devops
