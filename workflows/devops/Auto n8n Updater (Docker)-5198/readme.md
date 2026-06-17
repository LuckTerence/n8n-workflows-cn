## 简介
**Auto n8n Updater (Docker)**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5198

---

# Auto n8n Updater (Docker)


## 节点清单

| 节点 | 类型 |
|------|------|
| Docker Path | 数据设置 |
| Update Docker | SSH |
| Get n8n Current Version | SSH |
| Get Instance's Settings | HTTP Request |
| Is Docker | IF 判断 |
| Get Version's Last Update | HTTP Request |
| Target Version | 数据设置 |
| Get Current Version | HTTP Request |
| Needs Update ? | IF 判断 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Approved ? | IF 判断 |
| Every Hour | 定时触发器 |
| Published In Last Hours ? | IF 判断 |
| Release Overview | LLM Chain |
| Approve Update | Telegram |
| Get n8n Github Release | HTTP Request |



## 功能说明

自动部署流水线，代码提交后自动构建和发布，定时执行。

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

- 节点总数：16
- 触发方式：定时触发

## 触发方式
- Every Hour 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：10
- 输出节点：5
- 分类：devops
