## 简介
**Fetch Odoo Customer Data and Export to JSON or Excel**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10599

---

# Fetch Odoo Customer Data and Export to JSON or Excel


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Company Request1 | Webhook |
| Prepare Dynamic Filter1 | Function |
| Prepare Output Data1 | Function |
| Check If Excel Required1 | IF 判断 |
| Convert to Excel1 | 转换为文件 |
| Respond with File1 | 响应 Webhook |
| Respond with JSON1 | 响应 Webhook |
| Fetch Customer | odoo |
| Return all data for create binary file | Code |



## 功能说明

Fetch Odoo Customer Data and Export to JSON or Exc。

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

- 节点总数：9
- 触发方式：Webhook 触发

## 触发方式
- Receive Company Request1 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
