## 简介
**Generate & Publish SEO Blog Posts to Blogger using OpenRouter AI & Mediastack News**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6015

---

# Generate & Publish SEO Blog Posts to Blogger using OpenRouter AI & Mediastack News


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Send a text message | Telegram |
| Mediastack News | HTTP Request |
| Copywriter AI Agent | AI Agent |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Cleanup HTML | 数据设置 |
| AI Agent | AI Agent |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Parsing | Code |
| HTTP Request | HTTP Request |
| Send a text message1 | Telegram |
| Genarate image | HTTP Request |



## 功能说明

SEO 优化工具，关键词分析和内容优化，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：12
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
