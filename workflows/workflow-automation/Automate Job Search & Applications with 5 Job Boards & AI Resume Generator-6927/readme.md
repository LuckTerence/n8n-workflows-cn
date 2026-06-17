## 简介
**Automate Job Search & Applications with 5 Job Boards & AI Resume Generator**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6927

---

# Automate Job Search & Applications with 5 Job Boards & AI Resume Generator


## 节点清单

| 节点 | 类型 |
|------|------|
| 4️⃣Get Jobs from Adzuna | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Filter Duplicates | Code |
| Webhook | Webhook |
| 📈 IF Score ≥ 3 | IF 判断 |
| 🔥Write Cover Letter | AI Agent |
| Upate sheets | Google Sheets |
| 📧Gmail | Email 发送 |
| Extract from File | 从文件提取 |
| Check Send Email Success | IF 判断 |
| Apify: Run Indeed Scraper | apify |
| Apify: Get Indeed Results | apify |
| Apify: Run LinkedIn Scraper | apify |
| Apify: Run Upwork Scraper | apify |
| Apify: Run Glassdoor Scraper | apify |
| Apify: Get Upwork Results | apify |
| Apify: Get Glassdoor Results | apify |
| Merge | 数据合并 |
| Standardize Job Data | 数据设置 |
| Filter | 过滤器 |
| Apify: Get LinkedIn Results | apify |
| Extract Skills from Job Description | AI Agent |
| Resume Match Score | AI Agent |
| Rewrite Resume | AI Agent |
| Itemize List | 数据拆分 |
| Respond to Webhook | 响应 Webhook |
| Loop Over Items | 分批处理 |
| Send a message if process failed | Email 发送 |
| Set Job Title | 数据设置 |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化，Webhook 触发。

Webhook触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：29
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：24
- 输出节点：4
- 分类：workflow-automation
