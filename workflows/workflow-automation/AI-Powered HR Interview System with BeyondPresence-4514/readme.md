## 简介
**AI-Powered HR Interview System with BeyondPresence**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4514

---

# AI-Powered HR Interview System with BeyondPresence


## 节点清单

| 节点 | 类型 |
|------|------|
| 📝 Your Job Description | Code |
| ▶️ Click to Start Setup | 手动触发 |
| Prepare Interview Agent | Code |
| Create Interview Agent | beyondPresence |
| Save Agent Info | Code |
| Receive Interview Data | Webhook |
| Confirm Receipt | 响应 Webhook |
| Is Our Interview? | IF 判断 |
| Analyze Interview | OpenAI |
| Format for Sheets | Code |
| Save to Google Sheets | Google Sheets |
| Data checks | Code |
| Save to Google Sheets1 | Google Sheets |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化，Webhook 触发。

Webhook触发、手动触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：13
- 触发方式：手动触发, Webhook 触发

## 触发方式
- ▶️ Click to Start Setup 触发
- Receive Interview Data 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
