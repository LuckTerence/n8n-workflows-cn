## 简介
**Process Images with VLM Run: Auto Segmentation & Detection with Drive-Telegram Sharing**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
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
