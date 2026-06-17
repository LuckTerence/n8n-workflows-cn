## 简介
**EPA Environmental Compliance Data API for AI Agents with MCP Server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5636

---

# EPA Environmental Compliance Data API for AI Agents with MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| U.S. EPA Enforcement and Compliance History Online (ECHO) - Resource Conservation and Recovery Act MCP Server | MCP 触发器 |
| Download RCRA Data | HTTP Request 工具 |
| Request RCRA Data Download | HTTP Request 工具 |
| Search RCRA Facilities | HTTP Request 工具 |
| Request RCRA Facility Search | HTTP Request 工具 |
| Get RCRA Facility Details | HTTP Request 工具 |
| Request RCRA Facility Details | HTTP Request 工具 |
| Get RCRA GeoJSON Data | HTTP Request 工具 |
| Request RCRA GeoJSON Data | HTTP Request 工具 |
| Get RCRA Info Clusters | HTTP Request 工具 |
| Request RCRA Info Clusters | HTTP Request 工具 |
| Get RCRA Map Data | HTTP Request 工具 |
| Request RCRA Map Data | HTTP Request 工具 |
| Get RCRA Paginated Results | HTTP Request 工具 |
| Request RCRA Paginated Results | HTTP Request 工具 |
| Get RCRA Metadata | HTTP Request 工具 |
| Request RCRA Metadata | HTTP Request 工具 |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

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

- 节点总数：17
- 触发方式：手动或子流程调用

## 触发方式
- U.S. EPA Enforcement and Compliance History Online (ECHO) - Resource Conservation and Recovery Act MCP Server 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：0
- 输出节点：16
- 分类：devops
