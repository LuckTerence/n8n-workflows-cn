# Poll KIE.ai video generation status and send results via Telegram

https://n8nworkflows.xyz/workflows/12684

## 节点清单

| 节点 | 类型 |
|------|------|
| Poll Trigger | Webhook |
| Parse Input | Code |
| Respond OK | 响应 Webhook |
| Wait 1 Minute | 等待 |
| Check KIE Status | HTTP Request |
| Parse Status | Code |
| Completed? | IF 判断 |
| Get 1080p Video | Code |
| Get Final URL | Code |
| Download Video | HTTP Request |
| Get Session | Redis |
| Merge Session Data | Code |
| Update Session | Redis |
| Download for Telegram | S3 |
| Is Veo Model? | IF 判断 |
| Send Video Preview (Veo) | Telegram |
| Send Video Preview (Other) | Telegram |
| Can Retry? | IF 判断 |
| Retry Poll | HTTP Request |
| Send Timeout | Telegram |
| Upload a file | S3 |
| Create Metadata | Code |
| Upload Metadata | S3 |
| Is Extend? | IF 判断 |
| Skip Concat | Code |
| Merge After Concat | 数据合并 |
| Send Merge Options | Telegram |

## 触发方式
- Poll Trigger 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：18
- 输出节点：8
- 分类：multimodal-ai
