## 简介
**Generate stale page reports for Confluence spaces with REST API v1 and v2**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12237

---

# Generate stale page reports for Confluence spaces with REST API v1 and v2


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Variables | 数据设置 |
| Confluence - Get Spaces | HTTP Request |
| Format Space Ids | 数据设置 |
| Confluence - Get Outdated Spaces via CQL | HTTP Request |
| Filter Version by cutoffDate | 过滤器 |
| Switch API Version | Switch 路由 |
| Set Report Data V2 | 数据设置 |
| Set Report Data V1 | 数据设置 |
| Split Out Pages V1 | 数据拆分 |
| Split Out Pages V2 | 数据拆分 |
| Aggregate | 数据聚合 |
| Confluence - Get Pages | HTTP Request |



## 功能说明

API 集成接口，连接和编排多个第三方服务。

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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：9
- 输出节点：3
- 分类：workflow-automation
