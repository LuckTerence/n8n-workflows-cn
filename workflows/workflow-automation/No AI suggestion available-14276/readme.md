## 简介
**No AI suggestion available**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14276

---

# No AI suggestion available


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Receive Financial Data | Webhook |
| Workflow Configuration | 数据设置 |
| Check Data Source Type | IF 判断 |
| Extract CSV Data | 从文件提取 |
| Normalize Bank Statement Schema | 数据设置 |
| Normalize Invoice Schema | 数据设置 |
| Normalize ERP Schema | 数据设置 |
| Normalize CSV Schema | 数据设置 |
| Merge All Normalized Data | 数据合并 |
| Deterministic Matching Logic | Code |
| Check Match Quality | IF 判断 |
| AI Fuzzy Matching Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Merge Matched Results | 数据合并 |
| Calculate Confidence Scores | Code |
| Route by Confidence Threshold | IF 判断 |
| Flag for Human Review | 数据设置 |
| Mark as Auto-Reconciled | 数据设置 |
| Merge All Results | 数据合并 |
| Log to Reconciliation Report | Google Sheets |
| Notify Finance Team | Slack |
| Merge All Normalized Data1 | 数据合并 |
| Merge All Normalized Data2 | 数据合并 |



## 功能说明

No AI suggestion available（AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：Webhook 触发

## 触发方式
- Webhook - Receive Financial Data 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：22
- 输出节点：1
- 分类：workflow-automation
