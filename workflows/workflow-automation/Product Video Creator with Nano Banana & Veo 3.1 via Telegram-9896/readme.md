## 简介
**Product Video Creator with Nano Banana & Veo 3.1 via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9896

---

# Product Video Creator with Nano Banana & Veo 3.1 via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Image to Base64 | 从文件提取 |
| AI Design Analysis | OpenAI Chat Model |
| Combine Image & Analysis | 数据合并 |
| Prepare API Payload | Code |
| Generate Enhanced Image | HTTP Request |
| Convert Base64 to Image (only image) | 转换为文件 |
| Convert Base64 to Image (image and text) | 转换为文件 |
| Initiate veo 3.1 Video Generation | HTTP Request |
| Check Video Status | HTTP Request |
| Video Ready Validator | IF 判断 |
| Processing Delay (30s) | 等待 |
| Convert Base64 to video | 转换为文件 |
| Download Image File | Telegram |
| Telegram Trigger Received | Telegram 触发器 |
| Send veo 3.1 video | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：15
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger Received 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：9
- 输出节点：5
- 分类：workflow-automation
