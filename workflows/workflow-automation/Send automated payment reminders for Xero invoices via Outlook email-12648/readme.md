## 简介
**Send automated payment reminders for Xero invoices via Outlook email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12648

---

# Send automated payment reminders for Xero invoices via Outlook email


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Invoice Check Trigger | 定时触发器 |
| Fetch All Xero Invoices | xero |
| Filter Out Paid Invoices | IF 判断 |
| Filter Invoices Due Soon | IF 判断 |
| Calculate Days Until Due | Code |
| Log Reminder in Xero History | HTTP Request |
| Send a message1 | Outlook |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：7
- 触发方式：定时触发

## 触发方式
- Daily Invoice Check Trigger 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
