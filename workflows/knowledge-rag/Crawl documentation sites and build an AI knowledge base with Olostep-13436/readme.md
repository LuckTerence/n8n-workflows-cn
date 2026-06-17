## 简介
**Crawl documentation sites and build an AI knowledge base with Olostep**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Docs/Google Drive/Supabase/Notion/Pinecone)（基本改完，配置 API Key 应该就能跑）
> 节点数：25 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/13436

---

# Crawl documentation sites and build an AI knowledge base with Olostep


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Split Out1 | 数据拆分 |
| Service Name | 数据设置 |
| Create Parent Folder | Google Drive |
| Merge | 数据合并 |
| Create a map | olostepScrape |
| Edit Fields | 数据设置 |
| Loop Over Items | 分批处理 |
| Search files and folders | Google Drive |
| If | IF 判断 |
| Create folder | Google Drive |
| counter | 数据设置 |
| counter++ | 数据设置 |
| If1 | IF 判断 |
| counter++1 | 数据设置 |
| Scrape a URL | olostepScrape |
| set data | 数据设置 |
| No Operation, do nothing | 空操作 |
| Information Extractor | 信息提取器 |
| Google Gemini Chat Model2 | OpenAI Chat Model |
| AI Agent | AI Agent |
| Merge1 | 数据合并 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Create a document | Google Docs |
| Update a document | Google Docs |
| Wait | 等待 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：25
- 输出节点：0
- 分类：knowledge-rag
