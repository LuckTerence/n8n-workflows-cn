## 简介
**Flexible Currency Rate Uploads for SAP B1 with AI Validation & Multiple Sources**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4931

---

# Flexible Currency Rate Uploads for SAP B1 with AI Validation & Multiple Sources


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Switch | Switch 路由 |
| Enviar SAP (JSON) | HTTP Request |
| Conectar SAP | HTTP Request |
| Microsoft SQL | microsoftSql |
| Extraer Query | 数据设置 |
| Enviar SAP (SQL) | HTTP Request |
| Limit | 数据限制 |
| Enviar SAP (MANUAL) | HTTP Request |
| OpenAI | OpenAI |
| Split Out | 数据拆分 |
| Google Sheets | Google Sheets |
| Enviar SAP (SHEET) | HTTP Request |
| Success | Google Sheets |
| Fallo | Google Sheets |
| Success1 | Google Sheets |
| Comprobar Fecha | OpenAI |
| Fallo1 | Google Sheets |
| Success2 | Google Sheets |
| Fallo2 | Google Sheets |
| Success3 | Google Sheets |
| Fallo3 | Google Sheets |



## 功能说明

文件处理工具，自动转换或管理文件，Webhook 触发。

Webhook触发，通过 在线表格 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：16
- 输出节点：5
- 分类：workflow-automation
