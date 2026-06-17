## 简介
**Intelligent Legal Document Review and Compliance Automation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11861

---

# Intelligent Legal Document Review and Compliance Automation


## 节点清单

| 节点 | 类型 |
|------|------|
| Document Upload Webhook | Webhook |
| Workflow Configuration | 数据设置 |
| Extract Document Text | 从文件提取 |
| Clause Analysis Agent | AI Agent |
| OpenAI Model - Clause Analysis | OpenAI Chat Model |
| Clause Analysis Output Parser | 结构化输出解析器 |
| Compliance Check Agent | AI Agent |
| OpenAI Model - Compliance | OpenAI Chat Model |
| Compliance Output Parser | 结构化输出解析器 |
| Alternative Wording Agent | AI Agent |
| OpenAI Model - Alternative Wording | OpenAI Chat Model |
| Alternative Wording Output Parser | 结构化输出解析器 |
| Summary Report Generator | AI Agent |
| OpenAI Model - Summary | OpenAI Chat Model |
| Prepare Database Record | 数据设置 |
| Log to Contract Database | PostgreSQL |
| Send Notification | HTTP Request |



## 功能说明

Intelligent Legal Document Review and Compliance A（AI 增强)Webhook 触发，通过 数据库 + HTTP API 实现自动化。

Webhook触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：17
- 触发方式：Webhook 触发

## 触发方式
- Document Upload Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：15
- 输出节点：1
- 分类：workflow-automation
