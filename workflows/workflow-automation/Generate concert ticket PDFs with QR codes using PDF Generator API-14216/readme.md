## 简介
**Generate concert ticket PDFs with QR codes using PDF Generator API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14216

---

# Generate concert ticket PDFs with QR codes using PDF Generator API


## 节点清单

| 节点 | 类型 |
|------|------|
| Concert Ticket Form | 表单触发器 |
| Prepare Ticket Data | Code |
| Generate Concert Ticket PDF | pdfGeneratorApi |
| Build Confirmation Email | Code |
| Send Ticket to Attendee | Email 发送 |
| Log Ticket Sale | Google Sheets |
| Notify Event Organizer | Slack |



## 功能说明

PDF 文档处理，解析或生成 PDF 文件（Concert)表单提交触发，通过 邮箱 + 在线表格 + Slack + HTTP API 实现自动化。

，通过 邮箱 + 在线表格 + Slack + HTTP API 实现自动化。

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

- 节点总数：7
- 触发方式：表单提交触发

## 触发方式
- Concert Ticket Form 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
