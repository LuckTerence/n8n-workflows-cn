## 简介
**Batch verify emails in Google Sheet with Icypeas**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2016

---

# Batch verify emails in Google Sheet with Icypeas


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Authenticates to your Icypeas account | Code |
| Reads lastname,firstname and company from your sheet | Google Sheets |
| Run bulk search (email-verif) | HTTP Request |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：4
- 触发方式：手动触发

## 触发方式
- When clicking "Execute Workflow" 触发

## 统计
- 节点总数：4
- 触发节点：1
- 处理节点：2
- 输出节点：1
- 分类：workflow-automation
