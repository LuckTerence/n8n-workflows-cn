## 简介
**Standardized Workflow Design Pattern with Color-Coding System for Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9500

---

# Standardized Workflow Design Pattern with Color-Coding System for Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual | 手动触发 |
| Input | Combined | 数据合并 |
| Search records | Airtable |
| Normalize Manual Trigger | 数据设置 |
| Trigger | Normalized | 数据设置 |
| Triggered from other Workflow | 执行工作流触发器 |
| General Webhook | Webhook |
| Normalize Webhook Trigger | 数据设置 |
| Get Data From Google Sheets | Google Sheets |
| Set Defaults | 数据设置 |
| Business Logic Single or Multi step1 | Code |
| Business Logic Single or Multi step | Code |
| Some Old Version | 空操作 |
| Switch | Switch 路由 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，Webhook 触发。

Webhook触发、手动触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：手动触发, Webhook 触发

## 触发方式
- Manual 触发
- Triggered from other Workflow 触发
- General Webhook 触发

## 统计
- 节点总数：14
- 触发节点：3
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
