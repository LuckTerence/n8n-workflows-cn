## 简介
**Retrieve and Filter Kagi News by Category**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9318

---

# Retrieve and Filter Kagi News by Category


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 执行工作流触发器 |
| Get Latest Categories | HTTP Request |
| Split Categories | 数据拆分 |
| Filter by wanted category | 过滤器 |
| Get Stories in Category | HTTP Request |
| Split out stories | 数据拆分 |
| Pick only title | 数据设置 |
| Limit to 1 category | 数据限制 |



## 功能说明

内容管理工具，自动生成或发布内容。

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

- 节点总数：8
- 触发方式：手动或子流程调用

## 触发方式
- Start 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
