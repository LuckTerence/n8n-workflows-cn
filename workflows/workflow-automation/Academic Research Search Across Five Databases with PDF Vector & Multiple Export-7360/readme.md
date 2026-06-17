## 简介
**Academic Research Search Across Five Databases with PDF Vector & Multiple Exports**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7360

---

# Academic Research Search Across Five Databases with PDF Vector & Multiple Exports


## 节点清单

| 节点 | 类型 |
|------|------|
| Set Search Parameters | 数据设置 |
| PDF Vector - Multi-DB Search | pdfVector |
| Deduplicate Results | Code |
| Rank by Relevance | Code |
| Generate BibTeX | Code |
| Export BibTeX File | 写入二进制文件 |
| Export JSON | 写入二进制文件 |
| Export CSV | 写入二进制文件 |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析。

手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：8
- 触发方式：手动或子流程调用

## 触发方式
- 手动触发

## 统计
- 节点总数：8
- 触发节点：0
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
