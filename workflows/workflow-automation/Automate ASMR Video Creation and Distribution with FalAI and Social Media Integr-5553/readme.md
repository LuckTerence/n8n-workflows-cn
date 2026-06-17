## 简介
**Automate ASMR Video Creation and Distribution with FalAI and Social Media Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5553

---

# Automate ASMR Video Creation and Distribution with FalAI and Social Media Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate Video | HTTP Request |
| Get Result | HTTP Request |
| Result | 数据设置 |
| Get Past Objects | Google Sheets |
| Prompt Agent | AI Agent |
| Idea Agent | AI Agent |
| Aggregate | 数据聚合 |
| Set Object List | 数据设置 |
| YouTube | HTTP Request |
| TikTok | HTTP Request |
| Instagram | HTTP Request |
| Delete First Row | Google Sheets |
| Append Object | Google Sheets |
| Object & Caption | 结构化输出解析器 |
| Upload | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| When clicking ‘Execute workflow’ | 手动触发 |
| 1 Minute - Video taking longer please wait | 等待 |
| 5 Minutes - Wait for Video | 等待 |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：19
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
