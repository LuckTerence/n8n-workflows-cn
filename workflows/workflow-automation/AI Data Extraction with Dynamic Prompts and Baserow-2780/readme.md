## 简介
**AI Data Extraction with Dynamic Prompts and Baserow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2780

---

# AI Data Extraction with Dynamic Prompts and Baserow


## 节点清单

| 节点 | 类型 |
|------|------|
| Baserow Event | Webhook |
| Event Type | Switch 路由 |
| Table Fields API | HTTP Request |
| Get Prompt Fields | Code |
| Get Event Body | 数据设置 |
| List Table API | HTTP Request |
| Get Valid Rows | Code |
| Get File Data | HTTP Request |
| Extract from File | 从文件提取 |
| Update Row | HTTP Request |
| Get Result | 数据设置 |
| Loop Over Items | 分批处理 |
| Row Reference | 空操作 |
| Generate Field Value | LLM Chain |
| Get Row | HTTP Request |
| Rows to List | 数据拆分 |
| Fields to Update | Code |
| Loop Over Items1 | 分批处理 |
| Row Ref | 空操作 |
| Get File Data1 | HTTP Request |
| Extract from File1 | 从文件提取 |
| Update Row1 | HTTP Request |
| Get Result1 | 数据设置 |
| Generate Field Value1 | LLM Chain |
| Filter Valid Rows | 过滤器 |
| Filter Valid Fields | 过滤器 |
| Event Ref | 空操作 |
| Event Ref1 | 空操作 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：30
- 触发方式：Webhook 触发

## 触发方式
- Baserow Event 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：22
- 输出节点：7
- 分类：workflow-automation
