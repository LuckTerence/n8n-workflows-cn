## 简介
**Automate RSS-to-Social Media with AI Summaries and Image Generation**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Sheets/Supabase)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9208

---

# Automate RSS-to-Social Media with AI Summaries and Image Generation


## 节点清单

| 节点 | 类型 |
|------|------|
| RSS Feed Trigger | rssFeedReadTrigger |
| Get row(s) in sheet | Google Sheets |
| If | IF 判断 |
| HTTP Request | HTTP Request |
| HTML | HTML |
| Basic LLM Chain | LLM Chain |
| Append row in sheet | Google Sheets |
| Post to Instagram | HTTP Request |
| Post to Instagram1 | HTTP Request |
| Get Post URL | HTTP Request |
| Send a photo message | Telegram |
| Basic LLM Chain1 | LLM Chain |
| Anthropic Chat Model | OpenAI Chat Model |
| Google Gemini Chat Model | OpenAI Chat Model |
| Post to Facebook | HTTP Request |
| Merge | 数据合并 |
| Send a text message | Telegram |
| Generate an image | OpenAI |
| Edit Fields | 数据设置 |
| Upload to Supabase (uses credentials) | HTTP Request |
| Supabase Config | 数据设置 |
| Supabase Public URL | 数据设置 |
| Build Facebook URL | Code |
| Build Instagram URL | Code |
| Collect Important Data | Code |



## 功能说明

AI 图像生成工作流，文生图或图生图。

手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：手动或子流程调用

## 触发方式
- RSS Feed Trigger 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：16
- 输出节点：8
- 分类：multimodal-ai
