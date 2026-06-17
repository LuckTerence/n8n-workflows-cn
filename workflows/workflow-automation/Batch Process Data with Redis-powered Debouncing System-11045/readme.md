## 简介
**Batch Process Data with Redis-powered Debouncing System**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11045

---

# Batch Process Data with Redis-powered Debouncing System


## 节点清单

| 节点 | 类型 |
|------|------|
| Crypto | 加密 |
| Set last update uuid | Redis |
| Push to message list | Redis |
| Get last update uuid | Redis |
| Am I last? | IF 判断 |
| Set lock | Redis |
| Get messages | Redis |
| Clear messages | Redis |
| Release lock | Redis |
| Get lock value | Redis |
| Is lock active? | IF 判断 |
| Wait for lock release | 等待 |
| Split messages | 数据拆分 |
| Trigger | 执行工作流触发器 |
| Wait | 等待 |



## 功能说明

Batch Process Data with Redis-powered Debouncing S。

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
- 触发方式：手动或子流程调用

## 触发方式
- Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：workflow-automation
