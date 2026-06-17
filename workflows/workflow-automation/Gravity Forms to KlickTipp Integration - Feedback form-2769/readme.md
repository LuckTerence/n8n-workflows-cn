## 简介
**Gravity Forms to KlickTipp Integration - Feedback form**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2769

---

# Gravity Forms to KlickTipp Integration - Feedback form


## 节点清单

| 节点 | 类型 |
|------|------|
| Subscribe contact in KlickTipp | Klicktipp |
| Convert and set feedback data | 数据设置 |
| Tag contact directly in KlickTipp | Klicktipp |
| Tag creation check | IF 判断 |
| Aggregate tags to add to contact | 数据聚合 |
| Create the tag in KlickTipp | Klicktipp |
| Aggregate array of created tags | 数据聚合 |
| Tag contact KlickTipp after trag creation | Klicktipp |
| Get list of all existing tags | Klicktipp |
| Merge | 数据合并 |
| Define Array of tags from Gravityforms | 数据设置 |
| Split Out Gravityforms tags | 数据拆分 |
| New submission via Gravityforms | Webhook |



## 功能说明

表单问卷工具，自动收集和处理用户反馈，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：Webhook 触发

## 触发方式
- New submission via Gravityforms 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：12
- 输出节点：0
- 分类：workflow-automation
