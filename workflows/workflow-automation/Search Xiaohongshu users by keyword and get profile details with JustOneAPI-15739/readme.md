## 简介
**Search Xiaohongshu users by keyword and get profile details with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15739

---

# Search Xiaohongshu users by keyword and get profile details with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow | 手动触发 |
| Set API and Search Parameters | 数据设置 |
| Search Xiaohongshu Users by Keyword | HTTP Request |
| Output Search Results | 数据设置 |
| Extract User IDs from Search Results | Code |
| Output Extracted User IDs List | 数据设置 |
| Get Xiaohongshu User Profiles | HTTP Request |
| Build Combined User Profiles | Code |
| Output Final User Profile Data | 数据设置 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：9
- 触发方式：手动触发

## 触发方式
- Start Workflow 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
