# fal.ai图片生成

https://n8nworkflows.xyz/workflows/4108

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Fetch Status | HTTP Request |
| Wait | 等待 |
| Is Ready? | IF 判断 |
| Submit Request | HTTP Request |
| Fetch Result | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |
| 400 Error | 响应 Webhook |
| Success | 响应 Webhook |
| NSFW Filter | 文本分类器 |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：4
- 输出节点：5
- 分类：multimodal-ai
