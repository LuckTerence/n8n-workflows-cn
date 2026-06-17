## 简介
**Create and publish AI social posts to multiple platforms using Blotato**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13471

---

# Create and publish AI social posts to multiple platforms using Blotato


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait4 | 等待 |
| If Else | IF 判断 |
| If1 | IF 判断 |
| Telegram Trigger | Telegram 触发器 |
| Create Transcription | Blotato |
| Get Transcription | Blotato |
| Wait | 等待 |
| Create visual | Blotato |
| Check with perplexity ai | Blotato |
| If | IF 判断 |
| Wait1 | 等待 |
| Get content | Blotato |
| Send a photo message | Telegram |
| post for approval | Telegram |
| Get visual | Blotato |
| Send a text message | Telegram |
| Wait5 | 等待 |
| If Else1 | IF 判断 |
| Create visual1 | Blotato |
| Get visual1 | Blotato |
| Send notification : Published | Telegram |
| Wait9 | 等待 |
| If Else3 | IF 判断 |
| Create visual3 | Blotato |
| Get visual3 | Blotato |
| Send notification : Published2 | Telegram |
| Create Facebook2 | Blotato |
| Wait12 | 等待 |
| If Else4 | IF 判断 |
| Create visual4 | Blotato |
| Get visual4 | Blotato |
| Send notification : Published3 | Telegram |
| Create Linkedin3 | Blotato |
| Wait15 | 等待 |
| If Else5 | IF 判断 |
| Create visual5 | Blotato |
| Get visual5 | Blotato |
| Send notification : Published4 | Telegram |
| Create Tiktok | Blotato |
| Create Instagram | Blotato |
| Get image/video1 | HTTP Request |
| Create Twitter | Blotato |
| Get image/video2 | HTTP Request |
| Get image/video3 | HTTP Request |



## 功能说明

社交媒体管理，多平台内容发布和监听。

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

- 节点总数：44
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：44
- 触发节点：1
- 处理节点：33
- 输出节点：10
- 分类：workflow-automation
