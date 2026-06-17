## 简介
**Run Multiple Tasks in Parallel with Asynchronous Processing and Webhooks**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8578

---

# Run Multiple Tasks in Parallel with Asynchronous Processing and Webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| Start | 手动触发 |
| Call Entry Point | 执行工作流触发器 |
| Wait Seconds | 等待 |
| Call 1 | 执行工作流 |
| Request Webhook | HTTP Request |
| Wait for Webhook 1 | 等待 |
| Wait for Webhook 2 | 等待 |
| Wait 1 Second | 等待 |
| Call 2 | 执行工作流 |
| Merge | 数据合并 |
| Sum | 文本摘要 |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化。

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

- 节点总数：11
- 触发方式：手动触发

## 触发方式
- Start 触发
- Call Entry Point 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
