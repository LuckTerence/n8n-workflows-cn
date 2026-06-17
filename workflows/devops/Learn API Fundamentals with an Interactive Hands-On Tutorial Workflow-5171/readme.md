## 简介
**Learn API Fundamentals with an Interactive Hands-On Tutorial Workflow**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5171

---

# Learn API Fundamentals with an Interactive Hands-On Tutorial Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Tutorial | 手动触发 |
| 1. The Kitchen (GET /menu) | Webhook |
| Respond with Menu | 数据设置 |
| 1. The Customer (GET Menu Item) | HTTP Request |
| 2. The Customer (GET with Query Params) | HTTP Request |
| 2. The Kitchen (GET /order) | Webhook |
| Respond with Cheese | 数据设置 |
| Respond with Plain | 数据设置 |
| 3. The Customer (POST with Body) | HTTP Request |
| 3. The Kitchen (POST /review) | Webhook |
| Respond to Review | 数据设置 |
| 4. The Customer (GET with Headers/Auth) | HTTP Request |
| 4. The Kitchen (GET /secret-dish) | Webhook |
| Respond with Secret | 数据设置 |
| Respond with Error | 数据设置 |
| 5. The Customer (Request with Timeout) | HTTP Request |
| 5. The Kitchen (GET /slow-service) | Webhook |
| Respond Slowly | 数据设置 |
| Wait 3 seconds | 等待 |
| Base URL | 数据设置 |
| IF Authorized | IF 判断 |
| IF extra cheese | IF 判断 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，Webhook 触发。

Webhook触发、手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：手动触发, Webhook 触发

## 触发方式
- Start Tutorial 触发
- 1. The Kitchen (GET /menu) 触发
- 2. The Kitchen (GET /order) 触发
- 3. The Kitchen (POST /review) 触发
- 4. The Kitchen (GET /secret-dish) 触发
- 5. The Kitchen (GET /slow-service) 触发

## 统计
- 节点总数：22
- 触发节点：6
- 处理节点：11
- 输出节点：5
- 分类：devops
