## 简介
**E-commerce Price Tracker with ScrapeGraphAI, MongoDB, and Mailgun Alerts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11585

---

# E-commerce Price Tracker with ScrapeGraphAI, MongoDB, and Mailgun Alerts


## 节点清单

| 节点 | 类型 |
|------|------|
| Incoming Monitor Request | Webhook |
| Define Product Sources | Code |
| Split URLs | 分批处理 |
| Scrape Product Page | ScrapeGraph AI |
| Combine Scraped Data | 数据合并 |
| Analyze Price Movement | Code |
| Store to MongoDB | MongoDB |
| Significant Price Change? | IF 判断 |
| Prepare Alert Email | 数据设置 |
| Send Mailgun Alert | mailgun |
| Send Webhook Response | 响应 Webhook |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- Incoming Monitor Request 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
