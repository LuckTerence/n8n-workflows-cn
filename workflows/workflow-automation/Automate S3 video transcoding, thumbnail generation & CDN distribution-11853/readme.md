## 简介
**Automate S3 video transcoding, thumbnail generation & CDN distribution**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11853

---

# Automate S3 video transcoding, thumbnail generation & CDN distribution


## 节点清单

| 节点 | 类型 |
|------|------|
| S3 Event Webhook1 | Webhook |
| Manual Process Trigger1 | Webhook |
| Merge Triggers1 | 数据合并 |
| Extract S3 Info1 | Code |
| Check Is Video1 | IF 判断 |
| Invalid File Response1 | 数据设置 |
| Get Video Metadata (FFprobe)1 | HTTP Request |
| Parse Video Metadata1 | Code |
| Generate Thumbnails (FFmpeg)1 | HTTP Request |
| Generate Preview GIF1 | HTTP Request |
| Transcode Video1 | HTTP Request |
| Aggregate Processing Results1 | 数据聚合 |
| Invalidate CDN Cache1 | HTTP Request |
| Generate Signed URLs1 | Code |
| Log Processing Metrics1 | Google Sheets |
| Send Slack Notification1 | Slack |
| Merge Output Paths1 | 数据合并 |
| Merge All Paths1 | 数据合并 |
| Respond to Webhook1 | 响应 Webhook |



## 功能说明

AI 视频生成工作流，自动创作视频内容，Webhook 触发。

Webhook触发，通过 Slack + HTTP API 实现自动化。

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

- 节点总数：19
- 触发方式：Webhook 触发

## 触发方式
- S3 Event Webhook1 触发
- Manual Process Trigger1 触发

## 统计
- 节点总数：19
- 触发节点：2
- 处理节点：10
- 输出节点：7
- 分类：workflow-automation
