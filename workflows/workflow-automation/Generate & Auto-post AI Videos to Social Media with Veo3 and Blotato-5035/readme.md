## 简介
**Generate & Auto-post AI Videos to Social Media with Veo3 and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5035

---

# Generate & Auto-post AI Videos to Social Media with Veo3 and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Assign Social Media IDs | 数据设置 |
| Get my video | Google Sheets |
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
| Google Sheets | Google Sheets |
| Trigger: Run Daily Script Generator | 定时触发器 |
| AI Agent: Generate Video Concept | AI Agent |
| Tool: Inject Creativity | 思考工具 |
| LLM: Generate Idea & Caption (GPT-4.1) | OpenAI Chat Model |
| Parser: Extract JSON from Idea | 结构化输出解析器 |
| Google Sheets: Save Script Idea | Google Sheets |
| AI Agent: Create Veo3-Compatible Prompt | AI Agent |
| Tool: Build Prompt Structure | 思考工具 |
| LLM: Format Prompt for Veo3 (GPT-4.1) | OpenAI Chat Model |
| Call Veo3 API to Generate Video | HTTP Request |
| Wait for Veo3 Processing (5 mins) | 等待 |
| Retrieve Final Video URL from Veo3 | HTTP Request |
| Google Sheets: Log Final Video Output | Google Sheets |



## 功能说明

AI 视频生成工作流，自动创作视频内容，定时执行。

定时触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：26
- 触发方式：定时触发

## 触发方式
- Trigger: Run Daily Script Generator 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：13
- 输出节点：12
- 分类：workflow-automation
