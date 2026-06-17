## 简介
**Automated video creation using Google V3 and n8n workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Zoom/Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4877

---

# Automated video creation using Google V3 and n8n workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| 📊 Fetch Ready Ideas from Sheet | Google Sheets |
| 🤖 VEO3 Prompt Generator (GPT-4.1) | AI Agent |
| 🧠 OpenAI Chat Model | OpenAI Chat Model |
| 📝 Structured Output Parser | 结构化输出解析器 |
| 🎬 Create Video with VEO3 (Fal AI) | HTTP Request |
| 🔍 Check Video Generation Status | HTTP Request |
| ✅ Is Video Generation Complete? | IF 判断 |
| ⏰ Wait Before Retry | 等待 |
| 📥 Download Generated Video | HTTP Request |
| 📊 Update Sheet with Video URL | Google Sheets |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
