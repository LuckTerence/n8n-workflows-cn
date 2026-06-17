## 简介
**Estimate 4D-5D construction costs from Revit BIM models with DDC CWICR**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12177

---

# Estimate 4D-5D construction costs from Revit BIM models with DDC CWICR


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking 'Execute workflow' | 手动触发 |
| Setup - Define file paths1 | 数据设置 |
| Configure Language & Vector DB | Code |
| Non-3D View Elements Output1 | 数据设置 |
| Find Category Fields | Code |
| Apply Classification to Groups | Code |
| Non-Building Elements Output1 | 数据设置 |
| Is Building Element1 | IF 判断 |
| Group Data with AI Rules1 | Code |
| Extract Headers and Data | Code |
| Read Excel File1 | 读取二进制文件 |
| Parse Excel1 | 电子表格文件 |
| Create - Excel filename1 | 数据设置 |
| Check - Does Excel file exist?1 | 读取二进制文件 |
| If - File exists?1 | IF 判断 |
| Extract - Run converter1 | 执行命令 |
| Info - Skip conversion1 | 数据设置 |
| Check - Did extraction succeed?1 | IF 判断 |
| Error - Show what went wrong1 | 数据设置 |
| Set xlsx_filename after success1 | 数据设置 |
| Merge - Continue workflow1 | 数据合并 |
| Set Parameters1 | 数据设置 |
| Process AI Response1 | Code |
| On the standard 3D View | IF 判断 |
| STAGE 0 - Collect BIM Data | Code |
| Parse Stage 1 - Project Type | Code |
| Parse Stage 2 - Phases | Code |
| Parse Stage 3 - Final Structure | Code |
| Prepare Types for Decomposition | Code |
| Loop Types for Decomposition | 分批处理 |
| Parse Decomposition & Prepare Works | Code |
| Has Work Items? | IF 判断 |
| Loop Work Items | 分批处理 |
| STAGE 6 - Map Rate Units to BIM | Code |
| Accumulate Work Results | Code |
| Aggregate Type Works | Code |
| Store Type Result | Code |
| Handle No Works | Code |
| STAGE 8 - Aggregate by Phases | Code |
| STAGE 7 - Calculate Costs | Code |
| STAGE 9 - Generate Cost Estimate | Code |
| STAGE 7.5 - Parse Validation | Code |
| STAGE 5.1 - Prepare Search Strategies1 | Code |
| STAGE 5.2 - Parse Results | Code |
| Save to Project Folder | Code |
| Write HTML File | 写入二进制文件 |
| CONFIG - AI Classify | 数据设置 |
| AI Classify Categories | LLM Chain |
| CONFIG - AI Headers | 数据设置 |
| AI Analyze All Headers | LLM Chain |
| CONFIG - STAGE 1 | 数据设置 |
| STAGE 1 - Detect Project Type | LLM Chain |
| CONFIG - STAGE 2 | 数据设置 |
| STAGE 2 - Generate Construction Phases | LLM Chain |
| CONFIG - STAGE 4 | 数据设置 |
| STAGE 4 - Decompose Type to Works | LLM Chain |
| CONFIG - STAGE 7.5 | 数据设置 |
| STAGE 7.5 - Validate Type Works | LLM Chain |
| Write XLS File | 写入二进制文件 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Anthropic Chat Model2 | OpenAI Chat Model |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| xAI Grok Chat Model1 | lmChatXAiGrok |
| Open HTML in Browser | 执行命令 |
| STAGE 5.1 - Embeddings | OpenAI Embeddings |
| DeepSeek Chat Model | lmChatDeepSeek |
| OpenAI LLM | OpenAI Chat Model |
| Save Type Before LLM | Code |
| Export All Outputs | Code |
| Write Output File | 写入二进制文件 |
| STAGE 2.5 - Compact Types1 | Code |
| CONFIG - STAGE 5 | 数据设置 |
| STAGE 3 - Assign Types to Phases1 | LLM Chain |
| Rate Limit Wait | 等待 |
| Limit to 10 Groups | Code |
| STAGE 5.1 - Vector Search | Qdrant 向量存储 |

## 触发方式
- When clicking 'Execute workflow' 触发

## 统计
- 节点总数：76
- 触发节点：1
- 处理节点：75
- 输出节点：0
- 分类：workflow-automation
