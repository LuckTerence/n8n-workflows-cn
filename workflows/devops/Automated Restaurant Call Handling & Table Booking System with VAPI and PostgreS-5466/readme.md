## 简介
**Automated Restaurant Call Handling & Table Booking System with VAPI and PostgreSQL**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5466

---

# Automated Restaurant Call Handling & Table Booking System with VAPI and PostgreSQL


## 节点清单

| 节点 | 类型 |
|------|------|
| Query Table Availability (Postgres) | PostgreSQL |
| Respond: Availability Status (VAPI) | 响应 Webhook |
| Trigger: Booking Request (VAPI)	 | Webhook |
| Upsert Booking in Postgres	 | PostgreSQL |
| Respond: Booking Confirmation (VAPI)	 | 响应 Webhook |
| Trigger: Booking Request (VAPI)	1 | Webhook |



## 功能说明

日历日程管理，自动创建事件或发送提醒，Webhook 触发。

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

- 节点总数：6
- 触发方式：Webhook 触发

## 触发方式
- Trigger: Booking Request (VAPI)	 触发
- Trigger: Booking Request (VAPI)	1 触发

## 统计
- 节点总数：6
- 触发节点：2
- 处理节点：2
- 输出节点：2
- 分类：devops
