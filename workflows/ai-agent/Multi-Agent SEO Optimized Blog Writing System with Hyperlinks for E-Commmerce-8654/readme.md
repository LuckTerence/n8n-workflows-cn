## 简介
**Multi-Agent SEO Optimized Blog Writing System with Hyperlinks for E-Commmerce**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Google Docs/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8654

---

# Multi-Agent SEO Optimized Blog Writing System with Hyperlinks for E-Commmerce


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Tavily search results | HTTP 工具 |
| Anthropic Chat Model | OpenAI Chat Model |
| Airtable Get Article Data | Airtable |
| Set Airtable Fields for Agents | 数据设置 |
| Set KWs and Insights fields | 数据设置 |
| Refine the Title | AI Agent |
| Set Key Takeaways | 数据设置 |
| Key Takeaways AI Agent | AI Agent |
| Set Introduction Field | 数据设置 |
| Outline Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Set Outline Fields | 数据设置 |
| Content Writer Agent | AI Agent |
| Introduction Agent | AI Agent |
| OpenAI Chat Model2 | OpenAI Chat Model |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Create Article Folder | Google Drive |
| Google Drive | Google Drive |
| Edit Fields | 数据设置 |
| Airtable | Airtable |
| Edit Fields1 | 数据设置 |
| SERPs, Writing, KWs, Insights | AI Agent |
| Update Article Writer table | Airtable |
| Sets New Title Field | 数据设置 |
| Update Article Title | Airtable |
| Open AI | OpenAI Chat Model |
| OpenAI Key Takeaways | OpenAI Chat Model |
| OpenAI | OpenAI Chat Model |
| Main Body Prompt Writer | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| AI Agent Conclusion Writer | AI Agent |
| Set Conclusion | 数据设置 |
| OpenAI Chat Model5 | OpenAI Chat Model |
| Create Doc Filename is title | Google Docs |
| Add Final Article | Google Docs |
| Add Meta Description | Google Docs |
| OpenAI Meta | OpenAI |
| Update Article Writer table1 | Airtable |
| OpenAI Image Prompt1 | OpenAI |
| Add Image Prompt1 | Google Docs |
| Set Airtable Fields | 数据设置 |
| Set KWs and Insights fields1 | 数据设置 |
| Article Assembly Agent1 | AI Agent |
| Final Edit Agent1 | AI Agent |
| OpenAI Chat Model6 | OpenAI Chat Model |
| Final Article1 | 数据设置 |
| Final Article | 数据设置 |
| HTTP Request | HTTP Request |
| XML | XML |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| HTTP Request1 | HTTP Request |
| XML1 | XML |
| Open AI1 | OpenAI Chat Model |
| Set list URLs | 数据设置 |
| Set best urls | 数据设置 |
| Set Airtable Fields for Agent | 数据设置 |
| URLs Selection | AI Agent |
| Code in JavaScript | Code |



## 功能说明

多智能体协作系统，多个 AI Agent 协同完成任务，Webhook 触发。

Webhook触发，通过 在线表格 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：60
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：60
- 触发节点：1
- 处理节点：56
- 输出节点：3
- 分类：ai-agent
