## 简介
**Learn Workflow Logic with Merge, IF & Switch Operations**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5996

---

# Learn Workflow Logic with Merge, IF & Switch Operations


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Sorting | 手动触发 |
| Add 'Fragile' Handling | 数据设置 |
| Add 'Standard' Handling | 数据设置 |
| Send to London Bin | 数据设置 |
| Send to New York Bin | 数据设置 |
| Send to Tokyo Bin | 数据设置 |
| Default Bin | 数据设置 |
| Final Sorted Packages | 空操作 |
| 3. Switch Node | Switch 路由 |
| Create Letter | 数据设置 |
| 1. Merge Node | 数据合并 |
| 2. IF Node | IF 判断 |
| Re-group All Packages | 数据合并 |
| Create 2nd Letter | 数据设置 |
| Create Parcel | 数据设置 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

手动触发，通过 工作流编排 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：15
- 触发方式：手动触发

## 触发方式
- Start Sorting 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：devops
