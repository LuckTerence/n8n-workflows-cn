## 简介
**Monetize Your Private LLM Models with x402 & Ollama**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6597

---

# Monetize Your Private LLM Models with x402 & Ollama


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Check for presence of X-HEADER | IF 判断 |
| Decode & Validate X-Payment | Code |
| Simulate Payment | 一次性执行 |
| On Successful Payment Simulation | IF 判断 |
| 1Shot API Submit & Wait | 一次性同步 |
| Ensure Well Formatted Payment Payload | IF 判断 |
| Response: Missing or Invalid Payment Headers | 响应 Webhook |
| Response: Payment Invalid | 响应 Webhook |
| Response: 200 - Payment Successful | 响应 Webhook |
| Private Model Inference | LLM Chain |
| Ollama Engine | lmOllama |



## 功能说明

Monetize Your Private LLM Models with x402 & Ollam（AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
