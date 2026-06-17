## 简介
**Redis Locking for Concurrent Task Handling**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3444

---

# Redis Locking for Concurrent Task Handling


## 节点清单

| 节点 | 类型 |
|------|------|
| END | 空操作 |
| Workflow 1 | 数据设置 |
| Workflow 2 | 数据设置 |
| Workflow 3 | 数据设置 |
| Incoming Webhook Data | Webhook |
| Fetch Webhook Data & Declare lockValue | Code |
| Check Redis Lock | Redis |
| Acquire Redis Lock | Redis |
| redisLock existence boolean | IF 判断 |
| redisLock acquired booleans | IF 判断 |
| Poll for lock | 等待 |
| duplicateWebhook boolean | IF 判断 |
| Discard Redis Lock | Redis |
| Workflow Switch | Switch 路由 |



## 功能说明

Redis Locking for Concurrent Task Handling。

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

- 节点总数：14
- 触发方式：Webhook 触发

## 触发方式
- Incoming Webhook Data 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
