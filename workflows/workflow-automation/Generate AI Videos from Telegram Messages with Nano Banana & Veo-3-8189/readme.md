## 简介
**Generate AI Videos from Telegram Messages with Nano Banana & Veo-3**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8189

---

# Generate AI Videos from Telegram Messages with Nano Banana & Veo-3


## 节点清单

| 节点 | 类型 |
|------|------|
| Wait | 等待 |
| Telegram Trigger | Telegram 触发器 |
| Image Gen (Nano Banana) | HTTP Request |
| Telegram: Send Photo | Telegram |
| Telegram: Send Video | Telegram |
| Switch | Switch 路由 |
| Transcribe a recording | OpenAI |
| Transcribed Audio | 数据设置 |
| Text Message | 数据设置 |
| Download Audio1 | Telegram |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Wait1 | 等待 |
| Get Image | HTTP Request |
| Image created | IF 判断 |
| Download Image | HTTP Request |
| Download Video | HTTP Request |
| Get Video | HTTP Request |
| Generate Video | HTTP Request |
| Video created | IF 判断 |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：11
- 输出节点：9
- 分类：workflow-automation
