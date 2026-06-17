## 简介
**Delete Dialogflow Intents via Telegram Commands**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7409

---

# Delete Dialogflow Intents via Telegram Commands


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| HTTP Request ELIMINAR | HTTP Request |
| User validation by ID | IF 判断 |
| Keyword validation | IF 判断 |
| Invalid user message | Telegram |
| Invalid keyword message | Telegram |
| HTTP Request GET NAME | HTTP Request |
| simulated delay | 等待 |
| Confirmation message | Telegram |
| HTTP Request GET | HTTP Request |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：3
- 输出节点：6
- 分类：devops
