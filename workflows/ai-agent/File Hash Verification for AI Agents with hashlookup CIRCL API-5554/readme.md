## 简介
**File Hash Verification for AI Agents with hashlookup CIRCL API**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5554

---

# File Hash Verification for AI Agents with hashlookup CIRCL API


## 节点清单

| 节点 | 类型 |
|------|------|
| hashlookup CIRCL MCP Server | MCP 触发器 |
| Bulk Search MD5 Hashes | HTTP Request 工具 |
| Bulk Search SHA1 Hashes | HTTP Request 工具 |
| List SHA1 Children | HTTP Request 工具 |
| Get Database Info | HTTP Request 工具 |
| Lookup MD5 Hash | HTTP Request 工具 |
| Lookup SHA1 Hash | HTTP Request 工具 |
| Lookup SHA256 Hash | HTTP Request 工具 |
| List SHA1 Parents | HTTP Request 工具 |
| Create Search Session | HTTP Request 工具 |
| Get Session Results | HTTP Request 工具 |
| Get Top Queries | HTTP Request 工具 |



## 功能说明

文件处理工具，自动转换或管理文件。

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

- 节点总数：12
- 触发方式：手动或子流程调用

## 触发方式
- hashlookup CIRCL MCP Server 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：0
- 输出节点：11
- 分类：ai-agent
