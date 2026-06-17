## 简介
**Generate images on Telegram from text and voice using Grok Imagine via Kie AI**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：23 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/13367

---

# Generate images on Telegram from text and voice using Grok Imagine via Kie AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Grok 4.1 Fast | OpenRouter Chat Model |
| Code | Code |
| Get Message | Telegram 触发器 |
| Send a text message | Telegram |
| Get Text | 数据设置 |
| Switch2 | Switch 路由 |
| Run text to image | 工作流工具 |
| Wait1 | 等待 |
| Run image to image | 工作流工具 |
| Wait2 | 等待 |
| Switch | Switch 路由 |
| Run Kei AI | 执行工作流触发器 |
| Run text to image1 | HTTP Request |
| Run image to image1 | HTTP Request |
| Result text to image | HTTP Request |
| Result image to image | HTTP Request |
| Get voice message | Telegram |
| Transcribe recording | OpenAI |
| Get image file | Telegram |
| Upload image | FTP |
| Set Image Url | 数据设置 |
| Get input text from voice | 数据设置 |
| Grok Imagine Agent | AI Agent |
| Simple Memory1 | 记忆缓冲区 |

## 触发方式
- Get Message 触发
- Run Kei AI 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：15
- 输出节点：7
- 分类：multimodal-ai
