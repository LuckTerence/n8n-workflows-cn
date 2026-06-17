# Process Images with VLM Run: Auto Segmentation & Detection with Drive-Telegram Sharing

https://n8nworkflows.xyz/workflows/11246

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
