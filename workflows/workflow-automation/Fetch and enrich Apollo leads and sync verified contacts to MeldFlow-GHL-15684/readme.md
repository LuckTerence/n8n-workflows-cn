## 简介
**Fetch and enrich Apollo leads and sync verified contacts to MeldFlow-GHL**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15684

---

# Fetch and enrich Apollo leads and sync verified contacts to MeldFlow-GHL


## 节点清单

| 节点 | 类型 |
|------|------|
| If Apollo Email Verified | IF 判断 |
| Update Page Number | Google Sheets |
| Apollo-Enrichment1 | HTTP Request |
| Wait1 | 等待 |
| Loop Over for batching limit | 分批处理 |
| Meldflow-Contacts | HTTP Request |
| Wait | 等待 |
| Schedule Trigger | 定时触发器 |
| Apollo lead search | HTTP Request |
| Data Filtering & Formatting | 数据设置 |
| Extract ID | Code |
| Get Apollo Page | Google Sheets |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
