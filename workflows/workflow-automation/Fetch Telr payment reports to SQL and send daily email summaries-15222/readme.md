## 简介
**Fetch Telr payment reports to SQL and send daily email summaries**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15222

---

# Fetch Telr payment reports to SQL and send daily email summaries


## 节点清单

| 节点 | 类型 |
|------|------|
| Edit Fields | 数据设置 |
| Compression | compression |
| Extract from File | 从文件提取 |
| Code in JavaScript3 | Code |
| Schedule Trigger | 定时触发器 |
| Send email | Email 发送 |
| TELR API | HTTP Request |
| Convert XML to JSON | XML |
| Logic for date | Code |
| TELR API WITH DATE | HTTP Request |
| Data Formation | Code |
| Data Insert SQL | microsoftSql |
| Success Condition | IF 判断 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
