## 简介
**Generate addictive ASMR Veo 3 reels**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15151

---

# Generate addictive ASMR Veo 3 reels


## 节点清单

| 节点 | 类型 |
|------|------|
| When Every 8 Hours | 定时触发器 |
| Read Sheet1 Data | Google Sheets |
| Define Prompt Agent | AI Agent |
| Idea Generation Agent | AI Agent |
| Aggregate Data | 数据聚合 |
| Set Objects List | 数据设置 |
| Parse Object Caption | 结构化输出解析器 |
| Manual Trigger Start | 手动触发 |
| OpenAI GPT-4.1 Mini | OpenAI Chat Model |
| Set API Credentials | 数据设置 |
| Generate JWT | jwt |
| Acquire Access Token | HTTP Request |
| Route by Status | Switch 路由 |
| Post to Video API | HTTP Request |
| Post to Status API | HTTP Request |
| Wait 20 Seconds | 等待 |
| Convert Data to File | 转换为文件 |
| Wait for Rendering | 等待 |
| Fetch Final Video | HTTP Request |
| GCS Upload for URL Access | googleCloudStorage |
| Render Video to 9:16 | HTTP Request |
| Check Done Status | IF 判断 |
| Setup Postiz API Config | 数据设置 |
| Verify Render Completion | HTTP Request |
| Upload Video to Postiz | HTTP Request |
| Fetch Postiz Integrations | HTTP Request |
| Route by Integration Type | Switch 路由 |
| Post to YouTube API | HTTP Request |
| Post to TikTok API | HTTP Request |
| Post to Instagram API | HTTP Request |



## 功能说明

Generate addictive ASMR Veo 3 reels（AI 增强)定时触发、手动触发，通过 HTTP API 实现自动化。

定时触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：30
- 触发方式：定时触发, 手动触发

## 触发方式
- When Every 8 Hours 触发
- Manual Trigger Start 触发

## 统计
- 节点总数：30
- 触发节点：2
- 处理节点：17
- 输出节点：11
- 分类：workflow-automation
