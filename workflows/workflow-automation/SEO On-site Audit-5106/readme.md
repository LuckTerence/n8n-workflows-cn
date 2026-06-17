## 简介
**SEO On-site Audit**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5106

---

# SEO On-site Audit


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| HTTP Request - Get Page | HTTP Request |
| HTML Extract | htmlExtract |
| PageSpeed API | HTTP Request |
| Send Email | Email 发送 |
| Generate HTML REPORT | HTML |
| FUnctions to report | Code |
| Check Image | Code |
| Links | Code |
| DeepSeek Chat Model | lmChatDeepSeek |
| Title Analysis | LLM Chain |
| Description Analysis | LLM Chain |
| Title | Code |
| Description | Code |
| Alts Analysis | LLM Chain |
| Density Analysis | LLM Chain |
| Keyword Density | Code |
| Content Analysis | LLM Chain |
| Domain | Code |
| Robots.txt | HTTP Request |
| Code Analysis | Code |
| Sitemap | HTTP Request |
| Robots Analysis | Code |
| Code | Code |
| Merge | 数据合并 |



## 功能说明

SEO 优化工具，关键词分析和内容优化，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：19
- 输出节点：5
- 分类：workflow-automation
