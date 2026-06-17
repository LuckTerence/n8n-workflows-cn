## 简介
**Poll KIE.ai video generation status and send results via Telegram**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12684

---

# Poll KIE.ai video generation status and send results via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Poll Trigger | Webhook |
| Parse Input | Code |
| Respond OK | 响应 Webhook |
| Wait 1 Minute | 等待 |
| Check KIE Status | HTTP Request |
| Parse Status | Code |
| Completed? | IF 判断 |
| Get 1080p Video | Code |
| Get Final URL | Code |
| Download Video | HTTP Request |
| Get Session | Redis |
| Merge Session Data | Code |
| Update Session | Redis |
| Download for Telegram | S3 |
| Is Veo Model? | IF 判断 |
| Send Video Preview (Veo) | Telegram |
| Send Video Preview (Other) | Telegram |
| Can Retry? | IF 判断 |
| Retry Poll | HTTP Request |
| Send Timeout | Telegram |
| Upload a file | S3 |
| Create Metadata | Code |
| Upload Metadata | S3 |
| Is Extend? | IF 判断 |
| Skip Concat | Code |
| Merge After Concat | 数据合并 |
| Send Merge Options | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：27
- 触发方式：Webhook 触发

## 触发方式
- Poll Trigger 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：18
- 输出节点：8
- 分类：multimodal-ai
