# Generate multi-format social visuals with Abyssale and publish via Blotato

https://n8nworkflows.xyz/workflows/13357

## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Upload Image to tmpfiles | HTTP Request |
| Extract Public URL | Code |
| Prepare AI Agent Input | 数据设置 |
| Generate NanoBanana Prompt | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Create NanoBanana Image | HTTP Request |
| Extract Prediction ID | Code |
| Wait Before Polling | 等待 |
| Check Image Status | HTTP Request |
| Check If Completed | IF 判断 |
| Extract Final Image URL | Code |
| Download Final Image | HTTP Request |
| Send Photo to Telegram | Telegram |
| Structured Output Parser | 结构化输出解析器 |
| Get a file | Telegram |
| OpenAI Vision: Analyze Reference Image | OpenAI |
| Extract Prediction ID1 | Code |
| Wait Before Polling1 | 等待 |
| Check Image Status1 | HTTP Request |
| Check If Completed1 | IF 判断 |
| Extract Final Image URL1 | Code |
| image background remover | HTTP Request |
| Extract Layers | Code |
| On form submission | 表单触发器 |
| Form | 表单 |
| Build Form Fields | Code |
| Build Abyssale Elements | Code |
| Generate Images | HTTP Request |
| Convert Uploads to Base64 | Code |
| Get a design | abyssale |
| Switch | Switch 路由 |
| Upload media | Blotato |
| Upload media1 | Blotato |
| Upload media2 | Blotato |
| Upload media3 | Blotato |
| Upload media4 | Blotato |
| Upload media5 | Blotato |
| Upload media6 | Blotato |
| Upload media7 | Blotato |
| Create facebook-post | Blotato |
| Create facebook-reel | Blotato |
| Create instagram-post | Blotato |
| Create instagram-story | Blotato |
| Create tiktok-post | Blotato |
| Create twitter-post | Blotato |
| Create linkedin-feed | Blotato |
| Create pinterest-pins | Blotato |

## 触发方式
- Telegram Trigger 触发
- On form submission 触发

## 统计
- 节点总数：48
- 触发节点：2
- 处理节点：37
- 输出节点：9
- 分类：workflow-automation
