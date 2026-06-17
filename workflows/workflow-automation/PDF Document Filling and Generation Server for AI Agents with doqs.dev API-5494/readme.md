## 简介
**PDF Document Filling and Generation Server for AI Agents with doqs.dev API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5494

---

# PDF Document Filling and Generation Server for AI Agents with doqs.dev API


## 节点清单

| 节点 | 类型 |
|------|------|
| doqs.dev | PDF filling MCP Server | MCP 触发器 |
| List Templates | HTTP Request 工具 |
| Create Template | HTTP Request 工具 |
| Preview | HTTP Request 工具 |
| Delete | HTTP Request 工具 |
| List Templates 1 | HTTP Request 工具 |
| Update Template | HTTP Request 工具 |
| Generate Pdf | HTTP Request 工具 |
| List | HTTP Request 工具 |
| Create | HTTP Request 工具 |
| Delete | HTTP Request 工具 |
| Get Template | HTTP Request 工具 |
| Update | HTTP Request 工具 |
| Get File | HTTP Request 工具 |
| Fill | HTTP Request 工具 |



## 功能说明

PDF 文档处理，解析或生成 PDF 文件。

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

- 节点总数：15
- 触发方式：手动或子流程调用

## 触发方式
- doqs.dev | PDF filling MCP Server 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：0
- 输出节点：14
- 分类：workflow-automation
