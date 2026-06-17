## 简介
**Modular & Customizable AI-Powered Email Routing: Text Classifier for eCommerce**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2851

---

# Modular & Customizable AI-Powered Email Routing: Text Classifier for eCommerce


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Text Classifier | 文本分类器 |
| OpenAI | OpenAI Chat Model |
| Prod. Dep. | Email 发送 |
| Quote Dep. | Email 发送 |
| Gen. Dep. | Email 发送 |
| Order Dep. | Email 发送 |
| Other Dep. | Email 发送 |
| Quote DB | Google Sheets |
| Prod DB | Google Sheets |
| General DB | Google Sheets |
| Order DB | Google Sheets |
| Other DB | Google Sheets |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：7
- 输出节点：5
- 分类：workflow-automation
