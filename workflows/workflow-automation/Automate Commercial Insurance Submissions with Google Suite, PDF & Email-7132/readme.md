## 简介
**Automate Commercial Insurance Submissions with Google Suite, PDF & Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7132

---

# Automate Commercial Insurance Submissions with Google Suite, PDF & Email


## 节点清单

| 节点 | 类型 |
|------|------|
| Check for Applications | IF 判断 |
| Process Each Application | 分批处理 |
| Select Suitable Carriers | Code |
| Process Each Carrier | 分批处理 |
| Generate Application PDF | Code |
| Email to Carrier | Email 发送 |
| Track Submission | Code |
| Update row in sheet | Google Sheets |
| Create Process Summary | Code |
| Notify Broker | Email 发送 |
| When clicking 'Execute workflow' | 手动触发 |
| Get row(s) in sheet | Google Sheets |
| Update a document | Google Docs |
| Download file | Google Drive |
| Wait | 等待 |
| Copy file | Google Drive |
| If | IF 判断 |
| No Operation | 空操作 |
| If1 | IF 判断 |
| Merge | 数据合并 |
| Pre-process & Consolidate Data | Code |
| Set Test Emails | 数据设置 |
| Generate Carrier Code | Code |
| Edit Fields (Output) | 数据设置 |
| Generate Carrier Code (Production) | Code |
| Edit Fields (Output)1 | 数据设置 |
| Set Carriers | 数据设置 |
| Generate Carrier Selection Code | Code |
| Edit Fields (Output)2 | 数据设置 |



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

- 节点总数：29
- 触发方式：手动触发

## 触发方式
- When clicking 'Execute workflow' 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：26
- 输出节点：2
- 分类：workflow-automation
