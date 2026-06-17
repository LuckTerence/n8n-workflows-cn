## 简介
**弃购挽回分析**

Gmail+Sheets的弃购挽回分析

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（AI模型已适配，部分外服节点需手动替换为国内服务）
> 原始来源：https://n8nworkflows.xyz/workflows/6045

---

# 弃购挽回分析


## 节点清单

| 节点 | 类型 |
|------|------|
| Cart Abandoned Webhook | Webhook |
| Recovery Settings | 数据设置 |
| Qualify Cart | IF 判断 |
| Generate Recovery Data | Code |
| Wait 1 Hour | 等待 |
| Send First Recovery Email | Gmail |
| Wait 23 Hours More | 等待 |
| Send Second Recovery Email | Gmail |
| Wait 48 Hours More | 等待 |
| Send Final Recovery Email | Gmail |
| Track Recovery Start | Google Sheets |



## 功能说明

弃购挽回分析。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

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
- Cart Abandoned Webhook 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
