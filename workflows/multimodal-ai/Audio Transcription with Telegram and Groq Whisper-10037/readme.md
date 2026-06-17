## 简介
**Audio Transcription with Telegram and Groq Whisper**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10037

---

# Audio Transcription with Telegram and Groq Whisper


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram: Receive Message | Telegram 触发器 |
| Switch (Check Message Type) | Switch 路由 |
| Telegram: Unsupported Type Message | Telegram |
| Set Node (audio type) | 数据设置 |
| Set Node (voice type) | 数据设置 |
| Telegram: Download Audio File | Telegram |
| HTTP - Transcribe Audio (Groq) | HTTP Request |
| Set Credentials (Groq + Telegram) | 数据设置 |
| Telegram: Send Output Options | Telegram |
| If: Output Type Selected | IF 判断 |
| Telegram: Send Transcript Message | Telegram |
| Set: Transcribed Audio Text | 数据设置 |
| Convert to TXT File | 转换为文件 |
| Send Transcript File | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：14
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram: Receive Message 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：7
- 输出节点：6
- 分类：multimodal-ai
