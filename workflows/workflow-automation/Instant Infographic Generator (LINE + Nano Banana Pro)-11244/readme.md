## 简介
**Instant Infographic Generator (LINE + Nano Banana Pro)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11244

---

# Instant Infographic Generator (LINE + Nano Banana Pro)


## 节点清单

| 节点 | 类型 |
|------|------|
| LINE Webhook | Webhook |
| Extract Data | Code |
| Optimize Prompt (Data Vis) | OpenAI Chat Model |
| Parse Gemini Response | Code |
| Submit to Nano Banana Pro | HTTP Request |
| Wait | 等待 |
| Check Job Status | HTTP Request |
| Is Ready? | IF 判断 |
| Parse Result | Code |
| Download Image | HTTP Request |
| Upload to S3 | awsS3 |
| Send Image to LINE | HTTP Request |

## 触发方式
- LINE Webhook 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
