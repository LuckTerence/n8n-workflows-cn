## 简介
**Simple Google indexing Workflow in N8N**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2123

---

# Simple Google indexing Workflow in N8N


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Schedule Trigger | 定时触发器 |
| loop | 分批处理 |
| sitemap_set | HTTP Request |
| sitemap_convert | XML |
| sitemap_parse | 数据拆分 |
| url_set | 数据设置 |
| url_index | HTTP Request |
| index_check | IF 判断 |
| wait | 等待 |
| Stop and Error | 停止并报错 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，定时执行。

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

- 节点总数：11
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking "Execute Workflow" 触发
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
