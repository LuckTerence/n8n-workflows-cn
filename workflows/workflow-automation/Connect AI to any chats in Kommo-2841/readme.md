## 简介
**Connect AI to any chats in Kommo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2841

---

# Connect AI to any chats in Kommo


## 节点清单

| 节点 | 类型 |
|------|------|
| isVoice | IF 判断 |
| get voice | HTTP Request |
| get_entity | HTTP Request |
| ai | AI Agent |
| model | OpenAI Chat Model |
| memory | 记忆缓冲区 |
| hasStopTag | Switch 路由 |
| transcribe voice | OpenAI |
| setText | 数据设置 |
| Get token | HTTP Request |
| Recieve message | HTTP Request |
| new_message | Webhook |



## 功能说明

Connect AI to any chats in Kommo（AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：Webhook 触发

## 触发方式
- new_message 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
