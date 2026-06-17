## 简介
**fal.ai图片生成**

基于fal.ai的文本生成图片

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4108

---

# fal.ai图片生成


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Fetch Status | HTTP Request |
| Wait | 等待 |
| Is Ready? | IF 判断 |
| Submit Request | HTTP Request |
| Fetch Result | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| 400 Error | 响应 Webhook |
| Success | 响应 Webhook |
| NSFW Filter | 文本分类器 |



## 功能说明

AI 图像生成工作流，文生图或图生图，Webhook 触发。

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

- 节点总数：10
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：4
- 输出节点：5
- 分类：multimodal-ai
