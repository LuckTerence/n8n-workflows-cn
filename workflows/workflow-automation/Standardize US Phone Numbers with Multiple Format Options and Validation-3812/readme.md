## 简介
**Standardize US Phone Numbers with Multiple Format Options and Validation**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3812

---

# Standardize US Phone Numbers with Multiple Format Options and Validation


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Check if first digit is valid country code | IF 判断 |
| Add valid country code | 数据设置 |
| Strip phone number formatting | 数据设置 |
| Check number of digits in phone number | Switch 路由 |
| Format phone numbers | 数据设置 |
| Clear invalid number | 数据设置 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈。

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

- 节点总数：7
- 触发方式：手动或子流程调用

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
