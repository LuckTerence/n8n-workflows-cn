## 简介
**Conversational Interviews with AI Agents and n8n Forms**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2566

---

# Conversational Interviews with AI Agents and n8n Forms


## 节点清单

| 节点 | 类型 |
|------|------|
| Stop Interview? | IF 判断 |
| Generate Row | 数据设置 |
| Generate Row1 | 数据设置 |
| Clear For Next Interview | memoryManager |
| Send Reply To Agent | 数据设置 |
| Start Interview | 表单触发器 |
| Get Answer | 表单 |
| Set Interview Topic | 数据设置 |
| UUID | 加密 |
| Generate Row2 | 数据设置 |
| Create Session | Redis |
| Update Session | Redis |
| Update Session1 | Redis |
| Update Session2 | Redis |
| Valid Session? | IF 判断 |
| Respond to Webhook | 响应 Webhook |
| Window Buffer Memory2 | 记忆缓冲区 |
| Window Buffer Memory | 记忆缓冲区 |
| Redirect to Completion Screen | 表单 |
| Webhook | Webhook |
| 404 Not Found | HTML |
| AI Researcher | AI Agent |
| Parse Response | 数据设置 |
| Groq Chat Model | Groq Chat Model |
| Show Transcript | HTML |
| Save to Google Sheet | Google Sheets |
| Session to List | 数据拆分 |
| Messages To JSON | 数据设置 |
| Query By Session | Redis |
| Get Session | Redis |



## 功能说明

表单问卷工具，自动收集和处理用户反馈，Webhook 触发（Conversational)表单提交触发、Webhook 触发，通过 HTTP API 实现自动化。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：30
- 触发方式：表单提交触发, Webhook 触发

## 触发方式
- Start Interview 触发
- Webhook 触发

## 统计
- 节点总数：30
- 触发节点：2
- 处理节点：27
- 输出节点：1
- 分类：ai-agent
