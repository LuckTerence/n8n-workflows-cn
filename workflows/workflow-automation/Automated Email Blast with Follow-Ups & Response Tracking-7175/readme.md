## 简介
**Automated Email Blast with Follow-Ups & Response Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7175

---

# Automated Email Blast with Follow-Ups & Response Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Trigger | 定时触发器 |
| Fetch Contact Data | Google Sheets |
| Iterate Contacts | 分批处理 |
| Determine Follow-Up Stage | IF 判断 |
| Route by Follow-Up Stage | Switch 路由 |
| Send Follow-Up Email 1 | Email 发送 |
| Send Follow-Up Email 2 | Email 发送 |
| Update Sheet with Follow-Up Status | Google Sheets |
| Check Email Responses | Email 读取 |
| Update Sheet with Response | Google Sheets |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- Daily Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
