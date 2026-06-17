## 简介
**AI Video Summarization with VLM Run - Automated Content Analysis for Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5108

---

# AI Video Summarization with VLM Run - Automated Content Analysis for Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| VLM Run Video Summarizer | vlmRun |
| Monitor Video Uploads | Google Drive 触发器 |
| Download Video File | Google Drive |
| Receive VLM Run Callback | Webhook |
| Send Summary to Team | Slack |



## 功能说明

AI 视频生成工作流，自动创作视频内容，Webhook 触发。

Webhook触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 通义万相 API Key → https://dashscope.aliyun.com

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：5
- 触发方式：Webhook 触发

## 触发方式
- Monitor Video Uploads 触发
- Receive VLM Run Callback 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：2
- 输出节点：1
- 分类：workflow-automation
