## 简介
**Connect AI Agents to Beanstream Payments API for Payment Processing & Management**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5538

---

# Connect AI Agents to Beanstream Payments API for Payment Processing & Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Beanstream Payments MCP Server | MCP 触发器 |
| Make Payment | HTTP Request 工具 |
| Get payment | HTTP Request 工具 |
| Complete pre-auth | HTTP Request 工具 |
| Return payment | HTTP Request 工具 |
| Void Transaction | HTTP Request 工具 |
| Create Profile | HTTP Request 工具 |
| Delete profile | HTTP Request 工具 |
| Get profile | HTTP Request 工具 |
| Update Profile | HTTP Request 工具 |
| Get cards | HTTP Request 工具 |
| Add card | HTTP Request 工具 |
| Delete card | HTTP Request 工具 |
| Update card | HTTP Request 工具 |
| Search Query | HTTP Request 工具 |
| Tokenize credit card | HTTP Request 工具 |



## 功能说明

财务自动化，发票处理或支付流程管理。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：16
- 触发方式：手动或子流程调用

## 触发方式
- Beanstream Payments MCP Server 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：0
- 输出节点：15
- 分类：ai-agent
