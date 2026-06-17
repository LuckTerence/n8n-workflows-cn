## 简介
**Create an Offline DIGIPIN Microservice API for Precise Location Mapping in India**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5836

---

# Create an Offline DIGIPIN Microservice API for Precise Location Mapping in India


## 节点清单

| 节点 | 类型 |
|------|------|
| Respond to Webhook - Success | 响应 Webhook |
| Respond to Webhook - Error | 响应 Webhook |
| Switch - Check for Success | Switch 路由 |
| DIGIPIN_Generation_Code | Code |
| DIGIPIN_Decode_Code | Code |
| Encode_Webhook | Webhook |
| Decode_Webhook | Webhook |
| Switch 2 - Check for Success1 | Switch 路由 |
| Respond to Webhook - Success 2 | 响应 Webhook |
| Respond to Webhook - Error 2 | 响应 Webhook |



## 功能说明

API 集成接口，连接和编排多个第三方服务，Webhook 触发。

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

- 节点总数：10
- 触发方式：Webhook 触发

## 触发方式
- Encode_Webhook 触发
- Decode_Webhook 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：4
- 输出节点：4
- 分类：devops
