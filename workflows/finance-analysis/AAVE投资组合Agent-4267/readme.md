## 简介
**AAVE投资组合Agent**

Telegram+Email+GPT-4o加密投资分析

> 分类：金融分析 | 适配等级：A（需替换Notion/Google Sheets/Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/4267

---

# AAVE投资组合Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram | Telegram |
| Schedule Trigger | 定时触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| getDefiSummary | HTTP Request 工具 |
| getDefiPositionsSummary | HTTP Request 工具 |
| getDefiPositionsByProtocol | HTTP Request 工具 |
| Gmail | Gmail |
| Format Email | Code |
| AAVE Portfolio Professional AI Agent | AI Agent |
| Wallet Addresses to Monitor | Google Sheets |
| Edit Fields | 数据设置 |



## 功能说明

AAVE投资组合Agent。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：finance-analysis
