## 简介
**Monitor & Manage Docker Containers with Telegram Bot & AI Log Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10476

---

# Monitor & Manage Docker Containers with Telegram Bot & AI Log Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Message a model | OpenAI |
| Telegram Trigger | Telegram 触发器 |
| Switch | Switch 路由 |
| Merge | 数据合并 |
| Merge1 | 数据合并 |
| Switch1 | Switch 路由 |
| If | IF 判断 |
| OK Message | Telegram |
| ERROR Message | Telegram |
| Status Update | Telegram |
| Log Analysis | Telegram |
| Restart Message | Telegram |
| Success restart | Telegram |
| Restart Failed | Telegram |
| Docker Status | Telegram |
| get logs | SSH |
| restart container | SSH |
| docker ps | SSH |
| Code in Python (Beta) | Code |
| Update Docker | SSH |
| Update Msg | Telegram |
| Update Msg1 | Telegram |
| Extract the Service Name | Code |



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发。

Webhook触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：24
- 触发方式：Webhook 触发, Telegram 消息触发

## 触发方式
- Webhook 触发
- Telegram Trigger 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：12
- 输出节点：10
- 分类：workflow-automation
