## 简介
**Automated Telegram UserBot Session Monitoring & Recovery with TelePilot**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5872

---

# Automated Telegram UserBot Session Monitoring & Recovery with TelePilot


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Schedule Trigger | 定时触发器 |
| Stop auth | telePilot |
| Start auth | telePilot |
| Manual control | telePilot |
| Automatic control | telePilot |
| Get Session Status | 数据设置 |
| Stop Session | 数据设置 |
| Start Session | 数据设置 |
| Pass on Closed Status | 过滤器 |
| Send Closed Status message | Telegram |
| Check Session Connection | 过滤器 |
| Send Session Connection message | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Chat 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：13
- 触发方式：Chat 消息触发, 定时触发

## 触发方式
- When chat message received 触发
- Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：9
- 输出节点：2
- 分类：workflow-automation
