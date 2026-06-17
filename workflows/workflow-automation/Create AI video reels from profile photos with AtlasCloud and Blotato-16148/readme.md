# Create AI video reels from profile photos with AtlasCloud and Blotato

https://n8nworkflows.xyz/workflows/16148

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Config | 数据设置 |
| Wait Image | 等待 |
| Poll Image | HTTP Request |
| Generate Video | HTTP Request |
| Wait Video | 等待 |
| Poll Video | HTTP Request |
| Generate Image with GPT Image 2 Model | HTTP Request |
| Extract Image URL | Code |
| Extract Video URL | Code |
| Create post Tiktok | Blotato |
| Create post Instagram | Blotato |
| Image Status | Switch 路由 |
| Stop and Error | 停止并报错 |
| Video Status | Switch 路由 |
| Stop and Error II | 停止并报错 |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：11
- 输出节点：4
- 分类：workflow-automation
