## 简介
**Route and analyze customer feedback with Qwen3-VL, Tally, PostgreSQL**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13314

---

# Route and analyze customer feedback with Qwen3-VL, Tally, PostgreSQL


## 节点清单

| 节点 | 类型 |
|------|------|
| Tally Trigger | tallyTrigger |
| Field Mapping | 数据设置 |
| Sentiment Analysis | LLM Chain |
| If | IF 判断 |
| Fetch Image | HTTP Request |
| Routing LLM | OpenAI Chat Model |
| #general-inquiries | 数据设置 |
| #happy-customers | 数据设置 |
| Decision Logic | LLM Chain |
| Send Discord Notification | Discord |
| Sentiment LLM | OpenAI Chat Model |
| Sentiment Parser | 结构化输出解析器 |
| Text Classification | LLM Chain |
| Classification LLM | OpenAI Chat Model |
| Classification Parser | 结构化输出解析器 |
| Image Keyword Extraction | Code |
| Empty Keywords Handler | 数据设置 |
| Image Results Merge | 数据合并 |
| AI Results Merge | 数据合并 |
| Data Aggregation | 数据聚合 |
| Save to PostgreSQL | PostgreSQL |
| Route Parser | 结构化输出解析器 |
| Channel Router | Switch 路由 |
| #support-urgent | 数据设置 |
| Build Discord Message | 数据合并 |
| Format Embed Data | Code |



## 功能说明

表单问卷工具，自动收集和处理用户反馈。

手动触发，通过 数据库 + Discord + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：手动或子流程调用

## 触发方式
- Tally Trigger 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：23
- 输出节点：2
- 分类：workflow-automation
