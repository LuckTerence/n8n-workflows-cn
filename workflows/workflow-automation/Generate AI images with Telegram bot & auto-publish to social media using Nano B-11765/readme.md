## 简介
**Generate AI images with Telegram bot & auto-publish to social media using Nano Banana PRO**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：40 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/11765

---

# Generate AI images with Telegram bot & auto-publish to social media using Nano Banana PRO


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request | HTTP Request |
| HTTP Request2 | HTTP Request |
| HTTP Request1 | HTTP Request |
| Telegram Trigger | Telegram 触发器 |
| Switch | Switch 路由 |
| Ask for Text Prompt | Telegram |
| Ask for Image Upload | Telegram |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Send a photo message | Telegram |
| If | IF 判断 |
| Wait | 等待 |
| Upload Image | cloudinary |
| Ask for Multi Images | Telegram |
| Show Menu | Telegram |
| Upload an asset from file data | cloudinary |
| Loop Over Items | 分批处理 |
| AI Agent1 | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Share to Social Media | Telegram |
| Compress Image | HTTP Request |
| Get Image | HTTP Request |
| If2 | IF 判断 |
| Structured Output Parser | 结构化输出解析器 |
| Instagram | Blotato |
| X | Blotato |
| Facebook | Blotato |
| Switch1 | Switch 路由 |
| If1 | IF 判断 |
| SHARING PROCESSOR | Code |
| WITHOUT IMAGE DATA | Code |
| JSON FORMATTER | Code |
| ENHANCED TEXT PREP | Code |
| STANDARD TEXT PREP | Code |
| IMAGE-TO-IMAGE PREP | Code |
| MULTI-IMAGE PREP | Code |
| MULTI-IMAGE SPLITTER | Code |
| Image generation failed (Kie.ai) | Telegram |
| Image compression failed (TinyPNG) | Telegram |
| Image upload failed (Cloudinary) multiple-images | Telegram |
| Image upload failed (Cloudinary) image-image | Telegram |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：41
- 触发节点：1
- 处理节点：25
- 输出节点：15
- 分类：workflow-automation
