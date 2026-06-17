## 简介
**Send Postcards to Contacts Automatically using CentralStationCRM and EchtPost**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6124

---

# Send Postcards to Contacts Automatically using CentralStationCRM and EchtPost


## 节点清单

| 节点 | 类型 |
|------|------|
| Person is updated in CentralStationCRM | Webhook |
| Set fields needed for EchtPost | 数据设置 |
| Is "EchtPost" included in "taggings"? | IF 判断 |
| Do nothing | 空操作 |
| Send postcard with EchtPost | HTTP Request |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，Webhook 触发。

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

- 节点总数：5
- 触发方式：Webhook 触发

## 触发方式
- Person is updated in CentralStationCRM 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
