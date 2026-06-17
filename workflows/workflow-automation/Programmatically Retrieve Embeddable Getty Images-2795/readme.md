## 简介
**Programmatically Retrieve Embeddable Getty Images**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2795

---

# Programmatically Retrieve Embeddable Getty Images


## 节点清单

| 节点 | 类型 |
|------|------|
| Parse results page for first image | HTML |
| Continue if a result exists | IF 判断 |
| Extract the Getty image_id from url | 数据设置 |
| Get photo details | HTTP Request |
| GET img src | HTML |
| Get Embeddable iframeSnippet | 数据设置 |
| Request Getty Images Embed code | HTTP Request |
| Raise error when no results | 停止并报错 |
| Replace with CMS node | 空操作 |
| Getty Images Editorial Search | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Replaceable input | 数据设置 |
| Preview image (view binary) | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：8
- 输出节点：4
- 分类：workflow-automation
