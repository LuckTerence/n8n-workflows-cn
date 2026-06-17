# CV Resume PDF Parsing with Multimodal Vision AI

https://n8nworkflows.xyz/workflows/2416

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Structured Output Parser | 结构化输出解析器 |
| Should Proceed To Stage 2? | IF 判断 |
| Download Resume | Google Drive |
| PDF-to-Image API | HTTP Request |
| Resize Converted Image | 图片编辑 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Candidate Resume Analyser | LLM Chain |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
