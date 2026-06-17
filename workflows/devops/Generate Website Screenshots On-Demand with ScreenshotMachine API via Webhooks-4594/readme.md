## 简介
**Generate Website Screenshots On-Demand with ScreenshotMachine API via Webhooks**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4594

---

# Generate Website Screenshots On-Demand with ScreenshotMachine API via Webhooks


## 节点清单

| 节点 | 类型 |
|------|------|
| Receive URL Webhook | Webhook |
| Resolve URL (HEAD Request) | HTTP Request |
| Validate URL for SSRF | Code |
| IF URL Valid | IF 判断 |
| Take Screenshot | HTTP Request |
| Respond with Screenshot Data | 响应 Webhook |
| Respond with Validation Error | 响应 Webhook |

## 触发方式
- Receive URL Webhook 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：devops
