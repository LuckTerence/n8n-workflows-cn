## 简介
**Benchmark Content Safety Guardrails with Automated Test Suite & Reports**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10729

---

# Benchmark Content Safety Guardrails with Automated Test Suite & Reports


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| OpenAI Chat Model | OpenAI Chat Model |
| Check Guardrails | guardrails |
| Format Pass Result | Code |
| Format Fail Result | Code |
| Combine Result | 数据合并 |
| Calculate Metrics | Code |
| Format Report | Code |
| Preserve Original Data | Code |
| Send a message | Email 发送 |
| Set Test Data (code) | Code |
| Markdown | Markdown |



## 功能说明

内容管理工具，自动生成或发布内容。

手动触发，通过 邮箱 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：workflow-automation
