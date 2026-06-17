## 简介
**Parse and Extract Invoice Data with Nanonets OCR and Export to Excel**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6194

---

# Parse and Extract Invoice Data with Nanonets OCR and Export to Excel


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| HTTP Request2 | HTTP Request |
| Convert to File | 转换为文件 |
| Code | Code |
| Code1 | Code |
| Wait | 等待 |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，Webhook 触发。

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

- 节点总数：8
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
