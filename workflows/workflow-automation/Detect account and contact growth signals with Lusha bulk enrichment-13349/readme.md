## 简介
**Detect account and contact growth signals with Lusha bulk enrichment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13349

---

# Detect account and contact growth signals with Lusha bulk enrichment


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Signal Check | 定时触发器 |
| Get Target Accounts from CRM | hubspot |
| Format Companies for Bulk | Code |
| Enrich All Companies in Bulk | lusha |
| Detect Signals per Company | Code |
| Has Signals? | IF 判断 |
| Search for Key Contacts | lusha |
| Enrich Contacts from Search | lusha |
| Signal Alert to Sales | Slack |
| Update Account in CRM | hubspot |



## 功能说明

Detect account and contact growth signals with Lus。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- Daily Signal Check 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
