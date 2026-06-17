# Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch

https://n8nworkflows.xyz/workflows/2331

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Test workflow" | 手动触发 |
| Fetch Source Image | HTTP Request |
| Split Out Results Only | 数据拆分 |
| Filter Score >= 0.9 | 过滤器 |
| Crop Object From Image | 图片编辑 |
| Set Variables | 数据设置 |
| Use Detr-Resnet-50 Object Classification | HTTP Request |
| Upload to Cloudinary | HTTP Request |
| Create Docs In Elasticsearch | elasticsearch |
| Fetch Source Image Again | HTTP Request |

## 触发方式
- When clicking "Test workflow" 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：5
- 输出节点：4
- 分类：workflow-automation
