## 简介
**Find the best Roblox server for your game using a webhook and Roblox API**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12194

---

# Find the best Roblox server for your game using a webhook and Roblox API


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Error #1 | 数据设置 |
| Respond with Error #1 | 响应 Webhook |
| Place ID Set? | IF 判断 |
| Auto Config | 数据设置 |
| Fetch Public Servers | HTTP Request |
| Filter For The Best | Code |
| Respond with Success | 响应 Webhook |
| Success | 数据设置 |
| Auto Redirect? | IF 判断 |
| Respond to Webhook | 响应 Webhook |



## 功能说明

联网搜索工具，AI 驱动的信息检索和分析，Webhook 触发。

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

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：devops
