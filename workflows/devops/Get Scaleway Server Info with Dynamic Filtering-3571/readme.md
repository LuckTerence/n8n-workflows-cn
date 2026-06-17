## 简介
**Get Scaleway Server Info with Dynamic Filtering**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3571

---

# Get Scaleway Server Info with Dynamic Filtering


## 节点清单

| 节点 | 类型 |
|------|------|
| Code | Code |
| Edit Fields | 数据设置 |
| Switch | Switch 路由 |
| Code search Tags | Code |
| Code search Name | Code |
| Code search public_ip | Code |
| Code search zone | Code |
| Webhook | Webhook |
| Respond Error | 响应 Webhook |
| Respond to Webhook1 | 响应 Webhook |
| Respond to Webhook2 | 响应 Webhook |
| Respond to Webhook3 | 响应 Webhook |
| Respond to Webhook | 响应 Webhook |
| Get Scalway Machines | HTTP Request |
| Loop Over Items | 分批处理 |
| Respond to Webhook4 | 响应 Webhook |
| Get scw instance by zone | HTTP Request |
| Loop Over Zone Instance | 分批处理 |
| Get scw baremetal by zone | HTTP Request |
| Split Out ZONE_INSTANCE | 数据拆分 |
| If ZONE_BAREMETAL in ZONE_INSTANCE | IF 判断 |



## 功能说明

Get Scaleway Server Info with Dynamic Filtering。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：11
- 输出节点：9
- 分类：devops
