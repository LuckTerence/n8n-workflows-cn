## 简介
**Generate & Publish AI News Avatar Videos with HeyGen and Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8050

---

# Generate & Publish AI News Avatar Videos with HeyGen and Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload to Blotato1 | HTTP Request |
| Schedule Trigger1 | 定时触发器 |
| AI Agent1 | AI Agent |
| Wait6 | 等待 |
| Write Script1 | OpenAI Chat Model |
| Setup Heygen1 | 数据设置 |
| Get Avatar Video1 | HTTP Request |
| Prepare for Publish1 | 数据设置 |
| Write Long Caption1 | OpenAI |
| Write Short Caption1 | OpenAI |
| Create Avatar Video1 | HTTP Request |
| Write Title1 | OpenAI |
| [TikTOK] Publish via Blotato1 | HTTP Request |
| [TikTOK] Publish via Blotato | HTTP Request |
| [TikTOK] Publish via Blotato2 | HTTP Request |
| [TikTOK] Publish via Blotato3 | HTTP Request |
| [TikTOK] Publish via Blotato4 | HTTP Request |
| [TikTOK] Publish via Blotato5 | HTTP Request |
| [TikTOK] Publish via Blotato6 | HTTP Request |
| [TikTOK] Publish via Blotato7 | HTTP Request |
| Read AI News Feed | rssFeedReadTool |
| Read AI News Feed1 | rssFeedReadTool |



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

- 节点总数：22
- 触发方式：定时触发

## 触发方式
- Schedule Trigger1 触发
- Read AI News Feed 触发
- Read AI News Feed1 触发

## 统计
- 节点总数：22
- 触发节点：3
- 处理节点：8
- 输出节点：11
- 分类：workflow-automation
