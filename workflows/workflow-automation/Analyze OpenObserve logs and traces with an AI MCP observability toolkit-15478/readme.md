## 简介
**Analyze OpenObserve logs and traces with an AI MCP observability toolkit**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15478

---

# Analyze OpenObserve logs and traces with an AI MCP observability toolkit


## 节点清单

| 节点 | 类型 |
|------|------|
| Stream Schema Inspection | HTTP Request 工具 |
| Unique Error Fingerprinting | HTTP Request 工具 |
| Volume Trend Analysis | HTTP Request 工具 |
| Log Pattern Discovery | HTTP Request 工具 |
| P99 Latency Analysis | HTTP Request 工具 |
| Cold-Start Identification | HTTP Request 工具 |
| Dependency Hotspots | HTTP Request 工具 |
| SQL logs query | HTTP Request 工具 |
| Span Error Mapping | HTTP Request 工具 |
| SQL traces query | HTTP Request 工具 |
| OpenOberve Tool MCP Server | MCP 触发器 |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

手动触发，通过 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：手动或子流程调用

## 触发方式
- OpenOberve Tool MCP Server 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：0
- 输出节点：10
- 分类：workflow-automation
