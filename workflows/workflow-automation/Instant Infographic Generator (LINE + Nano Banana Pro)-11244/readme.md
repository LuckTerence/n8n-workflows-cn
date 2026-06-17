## 简介
**Instant Infographic Generator (LINE + Nano Banana Pro)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11244

---

# Instant Infographic Generator (LINE + Nano Banana Pro)


## 节点清单

| 节点 | 类型 |
|------|------|
| LINE Webhook | Webhook |
| Extract Data | Code |
| Optimize Prompt (Data Vis) | OpenAI Chat Model |
| Parse Gemini Response | Code |
| Submit to Nano Banana Pro | HTTP Request |
| Wait | 等待 |
| Check Job Status | HTTP Request |
| Is Ready? | IF 判断 |
| Parse Result | Code |
| Download Image | HTTP Request |
| Upload to S3 | awsS3 |
| Send Image to LINE | HTTP Request |



## 功能说明

Instant Infographic Generator (LINE + Nano Banana （AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- LINE Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
