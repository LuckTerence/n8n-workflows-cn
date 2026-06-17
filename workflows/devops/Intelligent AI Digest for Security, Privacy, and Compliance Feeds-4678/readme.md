## 简介
**Intelligent AI Digest for Security, Privacy, and Compliance Feeds**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4678

---

# Intelligent AI Digest for Security, Privacy, and Compliance Feeds


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent - Privacy Intelligence | AI Agent |
| AI Agent - Security Intelligence | AI Agent |
| AI Agent - Compliance Intelligence | AI Agent |
| Trigger Daily Digest | 定时触发器 |
| Fetch Privacy Feeds | Code |
| Fetch Compliance Feeds | Code |
| Normalize Article Security Metadata | 数据设置 |
| Normalize Article Privacy Metadata | 数据设置 |
| Normalize Article Compliance Metadata | 数据设置 |
| Filter Recent Security Articles (24h) | 过滤器 |
| Filter Recent Privacy Articles (24h) | 过滤器 |
| Filter Recent Compliance Articles (24h) | 过滤器 |
| Format Security Articles into HTML | Code |
| Format Privacy Articles into HTML | Code |
| Format Compliance Articles into HTML | Code |
| LLM - Gemini Security Summarizer | OpenAI Chat Model |
| LLM - Gemini Privacy Summarizer | OpenAI Chat Model |
| LLM - Gemini Compliance Summarizer | OpenAI Chat Model |
| Privacy Build Final Newsletter HTML | Code |
| Security Build Final Newsletter HTML | Code |
| Compliance Build Final Newsletter HTML | Code |
| Security Send Final Digest Email | Email 发送 |
| Privacy Send Final Digest Email | Email 发送 |
| Compliance Send Final Digest Email | Email 发送 |
| Sort - Security Articles by Date | 数据排序 |
| Sort - Privacy Articles by Date | 数据排序 |
| Sort - Compliance Articles by Date | 数据排序 |
| Split Out Security RSS | 数据拆分 |
| Split Out Compliance RSS | 数据拆分 |
| Security RSS Read | RSS Feed |
| Privacy RSS Read | RSS Feed |
| Compliance RSS Read | RSS Feed |
| Split Out Privacy RSS | 数据拆分 |
| Fetch Security RSS | Code |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，定时执行。

定时触发，通过 邮箱 实现自动化。

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

- 节点总数：34
- 触发方式：定时触发

## 触发方式
- Trigger Daily Digest 触发
- Security RSS Read 触发
- Privacy RSS Read 触发
- Compliance RSS Read 触发

## 统计
- 节点总数：34
- 触发节点：4
- 处理节点：27
- 输出节点：3
- 分类：devops
