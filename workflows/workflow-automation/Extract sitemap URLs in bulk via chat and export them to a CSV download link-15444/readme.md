## 简介
**Extract sitemap URLs in bulk via chat and export them to a CSV download link**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15444

---

# Extract sitemap URLs in bulk via chat and export them to a CSV download link


## 节点清单

| 节点 | 类型 |
|------|------|
| Listen for Bulk URLs | Chat 触发器 |
| Fetch XML Data | HTTP Request |
| Parse & Validate URLs | Code |
| Check for Validation Errors | IF 判断 |
| Alert User: Invalid URLs | 聊天 |
| Cache Validated URLs | Code |
| Format Successful Data | Code |
| Aggregate Successful Data | 数据聚合 |
| Delay Chat Sequence | 等待 |
| Alert User: Accessible URLs | 聊天 |
| Isolate Failed URLs | 数据拆分 |
| Aggregate Failed URLs | 数据聚合 |
| Alert User: Failed URLs | 聊天 |
| Process Each Sitemap | 分批处理 |
| Parse XML Data | XML |
| Scan for Sitemap Indexes | Code |
| Check if Nested Index | IF 判断 |
| Alert User: Nested Index Found | 聊天 |
| Isolate Individual URLs | 数据拆分 |
| Standardize URL Data | 数据设置 |
| Generate CSV File | 转换为文件 |
| Upload CSV to Host | HTTP Request |
| Extract Download URL | Code |
| Send Download Link | 聊天 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

Chat 消息触发，通过 HTTP API 实现自动化。

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
- 触发方式：Chat 消息触发

## 触发方式
- Listen for Bulk URLs 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：16
- 输出节点：7
- 分类：workflow-automation
