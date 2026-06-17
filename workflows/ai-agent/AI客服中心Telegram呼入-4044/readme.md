## 简介
**AI客服中心Telegram呼入**

生产级聊天机器人Part1

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4044

---

# AI客服中心Telegram呼入


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Test Trigger | Chat 触发器 |
| Test Input | 数据设置 |
| Telegram Input | 数据设置 |
| Type Switch | Switch 路由 |
| Download Audio | Telegram |
| Extract from File | 从文件提取 |
| Google STT | googleSpeech |
| Telegram Voice Input | 数据设置 |
| Input | 数据设置 |
| If Telegram | IF 判断 |
| If Active | IF 判断 |
| Parse Service | Code |
| Member Cache | Redis |
| If Member Cache | IF 判断 |
| Load Memer Data | PostgreSQL |
| Save Member Cache | Redis |
| Member | 数据设置 |
| Switch | Switch 路由 |
| English | 数据设置 |
| yue-Hant-HK | 数据设置 |
| cmn-Hant-TW | 数据设置 |
| cmn-Hans-CN | 数据设置 |
| ja-JP | 数据设置 |
| If Transcript | IF 判断 |
| No Transcript Input | 数据设置 |
| Demo Call Back | 执行工作流 |
| Demo Call Center | 执行工作流 |
| Telegram Test Output | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Chat 消息触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 数据库连接信息
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：29
- 触发方式：Telegram 消息触发, Chat 消息触发

## 触发方式
- Telegram Trigger 触发
- Test Trigger 触发

## 统计
- 节点总数：29
- 触发节点：2
- 处理节点：25
- 输出节点：2
- 分类：ai-agent
