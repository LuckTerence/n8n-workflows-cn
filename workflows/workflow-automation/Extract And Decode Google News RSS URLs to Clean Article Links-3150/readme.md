## 简介
**Extract And Decode Google News RSS URLs to Clean Article Links**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3150

---

# Extract And Decode Google News RSS URLs to Clean Article Links


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Limit | 数据限制 |
| Reading Google News RSS | RSS Feed |
| Decoded url | 数据设置 |
| Call decoding URL | HTTP Request |
| Prepare decoding variables | Code |
| Get encoded news URL | HTTP Request |
| Map needed keys | 数据设置 |
| Extract decoding keys | HTML |
| Aggregate results in a single object | 数据聚合 |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Reading Google News RSS 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
