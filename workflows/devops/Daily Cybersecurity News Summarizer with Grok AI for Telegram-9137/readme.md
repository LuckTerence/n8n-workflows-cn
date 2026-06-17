## 简介
**Daily Cybersecurity News Summarizer with Grok AI for Telegram**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9137

---

# Daily Cybersecurity News Summarizer with Grok AI for Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Merge | 数据合并 |
| Loop Over Items | 分批处理 |
| Bleeping Computer Security Bulletin | RSS Feed |
| HTTP Request | HTTP Request |
| Filter Image Links From Body | 数据设置 |
| Filter Body from Full HTML | 数据设置 |
| Send a photo message | Telegram |
| OpenRouter Chat Model | OpenRouter Chat Model |
| 9 AM - Schedule Trigger | 定时触发器 |
| Wait 1 min | 等待 |
| AI Agent | AI Agent |
| Simple Memory | 记忆缓冲区 |
| Sponsored Removal | IF 判断 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：13
- 触发方式：定时触发

## 触发方式
- Bleeping Computer Security Bulletin 触发
- 9 AM - Schedule Trigger 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：9
- 输出节点：2
- 分类：devops
