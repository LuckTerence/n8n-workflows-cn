## 简介
**Evaluate organizational data maturity and email HTML reports with Postgres**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12963

---

# Evaluate organizational data maturity and email HTML reports with Postgres


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook1 | Webhook |
| Send Email seek chart wtith overall | Email 发送 |
| Calculate & Generate Charts | Code |
| Save Results | PostgreSQL |
| Save Form Details | PostgreSQL |
| Collect Step | 数据合并 |
| Collect Ranks | 数据合并 |
| Rank_Data_Strategy_Governance | PostgreSQL |
| Rank_Data_Quality_Integrity | PostgreSQL |
| Rank_Data_DrivenDecision_Intelligence | PostgreSQL |
| Rank_Data_Management_Operations | PostgreSQL |
| Rank_Data_Ethics_Privacy | PostgreSQL |
| Rank_AI_Maturity_Assessment | PostgreSQL |
| Rank_Overall_Avg | PostgreSQL |
| Create HTML FIle | 转换为文件 |
| HTML Body | 数据设置 |
| Merge | 数据合并 |
| DataCollector | 数据设置 |
| Generate Email styling and Formats | Code |
| Wait Save Form Details | 等待 |
| Wait Save Results | 等待 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Webhook 触发

## 触发方式
- Webhook1 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：19
- 输出节点：1
- 分类：workflow-automation
