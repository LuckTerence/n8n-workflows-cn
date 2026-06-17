## 简介
**Automate social media content planning with Llama 3.3 AI, trending topics & Google Suite**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11880

---

# Automate social media content planning with Llama 3.3 AI, trending topics & Google Suite


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily 8 AM Trigger1 | 定时触发器 |
| Workflow Configuration1 | 数据设置 |
| Fetch News RSS1 | RSS Feed |
| Fetch Reddit Popular1 | reddit |
| Merge Trends1 | 数据合并 |
| Format Trending Topics1 | Code |
| Read Active Campaigns1 | Google Sheets |
| Check Campaign Status1 | IF 判断 |
| Enrich with Trends1 | 数据设置 |
| Groq Chat Model1 | Groq Chat Model |
| Generate Content Ideas1 | AI Agent |
| Structured Output Parser1 | 结构化输出解析器 |
| Format for Sheets1 | 数据设置 |
| Append to Daily Content Plan1 | Google Sheets |
| Format for Calendar1 | 数据设置 |
| Create Calendar Event1 | Google Calendar |
| Calculate Performance Metrics1 | Code |
| Aggregate Daily Summary1 | 数据聚合 |
| Format Email Content1 | 数据设置 |
| Send Gmail Summary1 | Email 发送 |



## 功能说明

社交媒体管理，多平台内容发布和监听，定时执行。

定时触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：20
- 触发方式：定时触发

## 触发方式
- Daily 8 AM Trigger1 触发
- Fetch News RSS1 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：17
- 输出节点：1
- 分类：workflow-automation
