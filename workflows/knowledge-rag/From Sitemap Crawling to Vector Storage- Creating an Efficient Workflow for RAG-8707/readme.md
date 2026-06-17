## 简介
**From Sitemap Crawling to Vector Storage: Creating an Efficient Workflow for RAG**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：34 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/8707

---

# From Sitemap Crawling to Vector Storage: Creating an Efficient Workflow for RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| HTTP Request | HTTP Request |
| XML | XML |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| If | IF 判断 |
| Default Data Loader | 文档加载器 |
| Character Text Splitter | textSplitterCharacterTextSplitter |
| Embeddings OpenAI | OpenAI Embeddings |
| Edit Fields | 数据设置 |
| Crawl4AI_Task Status | HTTP Request |
| Loop Over Items1 | 分批处理 |
| If2 | IF 判断 |
| Split Out1 | 数据拆分 |
| Format the URL | 数据设置 |
| Check if the URL is in the Supabase Table | Supabase |
| Format the Output from the Supabase node | Code |
| If "shouldInsert" is true | IF 判断 |
| URL in a new row | Supabase |
| CREATE TABLE scrape_queue in Supabase | PostgreSQL |
| CREATE TABLE scrape_queue in Supabase1 | PostgreSQL |
| Crawl4ai Web Page Scrape | HTTP Request |
| Remove redundant data from the scraping | Code |
| Supabase Vector Store_documents | Supabase 向量存储 |
| Get a row - scrape_queue Table | Supabase |
| Update a row in scrape_queue Table | Supabase |
| Update a row in scrape_queue Table1 | Supabase |
| Wait1 | 等待 |
| Quality Filter Node | Code |
| Content Type Detection | Code |
| Better Metadata Extraction | Code |
| If1 | IF 判断 |
| Update a row in scrape_queue Table2 | Supabase |
| Task_id Counter | Code |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：35
- 触发节点：1
- 处理节点：31
- 输出节点：3
- 分类：knowledge-rag
