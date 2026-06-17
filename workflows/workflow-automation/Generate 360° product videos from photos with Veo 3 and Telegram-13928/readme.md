## 简介
**Generate 360° product videos from photos with Veo 3 and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13928

---

# Generate 360° product videos from photos with Veo 3 and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait 2 Minutes | 等待 |
| Send Timeout Error | Telegram |
| Check Timeout | IF 判断 |
| Download Image | Telegram |
| Telegram Trigger | Telegram 触发器 |
| 2. Validate Input | Code |
| Check Auth Token Valid | IF 判断 |
| Send Validation Error | Telegram |
| Send Processing Message | Telegram |
| Convert Image to Base64 | Code |
| Conversion OK? | IF 判断 |
| Send Conversion Error | Telegram |
| 5. Prepare Veo Request | Code |
| 6. Call Vertex AI Veo 3 | HTTP Request |
| Extract Operation Name | Code |
| Poll Video Status | HTTP Request |
| Is Video Ready? | IF 判断 |
| Convert Video to File | 转换为文件 |
| Continue Polling | Code |
| Send Video to User | Telegram |
| 2. Build JWT from Sheet | Code |
| 3. Get Access Token | HTTP Request |
| 1. Get Service Account Details | Google Sheets |



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

- 节点总数：23
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：13
- 输出节点：9
- 分类：workflow-automation
