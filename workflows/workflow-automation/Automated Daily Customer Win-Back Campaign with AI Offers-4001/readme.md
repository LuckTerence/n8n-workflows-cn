## 简介
**Automated Daily Customer Win-Back Campaign with AI Offers**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4001

---

# Automated Daily Customer Win-Back Campaign with AI Offers


## 节点清单

| 节点 | 类型 |
|------|------|
| Scheduled Start: Daily Churn Check | 定时触发器 |
| Fetch Customer Data from Sheet | Google Sheets |
| Filter High Churn Risk & No Campaign Customers | 过滤器 |
| Check if Eligible Customers Found | IF 判断 |
| Process Each Eligible Customer | 分批处理 |
| Generate Win-Back Offer | LLM Chain |
| (LLM Model for Offer Generation) | OpenAI Chat Model |
| (Parse Offer JSON) | 结构化输出解析器 |
| Log Sent Offer in System Log | Google Sheets |
| Send Win-Back Offer via Email | Email 发送 |
| Set 'Not Found' Status | 数据设置 |
| Log 'Not Found' in System Log | Google Sheets |



## 功能说明

Automated Daily Customer Win-Back Campaign with AI（AI 增强)定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Scheduled Start: Daily Churn Check 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
