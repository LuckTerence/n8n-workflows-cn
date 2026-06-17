## 简介
**Automated Blog Content Tracking with RSS Feeds and Time-Based Filtering**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9596

---

# Automated Blog Content Tracking with RSS Feeds and Time-Based Filtering


## 节点清单

| 节点 | 类型 |
|------|------|
| Split RSS Feeds | 分批处理 |
| RSS → Items | RSS Feed |
| When clicking ‘Execute workflow’ | 手动触发 |
| Merge3 | 数据合并 |
| Client ID + Max Content Age + Blogs | 数据合并 |
| Find Date & Time of Blogs | 日期时间 |
| Filter Out Old Blogs | IF 判断 |
| max_content_age_days | 数据设置 |
| Split Out | 数据拆分 |
| blogs to track | 数据设置 |
| Rss feed link | 数据设置 |
| rss feed links + blogs | 数据合并 |



## 功能说明

内容管理工具，自动生成或发布内容。

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

- 节点总数：12
- 触发方式：手动触发

## 触发方式
- RSS → Items 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：workflow-automation
