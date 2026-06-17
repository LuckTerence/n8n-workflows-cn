## 简介
**Process Images with VLM Run: Auto Segmentation & Detection with Drive-Telegram Sharing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11246

---

# Process Images with VLM Run: Auto Segmentation & Detection with Drive-Telegram Sharing


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload Image | 表单触发器 |
| Send Image | Telegram |
| Upload File | Google Drive |
| Code | Code |
| VLM Run (Segmentation) | vlmRun |
| VLM Run (Detection) | vlmRun |
| Download Image | HTTP Request |
| Webhook for Segmented Image | Webhook |
| Webhook for Detected Image | Webhook |



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发（Images)表单提交触发、Webhook 触发，通过 Telegram + HTTP API 实现自动化。

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

- 节点总数：9
- 触发方式：表单提交触发, Webhook 触发

## 触发方式
- Upload Image 触发
- Webhook for Segmented Image 触发
- Webhook for Detected Image 触发

## 统计
- 节点总数：9
- 触发节点：3
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
