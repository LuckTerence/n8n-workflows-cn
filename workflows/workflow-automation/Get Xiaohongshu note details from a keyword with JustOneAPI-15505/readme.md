## 简介
**Get Xiaohongshu note details from a keyword with JustOneAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15505

---

# Get Xiaohongshu note details from a keyword with JustOneAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Execution Trigger | 手动触发 |
| Prepare API and Research Inputs | 数据设置 |
| Fetch Xiaohongshu Notes by Keyword | HTTP Request |
| Output Search Results Data | 数据设置 |
| Extract Note IDs from Results | Code |
| Output Extracted Note IDs | 数据设置 |
| Fetch Xiaohongshu Note Details | HTTP Request |
| Build Note Details List | Code |
| Output Final Note Details | 数据设置 |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

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
- Manual Execution Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
