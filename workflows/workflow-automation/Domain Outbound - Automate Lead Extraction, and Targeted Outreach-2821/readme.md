## 简介
**Domain Outbound : Automate Lead Extraction, and Targeted Outreach**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2821

---

# Domain Outbound : Automate Lead Extraction, and Targeted Outreach


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Sheets | Google Sheets |
| Remove Duplicates | 去重 |
| Remove Duplicates2 | 去重 |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| Loop Over Items | 分批处理 |
| HTTP Request1 | HTTP Request |
| Loop Over Items1 | 分批处理 |
| Wait1 | 等待 |
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items4 | 分批处理 |
| get website with Jina.ai | HTTP Request |
| If1 | IF 判断 |
| Gmail1 | Email 发送 |
| Generate Email content | OpenAI |
| Wait2 | 等待 |
| Code6 | Code |
| Generate queries | OpenAI |
| fomate queries | Code |
| Loop Over queries | 分批处理 |
| Gmail search | HTTP Request |
| Extract Urls | Code |
| Filter urls | 过滤器 |
| If url is not empty | IF 判断 |
| Extract Domain Name | Code |
| Extract Emails | Code |
| Limit Markdown | Code |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：27
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：22
- 输出节点：4
- 分类：workflow-automation
