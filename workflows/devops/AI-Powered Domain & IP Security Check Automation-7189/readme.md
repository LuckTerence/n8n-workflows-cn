## 简介
**AI-Powered Domain & IP Security Check Automation**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7189

---

# AI-Powered Domain & IP Security Check Automation


## 节点清单

| 节点 | 类型 |
|------|------|
| Request an domain rescan | HTTP Request |
| Get a domain report | HTTP Request |
| Get a URL / file analysis | HTTP Request |
| Domain-IP resolutions | HTTP Request |
| Resolution | HTTP Request |
| Code | Code |
| AI Agent | AI Agent |
| IF Checking Domain Found Or Not Found | IF 判断 |
| Malicious Hostname | IF 判断 |
| check SPF | HTTP Request |
| check DMARC | HTTP Request |
| check DKIM | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Simple Memory1 | 记忆缓冲区 |
| HTTP Request | HTTP Request |
| check SPF1 | HTTP Request |
| check DMARC1 | HTTP Request |
| check DKIM1 | HTTP Request |
| Malicious IP | IF 判断 |
| AI Agent1 | AI Agent |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Simple Memory | 记忆缓冲区 |
| Safe | IF 判断 |
| check SPF2 | HTTP Request |
| check DMARC2 | HTTP Request |
| check DKIM2 | HTTP Request |
| AI Agent2 | AI Agent |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Simple Memory2 | 记忆缓冲区 |
| Google Sheets | Google Sheets |
| Google Sheets1 | Google Sheets |
| Google Sheets2 | Google Sheets |
| Google Sheets3 | Google Sheets |
| Google Sheets4 | Google Sheets |
| Google Sheets5 | Google Sheets |
| Google Sheets6 | Google Sheets |
| Google Sheets7 | Google Sheets |
| Google Sheets8 | Google Sheets |
| Schedule Trigger1 | 定时触发器 |
| Google Sheets10 | Google Sheets |
| Google Sheets9 | Google Sheets |
| Google Sheets11 | Google Sheets |
| Google Sheets12 | Google Sheets |



## 功能说明

AI-Powered Domain & IP Security Check Automation（AI 增强)定时触发，通过 在线表格 + HTTP API 实现自动化。

定时触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：43
- 触发方式：定时触发

## 触发方式
- Schedule Trigger1 触发

## 统计
- 节点总数：43
- 触发节点：1
- 处理节点：27
- 输出节点：15
- 分类：devops
