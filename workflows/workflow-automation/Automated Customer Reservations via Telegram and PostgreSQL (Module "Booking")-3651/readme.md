## 简介
**Automated Customer Reservations via Telegram and PostgreSQL (Module "Booking")**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3651

---

# Automated Customer Reservations via Telegram and PostgreSQL (Module "Booking")


## 节点清单

| 节点 | 类型 |
|------|------|
| Update Name | PostgreSQL |
| Update Hour | PostgreSQL |
| Get Work Hours | PostgreSQL |
| Get Work Days | PostgreSQL |
| Update bot status on START | PostgreSQL |
| Is Date correct? | IF 判断 |
| Commands | Switch 路由 |
| Starts | WhatsApp |
| Get Bot Status | PostgreSQL |
| Upsert Bot Status on START | PostgreSQL |
| WhatsApp Trigger | whatsAppTrigger |
| Define Flow | Switch 路由 |
| Initialization | 数据设置 |
| Get book | PostgreSQL |
| Main Menu | WhatsApp |
| Request Date | WhatsApp |
| Union Number with Question | 数据设置 |
| Union list | 文本摘要 |
| Update bot status on BOOKING | PostgreSQL |
| First Question? | IF 判断 |
| Get Work Days | PostgreSQL |
| Add Book | PostgreSQL |
| Merge1 | 数据合并 |
| Union Number with Question1 | 数据设置 |
| Union list1 | 文本摘要 |
| Merge | 数据合并 |
| Edit Fields | 数据设置 |
| Switch | Switch 路由 |
| Update Date AND Status | PostgreSQL |
| Phone validation1 | IF 判断 |
| Request Phone | WhatsApp |
| Request Name | WhatsApp |
| Phone Error | WhatsApp |
| page booking success | WhatsApp |
| Update status on BOOKED | PostgreSQL |
| Update Phone | PostgreSQL |
| Payments | WhatsApp |
| Update bot status on PAYMENTS | PostgreSQL |
| Request Time | WhatsApp |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：39
- 触发方式：手动或子流程调用

## 触发方式
- WhatsApp Trigger 触发

## 统计
- 节点总数：39
- 触发节点：1
- 处理节点：29
- 输出节点：9
- 分类：workflow-automation
