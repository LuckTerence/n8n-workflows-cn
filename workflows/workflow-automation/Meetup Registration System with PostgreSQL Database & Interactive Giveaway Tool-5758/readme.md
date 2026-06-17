## 简介
**Meetup Registration System with PostgreSQL Database & Interactive Giveaway Tool**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5758

---

# Meetup Registration System with PostgreSQL Database & Interactive Giveaway Tool


## 节点清单

| 节点 | 类型 |
|------|------|
| Thank you screen | 表单 |
| Format participant list | Code |
| Mapping form to database | 数据设置 |
| Get all participants | PostgreSQL |
| Giveaway App | Webhook |
| Respond to Giveaway App | 响应 Webhook |
| Participant Form | 表单触发器 |
| Save Participant to Database | PostgreSQL |



## 功能说明

内容管理工具，自动生成或发布内容，Webhook 触发。

Webhook触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：Webhook 触发, 表单提交触发

## 触发方式
- Giveaway App 触发
- Participant Form 触发

## 统计
- 节点总数：8
- 触发节点：2
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
