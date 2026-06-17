## 简介
**Generate metaphor-based product video ads Veo 3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15149

---

# Generate metaphor-based product video ads Veo 3


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Workflow Trigger | 手动触发 |
| Google Gemini Brainstormer | OpenAI Chat Model |
| Google Gemini Creative Session | OpenAI Chat Model |
| Content Creation Director | LLM Chain |
| Idea Generation Chain | LLM Chain |
| Parse Structured Output | 结构化输出解析器 |
| DeepSeek Conversational AI | lmChatDeepSeek |
| Google Gemini Prompt Design | OpenAI Chat Model |
| Prompt Optimization Chain | LLM Chain |
| Google Gemini Complementary Ideas | OpenAI Chat Model |
| Post to Creatomate API | HTTP Request |
| Wait for Rendering | 等待 |
| Check Render Status | HTTP Request |
| Upload Ad to Cloud Storage | googleCloudStorage |
| Upload Complementary File | googleCloudStorage |
| Complementary Insights Chain | LLM Chain |
| Build Creatomate Request | Code |
| Set Input Variables | 数据设置 |
| Configure API Settings | 数据设置 |
| Generate JWT Token | jwt |
| Fetch OAuth Token | HTTP Request |
| Initiate Video Creation | HTTP Request |
| Wait for Video Processing | 等待 |
| Check Processing Status | HTTP Request |
| Route by Processing Outcome | Switch 路由 |
| Convert Ad to File | 转换为文件 |
| Start Complementary Video Creation | HTTP Request |
| Wait for Complementary Video | 等待 |
| Check Complementary Status | HTTP Request |
| Route Complementary Outcome | Switch 路由 |
| Convert Complementary to File | 转换为文件 |
| Route Final Video Outcome | Switch 路由 |
| Download Final Video | HTTP Request |
| Send Video via Telegram | Telegram |



## 功能说明

AI 视频生成工作流，自动创作视频内容。

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

- 节点总数：34
- 触发方式：手动触发

## 触发方式
- Manual Workflow Trigger 触发

## 统计
- 节点总数：34
- 触发节点：1
- 处理节点：24
- 输出节点：9
- 分类：workflow-automation
