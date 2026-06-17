## 简介
**Audio & Video Data Search and Analysis with Clarify API and AI Agent Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5557

---

# Audio & Video Data Search and Analysis with Clarify API and AI Agent Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| api.clarify.io MCP Server | MCP 触发器 |
| List Bundles | HTTP Request 工具 |
| Create Bundle 3 | HTTP Request 工具 |
| Delete Bundle 4 | HTTP Request 工具 |
| Retrieve Bundle | HTTP Request 工具 |
| Update Bundle 4 | HTTP Request 工具 |
| Retrieve Bundle Insights | HTTP Request 工具 |
| Request Insight Run | HTTP Request 工具 |
| Retrieve Bundle Insight | HTTP Request 工具 |
| Delete Bundle Metadata | HTTP Request 工具 |
| Retrieve Bundle Metadata | HTTP Request 工具 |
| Update Bundle Metadata | HTTP Request 工具 |
| Delete Bundle Tracks | HTTP Request 工具 |
| Retrieve Bundle Tracks | HTTP Request 工具 |
| Add Bundle Track | HTTP Request 工具 |
| Update Bundle Tracks | HTTP Request 工具 |
| Delete Bundle Track | HTTP Request 工具 |
| Retrieve Bundle Track | HTTP Request 工具 |
| Add Media to Track | HTTP Request 工具 |
| Generate Group Report | HTTP Request 工具 |
| Generate Trends Report | HTTP Request 工具 |
| Search Bundles | HTTP Request 工具 |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

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

- 节点总数：22
- 触发方式：手动或子流程调用

## 触发方式
- api.clarify.io MCP Server 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：0
- 输出节点：21
- 分类：workflow-automation
