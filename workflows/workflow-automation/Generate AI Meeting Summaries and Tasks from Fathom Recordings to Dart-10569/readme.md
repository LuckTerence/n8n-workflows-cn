## 简介
**Generate AI Meeting Summaries and Tasks from Fathom Recordings to Dart**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10569

---

# Generate AI Meeting Summaries and Tasks from Fathom Recordings to Dart


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Retrieve an existing folder | dart |
| Create a new doc | dart |
| Code in JavaScript | Code |
| Create a new task | dart |
| Retrieve an existing dartboard | dart |
| Retrieve an existing doc | dart |



## 功能说明

AI 内容摘要工具，自动提炼长文关键信息，Webhook 触发。

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

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
