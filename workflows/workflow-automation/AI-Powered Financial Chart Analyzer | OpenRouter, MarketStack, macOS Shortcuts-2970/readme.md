## 简介
**AI-Powered Financial Chart Analyzer | OpenRouter, MarketStack, macOS Shortcuts**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2970

---

# AI-Powered Financial Chart Analyzer | OpenRouter, MarketStack, macOS Shortcuts


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Fields_Data | 数据设置 |
| Base64_To_Binary_Image | 转换为文件 |
| AI Agent | AI Agent |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Window Buffer Memory | 记忆缓冲区 |
| Calculator | 计算器工具 |
| Marketstack | marketstackTool |
| SerpAPI | SerpApi 工具 |
| Markdown | Markdown |



## 功能说明

AI-Powered Financial Chart Analyzer | OpenRouter、（AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：11
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
