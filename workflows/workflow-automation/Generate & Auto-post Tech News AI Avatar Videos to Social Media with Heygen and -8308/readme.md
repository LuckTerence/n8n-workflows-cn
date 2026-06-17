## 简介
**Generate & Auto-post Tech News AI Avatar Videos to Social Media with Heygen and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8308

---

# Generate & Auto-post Tech News AI Avatar Videos to Social Media with Heygen and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| AI Agent | AI Agent |
| Fetch HN Article | hackerNewsTool |
| Fetch HN Front Page | hackerNewsTool |
| Wait | 等待 |
| Write Script | OpenAI Chat Model |
| Setup Heygen | 数据设置 |
| Get Avatar Video | HTTP Request |
| Write Long Caption | OpenAI |
| Write Short Caption | OpenAI |
| Upload media | Blotato |
| Tiktok [BLOTATO] | Blotato |
| Linkedin [BLOTATO] | Blotato |
| Facebook [BLOTATO] | Blotato |
| Instagram [BLOTATO] | Blotato |
| Twitter [BLOTATO] | Blotato |
| Youtube [BLOTATO] | Blotato |
| Threads [BLOTATO] | Blotato |
| Bluesky [BLOTATO] | Blotato |
| Pinterest [BLOTATO] | Blotato |
| Create Avatar Video WITH Background Video | HTTP Request |
| Create Avatar Video WITHOUT Background Video | HTTP Request |
| If | IF 判断 |
| Merge | 数据合并 |



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
- 处理节点：20
- 输出节点：3
- 分类：workflow-automation
