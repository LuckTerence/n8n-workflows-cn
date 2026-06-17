## 简介
**Regional Prospecting for registered Companies in Germany**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11750

---

# Regional Prospecting for registered Companies in Germany


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Validate Input | Code |
| Search Success? | IF 判断 |
| Normalize & Score Results | Code |
| Sort by Relevance | Code |
| High Quality Leads? | IF 判断 |
| Prepare High Quality Payload | 数据设置 |
| Prepare Medium Quality Payload | 数据设置 |
| Merge & Log Results | Code |
| Generate Summary Report | 数据设置 |
| Implisense Search | HTTP Request |
| Authorization | 数据设置 |
| Prepare Search Input | 数据设置 |



## 功能说明

Regional Prospecting for registered Companies in G。

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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- Manual Trigger 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：workflow-automation
