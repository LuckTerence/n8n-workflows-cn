## 简介
**Extract University Term Dates from Excel using CloudFlare Markdown Conversion**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3505

---

# Extract University Term Dates from Excel using CloudFlare Markdown Conversion


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Get Term Dates Excel | HTTP Request |
| Extract Key Events and Dates | 信息提取器 |
| Extract Target Sheet | 数据设置 |
| Fix Dates | 数据设置 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Create ICS File | 转换为文件 |
| Events to ICS Document | Code |
| Sort Events by Date | 数据排序 |
| Markdown Conversion Service | HTTP Request |
| Events to Items | 数据拆分 |
| Send Email with Attachment | Email 发送 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
