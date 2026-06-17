## 简介
**Automate S3 video transcoding, thumbnail generation & CDN distribution**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 节点数：17 | 难度：⭐⭐⭐ 高级
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

## 触发方式
- S3 Event Webhook1 触发
- Manual Process Trigger1 触发

## 统计
- 节点总数：19
- 触发节点：2
- 处理节点：10
- 输出节点：7
- 分类：workflow-automation
