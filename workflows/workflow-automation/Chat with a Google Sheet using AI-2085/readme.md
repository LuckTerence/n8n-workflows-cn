## 简介
**Chat with a Google Sheet using AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2085

---

# Chat with a Google Sheet using AI


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| When Executed by Another Workflow | 执行工作流触发器 |
| AI Agent | AI Agent |
| List columns tool | 工作流工具 |
| Get column values tool | 工作流工具 |
| Get customer tool | 工作流工具 |
| Set Google Sheet URL | 数据设置 |
| Get Google sheet contents | Google Sheets |
| Check operation | Switch 路由 |
| Get column names | 数据设置 |
| Prepare column data | 数据设置 |
| Filter | 过滤器 |
| Prepare output | Code |



## 功能说明

Chat with a Google Sheet using AI（AI 增强)Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
