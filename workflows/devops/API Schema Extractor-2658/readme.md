# API Schema Extractor

https://n8nworkflows.xyz/workflows/2658

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Web Search For API Schema | HTTP Request |
| Scrape Webpage Contents | HTTP Request |
| Results to List | 数据拆分 |
| Recursive Character Text Splitter1 | 文本分割器 |
| Content Chunking @ 50k Chars | 数据设置 |
| Split Out Chunks | 数据拆分 |
| Default Data Loader | 文档加载器 |
| Set Embedding Variables | 数据设置 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Execution Data | executionData |
| EventRouter | Switch 路由 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Successful Runs | 过滤器 |
| For Each Document... | 分批处理 |
| Embeddings Google Gemini | Google Gemini Embeddings |
| Has API Documentation? | 文本分类器 |
| Store Document Embeddings | Qdrant 向量存储 |
| Embeddings Google Gemini1 | Google Gemini Embeddings |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| Extract API Operations | 信息提取器 |
| Search in Relevant Docs | Qdrant 向量存储 |
| Wait | 等待 |
| Remove Dupes | 去重 |
| Filter Results | 过滤器 |
| Research | 执行工作流 |
| Has Results? | IF 判断 |
| Response Empty | 数据设置 |
| Response OK | 数据设置 |
| Combine Docs | 数据聚合 |
| Template to List | 数据拆分 |
| Query Templates | 数据设置 |
| Google Gemini Chat Model2 | OpenAI Chat Model |
| For Each Template... | 分批处理 |
| Query & Docs | 数据设置 |
| Identify Service Products | 信息提取器 |
| Extract API Templates | 数据设置 |
| Embeddings Google Gemini2 | Google Gemini Embeddings |
| Search in Relevant Docs1 | Qdrant 向量存储 |
| Combine Docs1 | 数据聚合 |
| Query & Docs1 | 数据设置 |
| For Each Template...1 | 分批处理 |
| Merge Lists | Code |
| Remove Duplicates | 去重 |
| Append Row | Google Sheets |
| Response OK1 | 数据设置 |
| Has Operations? | IF 判断 |
| Response Empty1 | 数据设置 |
| Research Pending | Google Sheets |
| Research Result | Google Sheets |
| Research Error | Google Sheets |
| Extract Pending | Google Sheets |
| Research Event | 数据设置 |
| Extract Event | 数据设置 |
| Extract | 执行工作流 |
| Extract Result | Google Sheets |
| Extract Error | Google Sheets |
| Get API Operations | Google Sheets |
| Contruct JSON Schema | Code |
| Upload to Drive | Google Drive |
| Set Upload Fields | 数据设置 |
| Response OK2 | 数据设置 |
| Generate Event | 数据设置 |
| Generate Pending | Google Sheets |
| Generate | 执行工作流 |
| Generate Error | Google Sheets |
| Generate Result | Google Sheets |
| Get All Extract | Google Sheets |
| Get All Research | Google Sheets |
| For Each Research... | 分批处理 |
| For Each Extract... | 分批处理 |
| Wait1 | 等待 |
| All Research Done? | IF 判断 |
| All Extract Done? | IF 判断 |
| Get All Generate | Google Sheets |
| All Generate Done? | IF 判断 |
| For Each Generate... | 分批处理 |
| Wait2 | 等待 |
| Has Results?1 | IF 判断 |
| Response Scrape Error | 数据设置 |
| Has Results?3 | IF 判断 |
| Response No API Docs | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：82
- 触发节点：2
- 处理节点：78
- 输出节点：2
- 分类：devops
