## 简介
**Send Server-Side Conversions to the Meta Ads API (CAPI)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11089

---

# Send Server-Side Conversions to the Meta Ads API (CAPI)


## 节点清单

| 节点 | 类型 |
|------|------|
| Edit Normalize PII | 数据设置 |
| Crypto - Hash Email | 加密 |
| Crypto - Hash Phone | 加密 |
| Set - Compute Timestamps & Map Fields | 数据设置 |
| Crypto - First Name | 加密 |
| Crypto - Last Name | 加密 |
| Sending Events To Facebook Pixel | HTTP Request |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Preparing for HTTP Request Payload | Code |



## 功能说明

API 集成接口，连接和编排多个第三方服务，Webhook 触发。

Webhook触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：devops
