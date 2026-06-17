## 简介
**Automated SEO Keyword & SERP Analysis with DataForSEO for High-Converting Content**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4277

---

# Automated SEO Keyword & SERP Analysis with DataForSEO for High-Converting Content


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Set Main Fields | 数据设置 |
| Set Related KW Fields | 数据设置 |
| Split Out Related KWs | 数据拆分 |
| Google Sheets KW Research Template | Google Sheets |
| Google Drive Create KW Folder | Google Drive |
| Google Drive Copy KW Template | Google Drive |
| HTTP Keyword Suggestions | HTTP Request |
| HTTP Related Keywords | HTTP Request |
| Add Related KWs to Related KWs Sheet | Google Sheets |
| Add Related KWs to Master all KW Variations Sheet | Google Sheets |
| Add KWs to Keyword Suggestions Sheet | Google Sheets |
| Add KWs to Master All KW Sheet | Google Sheets |
| Add KWs to Master All KW Sheet1 | Google Sheets |
| HTTP Keyword Ideas | HTTP Request |
| Split Out KW Suggestions | 数据拆分 |
| Set KW Suggestion Fields | 数据设置 |
| Split Out KW Ideas | 数据拆分 |
| Set KW Ideas Fields | 数据设置 |
| Add KWs to Keyword Ideas Sheet | Google Sheets |
| Split Out Autocomplete | 数据拆分 |
| Set Autocomplete Fields | 数据设置 |
| HTTP Autocomplete | HTTP Request |
| Add Autocomplete to Autocomplete Sheet | Google Sheets |
| Split Out Subtopics | 数据拆分 |
| Set Subtopics Fields | 数据设置 |
| HTTP Subtopics | HTTP Request |
| Add Subtopics to Subtopics Sheet | Google Sheets |
| Add Subtopics to Master KWs Sheet | Google Sheets |
| Filter SERPs | 过滤器 |
| Filter PAA | 过滤器 |
| Set SERP Fields | 数据设置 |
| Split Out PAA | 数据拆分 |
| Set PAA Fields | 数据设置 |
| HTTP SERPs | HTTP Request |
| Split Out SERPs and PAA | 数据拆分 |
| Add Subtopics to Master KW sheet | Google Sheets |
| Add SERPs to SERP Sheet | Google Sheets |
| Add PAA to PAA Sheet | Google Sheets |
| Add PAA to Master KW Variations Sheet | Google Sheets |



## 功能说明

SEO 优化工具，关键词分析和内容优化。

手动触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：40
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：40
- 触发节点：1
- 处理节点：33
- 输出节点：6
- 分类：workflow-automation
