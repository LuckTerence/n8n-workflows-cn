## 简介
**Fetch Live ETF Metrics from JustETF to Excel with One-Click Updates**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2519

---

# Fetch Live ETF Metrics from JustETF to Excel with One-Click Updates


## 节点清单

| 节点 | 类型 |
|------|------|
| Loop Over Items | 分批处理 |
| Logs the date & time | microsoftExcel |
| Gets rows from table | microsoftExcel |
| Forge a Get request with ISIN Values | HTTP Request |
| Extracts defined values with css selector | HTML |
| Extracts defined values in better format | Code |
| Updates my table | microsoftExcel |
| When called by Excel Macro | Webhook |
| Edit Fields | 数据设置 |
| When clicking ‘Test workflow’ | 手动触发 |



## 功能说明

Fetch Live ETF Metrics from JustETF to Excel with。

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

- 节点总数：10
- 触发方式：Webhook 触发, 手动触发

## 触发方式
- When called by Excel Macro 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：7
- 输出节点：1
- 分类：workflow-automation
