# Parse and Extract Data from Documents-Images with Mistral OCR

https://n8nworkflows.xyz/workflows/3102

## 节点清单

| 节点 | 类型 |
|------|------|
| Mistral Upload | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |
| Mistral Signed URL | HTTP Request |
| Import PDF | Google Drive |
| Import Image | Google Drive |
| Mistral Upload1 | HTTP Request |
| Mistral Signed URL1 | HTTP Request |
| Mistral DOC OCR | HTTP Request |
| Mistral IMAGE OCR | HTTP Request |
| Document URL | 数据设置 |
| Image URL | 数据设置 |
| Mistral DOC OCR1 | HTTP Request |
| Mistral IMAGE OCR1 | HTTP Request |
| Document URL1 | 数据设置 |
| Document Understanding | HTTP Request |
| Image URL1 | 数据设置 |
| Document Mis-Understanding? | HTTP Request |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：6
- 输出节点：10
- 分类：workflow-automation
