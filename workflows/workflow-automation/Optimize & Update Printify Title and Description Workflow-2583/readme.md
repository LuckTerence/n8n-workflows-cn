## 简介
**Optimize & Update Printify Title and Description Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2583

---

# Optimize & Update Printify Title and Description Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Printify - Get Shops | HTTP Request |
| Printify - Get Products | HTTP Request |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Split - id, title, desc | 数据拆分 |
| Calculator | 计算器工具 |
| Wikipedia | Wikipedia 工具 |
| Printify - Update Product | HTTP Request |
| Brand Guidelines + Custom Instructions | 数据设置 |
| Google Sheets Trigger | Google Sheets 触发器 |
| Printify - Get Shops1 | HTTP Request |
| GS - Add Product Option | Google Sheets |
| Update Product Option | Google Sheets |
| If1 | IF 判断 |
| Number of Options | 数据设置 |
| Calculate Options | Code |
| Remember Options | 数据设置 |
| Generate Title and Desc | OpenAI |
| If | IF 判断 |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停。

手动触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：20
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Google Sheets Trigger 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：14
- 输出节点：4
- 分类：workflow-automation
