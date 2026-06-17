## 简介
**Evaluate Animal Advocacy Text with Hugging Face Open Paws AI Models**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5587

---

# Evaluate Animal Advocacy Text with Hugging Face Open Paws AI Models


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Get Performance Score | HTTP Request |
| Get Preference Score | HTTP Request |
| Set Performance Score | 数据设置 |
| Get Preference Score2 | 数据设置 |
| Set Output | 数据设置 |
| Merge Branches | 数据合并 |
| Create Single Item | 数据聚合 |



## 功能说明

Evaluate Animal Advocacy Text with Hugging Face Op。

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
- When Executed by Another Workflow 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
