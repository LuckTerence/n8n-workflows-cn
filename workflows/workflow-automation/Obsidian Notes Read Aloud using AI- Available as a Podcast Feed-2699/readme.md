## 简介
**Obsidian Notes Read Aloud using AI: Available as a Podcast Feed**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2699

---

# Obsidian Notes Read Aloud using AI: Available as a Podcast Feed


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI1 | OpenAI |
| Webhook GET Note | Webhook |
| Webhook GET Podcast Feed | Webhook |
| Upload Audio to Cloudinary | HTTP Request |
| OpenAI | OpenAI |
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| Give Audio Unique Name | 数据设置 |
| Send Audio to Obsidian | 响应 Webhook |
| Rename Fields | 数据设置 |
| Append Item to Google Sheet | Google Sheets |
| Get Items from Google Sheets | Google Sheets |
| Write RSS Feed | Code |
| Return Podcast Feed to Webhook | 响应 Webhook |
| Manually Enter Other Data for Podcast Feed | 数据设置 |



## 功能说明

Obsidian Notes Read Aloud using AI- Available as a（AI 增强)Webhook 触发，通过 在线表格 + HTTP API 实现自动化。

Webhook触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：Webhook 触发

## 触发方式
- Webhook GET Note 触发
- Webhook GET Podcast Feed 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
