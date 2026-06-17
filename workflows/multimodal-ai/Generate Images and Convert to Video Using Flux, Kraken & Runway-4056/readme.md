# Generate Images and Convert to Video Using Flux, Kraken & Runway

https://n8nworkflows.xyz/workflows/4056

## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| get_image_url | HTTP Request |
| get_image | HTTP Request |
| upload to kraken | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Get Image3 | HTTP Request |
| upload to kraken1 | HTTP Request |
| Get Video Generation Status1 | HTTP Request |
| Confirm Generation Status | Switch 路由 |
| 1 minute3 | 等待 |
| 1 minute2 | 等待 |
| Download Video | HTTP Request |
| generate image (flux) | HTTP Request |
| generate image (flux-rapid-api) | HTTP Request |
| image to video (runway-rapid-api) | HTTP Request |
| image to video (runway) | HTTP Request |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：4
- 输出节点：11
- 分类：multimodal-ai
