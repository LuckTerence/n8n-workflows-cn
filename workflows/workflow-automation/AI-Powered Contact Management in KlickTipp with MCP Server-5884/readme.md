## 简介
**AI-Powered Contact Management in KlickTipp with MCP Server**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5884

---

# AI-Powered Contact Management in KlickTipp with MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| MCP Server Trigger | MCP 触发器 |
| Timestamp to date | 代码工具 |
| Date to timestamp | 代码工具 |
| Get Contact ID | Klicktipp 工具 |
| Get Contact | Klicktipp 工具 |
| Add or Update Contact | Klicktipp 工具 |
| List Contacts | Klicktipp 工具 |
| Update Contact | Klicktipp 工具 |
| Delete Contact | Klicktipp 工具 |
| Unsubscribe Contact | Klicktipp 工具 |
| List Tagged Contacts | Klicktipp 工具 |
| Tag Contact | Klicktipp 工具 |
| Untag Contact | Klicktipp 工具 |
| Get Data Field | Klicktipp 工具 |
| List Data Fields | Klicktipp 工具 |
| List Opt-in Processes | Klicktipp 工具 |
| Get Opt-in Process | Klicktipp 工具 |
| Get Redirect URL | Klicktipp 工具 |
| List Tags | Klicktipp 工具 |
| Create Tag | Klicktipp 工具 |
| Get Tag | Klicktipp 工具 |
| Delete Tag | Klicktipp 工具 |
| Update Tag | Klicktipp 工具 |



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：23
- 触发方式：手动或子流程调用

## 触发方式
- MCP Server Trigger 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：22
- 输出节点：0
- 分类：workflow-automation
