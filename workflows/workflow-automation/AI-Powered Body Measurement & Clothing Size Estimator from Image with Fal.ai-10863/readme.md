## 简介
**AI-Powered Body Measurement & Clothing Size Estimator from Image with Fal.ai**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10863

---

# AI-Powered Body Measurement & Clothing Size Estimator from Image with Fal.ai


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Get status | HTTP Request |
| Completed? | IF 判断 |
| Form | 表单 |
| Wait 10 sec. | 等待 |
| Send image to estimator | HTTP Request |
| Get result | HTTP Request |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Send a message | Email 发送 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |

## 触发方式
- On form submission 触发
- Webhook 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：6
- 输出节点：5
- 分类：workflow-automation
