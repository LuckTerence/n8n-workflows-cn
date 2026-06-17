## 简介
**Enrich up to 1500 emails per hour with Dropcontact batch requests**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2272

---

# Enrich up to 1500 emails per hour with Dropcontact batch requests


## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| PROFILES QUERY | PostgreSQL |
| BULK DROPCONTACT REQUESTS | HTTP Request |
| Loop Over Items2 | 分批处理 |
| Split Out | 数据拆分 |
| Postgres | PostgreSQL |
| BULK DROPCONTACT DOWNLOAD | HTTP Request |
| Wait2 | 等待 |
| DATA TRANSFORMATION | Code |
| Slack | Slack |
| Schedule Trigger | 定时触发器 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 数据库 + Slack + HTTP API 实现自动化。

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

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
