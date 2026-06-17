## 简介
**Daylight Saving Time Notification For Different Timezones**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3276

---

# Daylight Saving Time Notification For Different Timezones


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Timezones List | Code |
| Calculate Zone Date and Time | 数据设置 |
| Check If Daylight Saving Time | 数据设置 |
| Check If Change Tomorrow | IF 判断 |
| Send Notification On Upcoming Change | Slack |
| Calculate Tomorrow's Date | 日期时间 |
| Schedule Trigger | 定时触发器 |
| Send Email On Upcoming Change | Email 发送 |



## 功能说明

通知推送系统，多渠道消息分发，定时执行。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
