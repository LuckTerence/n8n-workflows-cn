## 简介
**Create Professional Marketing Assets with Google Imagen, Ideogram & Placid for Ads & Social**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5017

---

# Create Professional Marketing Assets with Google Imagen, Ideogram & Placid for Ads & Social


## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Status | HTTP Request |
| Wait | 等待 |
| Is Ready? | IF 判断 |
| Fetch Result | HTTP Request |
| Merge | 数据合并 |
| Fetch Status1 | HTTP Request |
| Wait1 | 等待 |
| Is Ready?1 | IF 判断 |
| Fetch Result1 | HTTP Request |
| Download Image | HTTP Request |
| Background Image Prompt Agent | AI Agent |
| Copywriting Agent | AI Agent |
| gpt-4o-mini | OpenAI Chat Model |
| gpt-4.1-mini | OpenAI Chat Model |
| BG Prompt Output Parser | 结构化输出解析器 |
| Copy Output Parser | 结构化输出解析器 |
| Fal.ai Replace Background | HTTP Request |
| Fal.ai Time of Day Relight | HTTP Request |
| Create Image via Template with Placid.app | HTTP Request |
| Save to Google Drive | Google Drive |
| On form submission | 表单触发器 |
| Get a temporary file url for the upload | HTTP Request |
| Fetch Status2 | HTTP Request |
| Wait2 | 等待 |
| Is Ready?2 | IF 判断 |
| Fal.ai Google Image Gen4 | HTTP Request |
| Fetch Style Reference Image | HTTP Request |



## 功能说明

AI 图像生成工作流，文生图或图生图（Professional)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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

- 节点总数：27
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：14
- 输出节点：12
- 分类：workflow-automation
