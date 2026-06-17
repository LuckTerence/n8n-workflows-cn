## 简介
**Generate AI images with Telegram bot & auto-publish to social media using Nano Banana PRO**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11765

---

# Generate AI images with Telegram bot & auto-publish to social media using Nano Banana PRO


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| HTTP Request2 | HTTP Request |
| HTTP Request1 | HTTP Request |
| Telegram Trigger | Telegram 触发器 |
| Switch | Switch 路由 |
| Ask for Text Prompt | Telegram |
| Ask for Image Upload | Telegram |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Send a photo message | Telegram |
| If | IF 判断 |
| Wait | 等待 |
| Upload Image | cloudinary |
| Ask for Multi Images | Telegram |
| Show Menu | Telegram |
| Upload an asset from file data | cloudinary |
| Loop Over Items | 分批处理 |
| AI Agent1 | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Share to Social Media | Telegram |
| Compress Image | HTTP Request |
| Get Image | HTTP Request |
| If2 | IF 判断 |
| Structured Output Parser | 结构化输出解析器 |
| Instagram | Blotato |
| X | Blotato |
| Facebook | Blotato |
| Switch1 | Switch 路由 |
| If1 | IF 判断 |
| SHARING PROCESSOR | Code |
| WITHOUT IMAGE DATA | Code |
| JSON FORMATTER | Code |
| ENHANCED TEXT PREP | Code |
| STANDARD TEXT PREP | Code |
| IMAGE-TO-IMAGE PREP | Code |
| MULTI-IMAGE PREP | Code |
| MULTI-IMAGE SPLITTER | Code |
| Image generation failed (Kie.ai) | Telegram |
| Image compression failed (TinyPNG) | Telegram |
| Image upload failed (Cloudinary) multiple-images | Telegram |
| Image upload failed (Cloudinary) image-image | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：41
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：41
- 触发节点：1
- 处理节点：25
- 输出节点：15
- 分类：workflow-automation
