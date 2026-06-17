## 简介
**Sell a Used Car with an AI Agent in Airtop**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3483

---

# Sell a Used Car with an AI Agent in Airtop


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Variables | 数据设置 |
| Wait 7 secs | 等待 |
| Parse response | Code |
| Switch | Switch 路由 |
| Offer received | 数据设置 |
| Type | Airtop |
| Click | Airtop |
| Create session | Airtop |
| Load website | Airtop |
| Click VIN button | Airtop |
| Terminate session | Airtop |
| Take screenshot | Airtop |
| Think next action | Airtop |



## 功能说明

Sell a Used Car with an AI Agent in Airtop。

手动触发，通过 工作流编排 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：ai-agent
