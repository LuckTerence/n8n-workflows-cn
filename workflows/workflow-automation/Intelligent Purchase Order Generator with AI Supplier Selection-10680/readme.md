## 简介
**Intelligent Purchase Order Generator with AI Supplier Selection**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10680

---

# Intelligent Purchase Order Generator with AI Supplier Selection


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Validate Request | Code |
| Prepare AI Context | 数据设置 |
| AI Supplier Selector | AI Agent |
| Enrich with Supplier Data | Code |
| Needs Approval? | IF 判断 |
| Request Approval | Email 发送 |
| Generate PO Document | Code |
| HTML to PDF | htmlcsstopdf |
| Archive in Drive | Google Drive |
| Email to Supplier | Email 发送 |
| Log in Procurement System | Code |
| Notify Procurement Team | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |



## 功能说明

电商自动化，订单处理或商品管理，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：Webhook 触发

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
