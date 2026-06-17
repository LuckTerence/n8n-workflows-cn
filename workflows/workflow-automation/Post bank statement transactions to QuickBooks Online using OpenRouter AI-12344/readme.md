## 简介
**Post bank statement transactions to QuickBooks Online using OpenRouter AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12344

---

# Post bank statement transactions to QuickBooks Online using OpenRouter AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract PDF Text | 从文件提取 |
| Transaction Extractor AI | AI Agent |
| JSON Output Parser | 结构化输出解析器 |
| Create QuickBooks SalesReceipt | HTTP Request |
| Bank Statement Form | 表单触发器 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Split Transactions | 数据拆分 |
| Loop Over Items | 分批处理 |
| Build Salesreceipt Payload | Code |
| Get many customers | QuickBooks |
| Create Vendor | QuickBooks |
| Vendor Exists? | IF 判断 |
| Find Vendor | QuickBooks |
| Search Categories | HTTP Request |
| Create Items | HTTP Request |
| Collect All Item Mappings | Code |
| Need to Create Items? | IF 判断 |
| Get All QB Items | QuickBooks |
| Check Which Items to Create | Code |
| Credit or Debit? | Switch 路由 |
| Customers Exists?1 | IF 判断 |
| Create a Customer | QuickBooks |
| Create QuickBooks Expense | HTTP Request |
| Build Expense Payload | Code |



## 功能说明

内容管理工具，自动生成或发布内容（Bank)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：表单提交触发

## 触发方式
- Bank Statement Form 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：19
- 输出节点：4
- 分类：workflow-automation
