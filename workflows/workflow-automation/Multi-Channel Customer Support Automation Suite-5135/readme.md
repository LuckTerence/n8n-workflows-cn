## 简介
**Multi-Channel Customer Support Automation Suite**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5135

---

# Multi-Channel Customer Support Automation Suite


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger | Email 读取 |
| Web Form Webhook | Webhook |
| Normalize Messages | Function |
| Categorize & Prioritize | Function |
| Check Auto-Response | IF 判断 |
| Generate Auto-Response | Function |
| Send Auto-Response | Email 发送 |
| Notify Slack | Slack |
| Store in CRM | Function |
| Log Success | Function |
| Error Handler | Function |
| Merge | 数据合并 |
| Notify Error to Slack | HTTP Request |
| Webhook Response | 响应 Webhook |



## 功能说明

Multi-Channel Customer Support Automation Suite。

Webhook触发，通过 邮箱 + Slack + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：Webhook 触发

## 触发方式
- Web Form Webhook 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：8
- 输出节点：5
- 分类：workflow-automation
