## 简介
**Automate Image Validation Tasks using AI Vision**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：7 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/2420

---

# Automate Image Validation Tasks using AI Vision


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Structured Output Parser | 结构化输出解析器 |
| Photo URLs | 数据设置 |
| Photos To List | 数据拆分 |
| Download Photos | Google Drive |
| Resize For AI | 图片编辑 |
| Passport Photo Validator | LLM Chain |
| Google Gemini Chat Model | OpenAI Chat Model |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：multimodal-ai
