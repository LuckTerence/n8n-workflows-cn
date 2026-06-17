## 简介
**Search, Manage, and Analyze Podcasts with Listen API for AI Agents**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5605

---

# Search, Manage, and Analyze Podcasts with Listen API for AI Agents


## 节点清单

| 节点 | 类型 |
|------|------|
| Listen API: Podcast Search, Directory, and Insights MCP Server | MCP 触发器 |
| Fetch Best Podcasts by Genre | HTTP Request 工具 |
| Fetch Curated Podcast Lists | HTTP Request 工具 |
| Fetch Curated Podcast List by ID | HTTP Request 工具 |
| Batch Fetch Episode Metadata | HTTP Request 工具 |
| Fetch Episode Details by ID | HTTP Request 工具 |
| Fetch Episode Recommendations | HTTP Request 工具 |
| Fetch Podcast Genres | HTTP Request 工具 |
| Fetch Random Podcast Episode | HTTP Request 工具 |
| Fetch Supported Languages | HTTP Request 工具 |
| Batch Fetch Podcast Metadata | HTTP Request 工具 |
| Fetch Podcast Details by ID | HTTP Request 工具 |
| Fetch Podcast Recommendations | HTTP Request 工具 |
| Fetch Supported Regions | HTTP Request 工具 |
| Fetch User Playlists | HTTP Request 工具 |
| Fetch Playlist Details by ID | HTTP Request 工具 |
| Submit Podcast to Database | HTTP Request 工具 |
| Delete Podcast by ID | HTTP Request 工具 |
| Fetch Podcast Audience Data | HTTP Request 工具 |
| Fetch Related Search Terms | HTTP Request 工具 |
| Full-Text Search | HTTP Request 工具 |
| Spell Check Search Term | HTTP Request 工具 |
| Fetch Trending Search Terms | HTTP Request 工具 |
| Typeahead Search | HTTP Request 工具 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

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

- 节点总数：24
- 触发方式：手动或子流程调用

## 触发方式
- Listen API: Podcast Search, Directory, and Insights MCP Server 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：0
- 输出节点：23
- 分类：workflow-automation
