## 简介
**Report spam and phishing URLs from IMAP mailboxes to Spamhaus**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12846

---

# Report spam and phishing URLs from IMAP mailboxes to Spamhaus


## 节点清单

| 节点 | 类型 |
|------|------|
| Phishing Trigger | Email 读取 |
| Spam Trigger | Email 读取 |
| initial config spam | 数据设置 |
| extract all URLs | Code |
| create item for spamhaus | 数据设置 |
| Spamhaus submit url | HTTP Request |
| Loop over each email | 分批处理 |
| initial phish config | 数据设置 |
| aggregate all into a single list | 数据聚合 |
| add run specific job | 空操作 |
| add email specific job | 空操作 |
| de-duplicate URLs | 去重 |
| split URLs to array | 数据拆分 |
| filter out URLs that match regexes | 过滤器 |



## 功能说明

邮件自动化处理，AI 分类整理或。

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

- 节点总数：14
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：14
- 触发节点：0
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
