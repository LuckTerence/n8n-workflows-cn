# Compare AI Models with Nvidia API: Qwen, DeepSeek, Seed-OSS & Nemotron

https://n8nworkflows.xyz/workflows/9283

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Format Response | 数据设置 |
| Send Aggregated AI Model Responses | 响应 Webhook |
| Merge AI Model | 数据合并 |
| AI Model Router | Switch 路由 |
| Query Qwen3-next-80b-a3b-thinking (Alibaba) | HTTP Request |
| Query Bytedance/seed-oss-36b-instruct (Bytedance) | HTTP Request |
| Query Nvidia-nemotron-nano-9b-v2 (Nvidia) | HTTP Request |
| Query DeepSeekv3_1 | HTTP Request |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：3
- 输出节点：5
- 分类：workflow-automation
