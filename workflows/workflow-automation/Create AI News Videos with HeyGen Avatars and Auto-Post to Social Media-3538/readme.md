## 简介
**Create AI News Videos with HeyGen Avatars and Auto-Post to Social Media**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3538

---

# Create AI News Videos with HeyGen Avatars and Auto-Post to Social Media


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload to Blotato | HTTP Request |
| [Instagram] Publish via Blotato | HTTP Request |
| [Facebook] Publish via Blotato | HTTP Request |
| [Linkedin] Publish via Blotato | HTTP Request |
| [Tiktok] Publish via Blotato | HTTP Request |
| OpenAI | OpenAI |
| Upload to Blotato - Image | HTTP Request |
| [Pinterest] Publish via Blotato | HTTP Request |
| [Youtube] Publish via Blotato | HTTP Request |
| [Threads] Publish via Blotato | HTTP Request |
| [Twitter] Publish via Blotato | HTTP Request |
| [Bluesky] Publish via Blotato | HTTP Request |
| Schedule Trigger | 定时触发器 |
| AI Agent | AI Agent |
| Fetch HN Article | hackerNewsTool |
| Fetch HN Front Page | hackerNewsTool |
| Wait | 等待 |
| Write Script | OpenAI Chat Model |
| Setup Heygen | 数据设置 |
| Get Avatar Video | HTTP Request |
| Prepare for Publish | 数据设置 |
| Write Long Caption | OpenAI |
| Write Short Caption | OpenAI |
| Create Avatar Video | HTTP Request |



## 功能说明

AI 视频生成工作流，自动创作视频内容，定时执行。

定时触发，通过 HTTP API 实现自动化。

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

- 节点总数：24
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：10
- 输出节点：13
- 分类：workflow-automation
