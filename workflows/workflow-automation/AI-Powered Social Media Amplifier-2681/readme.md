## 简介
**AI-Powered Social Media Amplifier**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2681

---

# AI-Powered Social Media Amplifier


## 节点清单

| 节点 | 类型 |
|------|------|
| Crawl HN Home | HTTP Request |
| Extract Meta | Code |
| Filter Unposted Items | Code |
| Visit GH Page | HTTP Request |
| Convert HTML To Markdown | Markdown |
| Filter Errored | 过滤器 |
| No Operation, do nothing | 空操作 |
| Update X Status | Airtable |
| LinkedIn | linkedIn |
| Update L Status | Airtable |
| Search Item | Airtable |
| Create Item | Airtable |
| X | Twitter |
| Validate Generate Content | Code |
| Schedule Trigger | 定时触发器 |
| Merge | 数据合并 |
| Generate Content | OpenAI |
| Ping Me | Telegram |
| Wait for 5 mins before posting | 等待 |



## 功能说明

社交媒体管理，多平台内容发布和监听，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：19
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：15
- 输出节点：3
- 分类：workflow-automation
