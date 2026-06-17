# Automated video creation using Google V3 and n8n workflow

https://n8nworkflows.xyz/workflows/4877

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
