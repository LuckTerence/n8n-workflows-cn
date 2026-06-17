## 简介
**Automatic Subscriber Creation in Beehiiv from Systeme.io Funnel Optins**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5992

---

# Automatic Subscriber Creation in Beehiiv from Systeme.io Funnel Optins


## 节点清单

| 节点 | 类型 |
|------|------|
| Clean Data | 数据设置 |
| Create New Beehiiv Subscriber | HTTP Request |
| Subscriber Created? | IF 判断 |
| Send Email Alert (Beehiiv API error) | Email 发送 |
| Configure Workflow | 数据设置 |
| On New Systeme.io Optin | Webhook |



## 功能说明

Automatic Subscriber Creation in Beehiiv from Syst。

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

- 节点总数：6
- 触发方式：Webhook 触发

## 触发方式
- On New Systeme.io Optin 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
