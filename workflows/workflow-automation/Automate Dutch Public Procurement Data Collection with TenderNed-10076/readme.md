## 简介
**Automate Dutch Public Procurement Data Collection with TenderNed**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10076

---

# Automate Dutch Public Procurement Data Collection with TenderNed


## 节点清单

| 节点 | 类型 |
|------|------|
| Haal XML Details | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| XML | XML |
| Merge | 数据合并 |
| Haal JSON Details | HTTP Request |
| Aggregate | 数据聚合 |
| Splits Alle Velden | Code |
| Verwerk Response | Code |
| Filter op ... | 过滤器 |
| Insert row | 数据表 |
| Tenderned Publicaties | HTTP Request |
| Schedule Trigger | 定时触发器 |



## 功能说明

Automate Dutch Public Procurement Data Collection。

定时触发、手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：14
- 触发节点：2
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
