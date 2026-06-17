## 简介
**Control AlphaInsider stock and crypto portfolios from Telegram text and voice**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13816

---

# Control AlphaInsider stock and crypto portfolios from Telegram text and voice


## 节点清单

| 节点 | 类型 |
|------|------|
| Transcribe Voice Message | OpenAI |
| Get Voice Message | Telegram |
| Channel Check | IF 判断 |
| Global Settings | 数据设置 |
| Message Details | 数据设置 |
| Message Details Check | Switch 路由 |
| Message Check | Switch 路由 |
| Get Positions | HTTP Request |
| Parse Position Percents | Code |
| Parse Stock Allocations | AI Agent |
| OpenAI Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Search Stocks | HTTP Request 工具 |
| Calculator | 计算器工具 |
| ParseOutput | 结构化输出解析器 |
| Parse Orders Allocations | Code |
| Create Orders | HTTP Request |
| Switch | Switch 路由 |
| Create Post | HTTP Request |
| User Reply | Telegram |
| If DM | IF 判断 |
| Telegram Channel Listener | Telegram 触发器 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警。

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

- 节点总数：22
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Channel Listener 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：15
- 输出节点：6
- 分类：finance-analysis
