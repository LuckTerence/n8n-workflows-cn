## 简介
**Automatically Correct Wrong Shipping Addresses in Billbee Orders**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2609

---

# Automatically Correct Wrong Shipping Addresses in Billbee Orders


## 节点清单

| 节点 | 类型 |
|------|------|
| get order data | HTTP Request |
| Split Out Order Data | 数据拆分 |
| Set Address Fields | 数据设置 |
| Check Address endereco api | HTTP Request |
| Split Out Corrected Address | 数据拆分 |
| set new delivery address to billbee | HTTP Request |
| Wait | 等待 |
| Wait1 | 等待 |
| check if new address is not empty | IF 判断 |
| set billbee tag | HTTP Request |
| check if housenumer is not empty | IF 判断 |
| check if addressline 2 contains number | IF 判断 |
| Filter | 过滤器 |
| set value of addressline2 as housenumber | 数据设置 |
| Filter Out PickUpShops | 过滤器 |
| check if addressline 2 contains number and letter | IF 判断 |
| set billbee tag manual check | HTTP Request |
| set value of addressline2 as housenumber number+letter | 数据设置 |
| set billbee success | HTTP Request |
| ConfigNode | 数据设置 |
| Webhook | Webhook |



## 功能说明

电商自动化，订单处理或商品管理，Webhook 触发。

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

- 节点总数：21
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：workflow-automation
