## 简介
**KlickTipp tag manager: convert tag names to IDs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11923

---

# KlickTipp tag manager: convert tag names to IDs


## 节点清单

| 节点 | 类型 |
|------|------|
| Find tags to create | 数据合并 |
| Find existing tags | 数据合并 |
| Combine existing & new tags | 数据合并 |
| Split tagNames into items | 数据拆分 |
| Map tagNames -> value | 数据设置 |
| Get tag list | Klicktipp |
| Create new tag | Klicktipp |
| Aggregate tag IDs | 数据聚合 |
| Extract only tag IDs | 数据设置 |
| Input: Tag names | 执行工作流触发器 |



## 功能说明

文件处理工具，自动转换或管理文件。

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

- 节点总数：10
- 触发方式：手动或子流程调用

## 触发方式
- Input: Tag names 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
