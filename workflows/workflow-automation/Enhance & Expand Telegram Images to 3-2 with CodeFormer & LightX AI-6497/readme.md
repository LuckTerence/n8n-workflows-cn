# Enhance & Expand Telegram Images to 3:2 with CodeFormer & LightX AI

https://n8nworkflows.xyz/workflows/6497

## 节点清单

| 节点 | 类型 |
|------|------|
| Send Final URL to User via Telegram | Telegram |
| Generate Public URL for Final Image | 数据设置 |
| Upload Final Photo to S1 | awsS3 |
| Download Final Photo from LightX | HTTP Request |
| Generate Output Filename (.jpeg) Final | 数据设置 |
| Check If Expansion Is Complete | IF 判断 |
| Check LightX Expansion Status | HTTP Request |
| Wait Before Checking Status Again | 等待 |
| Iterate Until Expansion is Ready | 分批处理 |
| Request AI Expansion from LightX | HTTP Request |
| Upload File to LightX via PUT | HTTP Request |
| Merge Data for Upload | 数据合并 |
| Extract Upload Link from LightX Response | 数据设置 |
| Request Upload Link from LightX | HTTP Request |
| Get File Size (in Bytes) | Code |
| Calculate Padding for 3:2 Ratio | Code |
| Download Upscaled Image from Replicate1 | HTTP Request |
| Wait After Upscale | 等待 |
| AI Upscale Image via Replicate | HTTP Request |
| Generate Output File Name (.png) | 数据设置 |
| Set Input URL for AI Model | 数据设置 |
| Generate Public URL for Original Image | 数据设置 |
| Upload Original Photo to S1 | awsS3 |
| Generate Input File Name (.jpeg) | 数据设置 |
| Check If Photo Exists1 | IF 判断 |
| Telegram Trigger1 | Telegram 触发器 |

## 触发方式
- Telegram Trigger1 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：17
- 输出节点：8
- 分类：workflow-automation
