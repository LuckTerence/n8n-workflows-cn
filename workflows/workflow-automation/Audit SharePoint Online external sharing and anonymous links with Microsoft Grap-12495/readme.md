## 简介
**Audit SharePoint Online external sharing and anonymous links with Microsoft Graph**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12495

---

# Audit SharePoint Online external sharing and anonymous links with Microsoft Graph


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Sharepoint - Get Sites | HTTP Request |
| Split Out - Sites | 数据拆分 |
| SharePoint - Get Drives | HTTP Request |
| Split Out - Drives | 数据拆分 |
| SharePoint - Get Item Permissions | HTTP Request |
| Filter Items based on permissions | Code |
| SharePoint - Get Items | HTTP Request |
| Split Out - Items | 数据拆分 |
| If Item is not a folder | IF 判断 |
| If Input is a Folder | IF 判断 |
| SharePoint - Get Child Items | HTTP Request |
| Call 'Audit SharePoint for externally shared Items and anonymous permissions' | 执行工作流 |
| Subworkflow - Get Items | 执行工作流触发器 |
| Recursive call Get Items | 执行工作流 |
| Return All Data | 数据设置 |
| Keept Items and Folders | 数据合并 |
| Merge | 数据合并 |
| Rename Output for Permissions | 数据设置 |
| Rename Output for Item | 数据设置 |
| Set Variables | 数据设置 |
| Filter sites | 过滤器 |



## 功能说明

Audit SharePoint Online external sharing and anony。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Subworkflow - Get Items 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：15
- 输出节点：5
- 分类：workflow-automation
