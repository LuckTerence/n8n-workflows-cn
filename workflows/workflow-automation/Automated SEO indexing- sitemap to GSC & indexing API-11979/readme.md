## 简介
**Automated SEO indexing: sitemap to GSC & indexing API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11979

---

# Automated SEO indexing: sitemap to GSC & indexing API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Configuration | 数据设置 |
| Fetch Sitemap XML | HTTP Request |
| Convert XML to JSON | XML |
| Parse Sitemap Structure | Code |
| Is Sitemap Index? | IF 判断 |
| Format URL Data | 数据设置 |
| Filter: Recent URLs Only | 过滤器 |
| Check Submission History | Code |
| GSC: Inspect URL Status | HTTP Request |
| Logic: Should Index? | Code |
| Filter: Only Not Indexed | 过滤器 |
| Batch Processing | 分批处理 |
| Delay (Rate Limiting) | 等待 |
| Schedule Trigger | 定时触发器 |
| Filter: Valid for Submission | 过滤器 |
| GSC: Request Indexing | HTTP Request |



## 功能说明

SEO 优化工具，关键词分析和内容优化，定时执行。

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

- 节点总数：17
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：12
- 输出节点：3
- 分类：workflow-automation
