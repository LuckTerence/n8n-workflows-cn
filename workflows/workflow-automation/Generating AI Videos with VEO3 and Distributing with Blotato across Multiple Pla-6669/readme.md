## 简介
**Generating AI Videos with VEO3 and Distributing with Blotato across Multiple Platforms**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Notion/Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6669

---

# Generating AI Videos with VEO3 and Distributing with Blotato across Multiple Platforms


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Think | 思考工具 |
| Structured Output Parser | 结构化输出解析器 |
| Assign Social Media IDs | 数据设置 |
| Upload Video to Blotato | HTTP Request |
| INSTAGRAM | HTTP Request |
| YOUTUBE | HTTP Request |
| TIKTOK | HTTP Request |
| FACEBOOK | HTTP Request |
| THREADS | HTTP Request |
| TWETTER | HTTP Request |
| LINKEDIN | HTTP Request |
| BLUESKY | HTTP Request |
| PINTEREST | HTTP Request |
| Send Video URL via Telegram | Telegram |
| Send Final Video Preview | Telegram |
| Telegram Trigger: Receive Video Idea | Telegram 触发器 |
| Read Video Parameters from Google Sheet | Google Sheets |
| Set Master Prompt | 数据设置 |
| AI Agent: Generate Video Script | AI Agent |
| Generate Video with VEO3 | HTTP Request |
| Wait for VEO3 Rendering | 等待 |
| Download Video from VEO3 | HTTP Request |
| Rewrite Caption with GPT-4o | OpenAI |
| Save Caption Video to Google Sheets | Google Sheets |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

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

- 节点总数：25
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger: Receive Video Idea 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：10
- 输出节点：14
- 分类：workflow-automation
