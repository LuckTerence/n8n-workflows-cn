## 简介
**Influencer Brand Safety Auditor with Engagement Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11808

---

# Influencer Brand Safety Auditor with Engagement Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Influencer Audit Form | 表单触发器 |
| Workflow Configuration | 数据设置 |
| Store Audit Request | Google Sheets |
| Apify Instagram Scraper | HTTP Request |
| Calculate Engagement Rate | Code |
| Aggregate Captions | 数据聚合 |
| AI Content Safety Audit | OpenAI |
| Send Audit Report to Slack | Slack |
| Store Audit Results | Google Sheets |



## 功能说明

Influencer Brand Safety Auditor with Engagement An（AI 增强)表单提交触发，通过 Slack + HTTP API 实现自动化。

，通过 Slack + HTTP API 实现自动化。

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

- 节点总数：9
- 触发方式：表单提交触发

## 触发方式
- Influencer Audit Form 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
