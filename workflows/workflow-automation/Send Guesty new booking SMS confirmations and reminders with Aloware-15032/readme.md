## 简介
**Send Guesty new booking SMS confirmations and reminders with Aloware**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15032

---

# Send Guesty new booking SMS confirmations and reminders with Aloware


## 节点清单

| 节点 | 类型 |
|------|------|
| Guesty: New Reservation | Webhook |
| Normalize Reservation Data | 数据设置 |
| Aloware: Create Guest Contact | HTTP Request |
| Aloware: Send Booking Confirmation SMS | HTTP Request |
| Aloware: Enroll in Check-in Reminder Sequence | HTTP Request |
| Wait Until After Checkout | 等待 |
| Aloware: Enroll in Post-Stay Review Sequence | HTTP Request |



## 功能说明

日历日程管理，自动创建事件或发送提醒，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：Webhook 触发

## 触发方式
- Guesty: New Reservation 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：workflow-automation
