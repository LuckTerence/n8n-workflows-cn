## 简介
**Automated Press Pass Verification & Badge Creation with QR Codes & Multi-Channel Distribution**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10793

---

# Automated Press Pass Verification & Badge Creation with QR Codes & Multi-Channel Distribution


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Validate Required Fields | IF 判断 |
| Stop: Incomplete Data | 停止并报错 |
| Check Domain Verified | IF 判断 |
| Stop: Domain Not Verified | 停止并报错 |
| Generate Press ID & QR | Code |
| Send Press Pass Email | Email 发送 |
| Notify Organizers (Slack) | Slack |
| Log to Google Sheets | Google Sheets |
| Respond to Webhook | 响应 Webhook |
| Verifi Email | verifiEmail |
| HTML/CSS to Image | htmlCssToImage |



## 功能说明

AI 代码助手，代码生成或审查，Webhook 触发。

Webhook触发，通过 邮箱 + 在线表格 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
