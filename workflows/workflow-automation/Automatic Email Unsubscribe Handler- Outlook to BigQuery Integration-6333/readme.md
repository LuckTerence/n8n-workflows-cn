## 简介
**Automatic Email Unsubscribe Handler: Outlook to BigQuery Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6333

---

# Automatic Email Unsubscribe Handler: Outlook to BigQuery Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Items1 | 分批处理 |
| Summarize | 文本摘要 |
| Edit Fields | 数据设置 |
| Edit Fields1 | 数据设置 |
| Run Ever 4 Hours | 定时触发器 |
| Query Bigquery for all Unsubscribes | Google BigQuery |
| Today & 7 Days Ago | Code |
| Get Emails in Past 7 Days | Outlook |
| Filter for Unsubscribes | 过滤器 |
| Keep Only New Unsubs | 数据合并 |
| Aggregate to email level | 文本摘要 |
| Add unsubscribes to Table | Google BigQuery |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 实现自动化。

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

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Run Ever 4 Hours 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
