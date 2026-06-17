# Generate text-to-video and image-to-video clips with Kling 2.6 via KIE.AI

https://n8nworkflows.xyz/workflows/12202

## 节点清单

| 节点 | 类型 |
|------|------|
| Submit Video Generation Request | HTTP Request |
| Switch Video Generation Status | Switch 路由 |
| Check Video Generation Status | HTTP Request |
| Wait for Video Generation | 等待 |
| Extract Video URL | Code |
| Download Video File | HTTP Request |
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Prompt & Image Url | 数据设置 |
| Wait for Image-to-Video Generation | 等待 |
| Switch | Switch 路由 |
| Check Video Status | HTTP Request |
| Download Video1 | HTTP Request |
| Submit Video Generation1 | HTTP Request |
| Video URL | Code |
| Set Text to Video Parameters | 数据设置 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：8
- 输出节点：6
- 分类：workflow-automation
