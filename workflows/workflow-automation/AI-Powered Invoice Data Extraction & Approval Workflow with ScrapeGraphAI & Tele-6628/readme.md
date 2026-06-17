## 简介
**AI-Powered Invoice Data Extraction & Approval Workflow with ScrapeGraphAI & Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6628

---

# AI-Powered Invoice Data Extraction & Approval Workflow with ScrapeGraphAI & Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger | Email 读取 |
| File Upload Webhook | Webhook |
| File Processor | Code |
| ScrapeGraphAI - Invoice Extractor | ScrapeGraph AI |
| Data Extractor & Cleaner | Code |
| Validation Rules Engine | Code |
| Approval Required? | Switch 路由 |
| Approval Workflow Generator | Code |
| Approval Notification | Telegram |
| Accounting System Integration | HTTP Request |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：Webhook 触发

## 触发方式
- File Upload Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
