# AI Data Extraction with Dynamic Prompts and Baserow

https://n8nworkflows.xyz/workflows/2780

## 节点清单

| 节点 | 类型 |
|------|------|
| Baserow Event | Webhook |
| Event Type | Switch 路由 |
| Table Fields API | HTTP Request |
| Get Prompt Fields | Code |
| Get Event Body | 数据设置 |
| List Table API | HTTP Request |
| Get Valid Rows | Code |
| Get File Data | HTTP Request |
| Extract from File | 从文件提取 |
| Update Row | HTTP Request |
| Get Result | 数据设置 |
| Loop Over Items | 分批处理 |
| Row Reference | 空操作 |
| Generate Field Value | LLM Chain |
| Get Row | HTTP Request |
| Rows to List | 数据拆分 |
| Fields to Update | Code |
| Loop Over Items1 | 分批处理 |
| Row Ref | 空操作 |
| Get File Data1 | HTTP Request |
| Extract from File1 | 从文件提取 |
| Update Row1 | HTTP Request |
| Get Result1 | 数据设置 |
| Generate Field Value1 | LLM Chain |
| Filter Valid Rows | 过滤器 |
| Filter Valid Fields | 过滤器 |
| Event Ref | 空操作 |
| Event Ref1 | 空操作 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |

## 触发方式
- Baserow Event 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：22
- 输出节点：7
- 分类：workflow-automation
