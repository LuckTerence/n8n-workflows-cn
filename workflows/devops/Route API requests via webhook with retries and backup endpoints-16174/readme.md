## 简介
**Route API requests via webhook with retries and backup endpoints**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16174

---

# Route API requests via webhook with retries and backup endpoints


## 节点清单

| 节点 | 类型 |
|------|------|
| API Recovery Webhook | Webhook |
| Extract Request Configuration | 数据设置 |
| Execute Primary API Request | HTTP Request |
| Check Primary API Success | IF 判断 |
| Return Primary API Response | 响应 Webhook |
| Wait Before Retry Attempt | 等待 |
| Retry Primary API Request | HTTP Request |
| Check Retry API Success | IF 判断 |
| Return Retry API Response | 响应 Webhook |
| Execute Backup API Request | HTTP Request |
| Check Backup API Success | IF 判断 |
| Return Backup API Response | 响应 Webhook |
| Prepare Failure Payload | 数据设置 |
| Return Final Failure Response | 响应 Webhook |



## 功能说明

自动备份系统，定时备份数据或配置，Webhook 触发。

定时触发、Webhook触发，通过 HTTP API 实现自动化。

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
- API Recovery Webhook 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：6
- 输出节点：7
- 分类：devops
