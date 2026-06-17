## 简介
**Optimize Technical Manuals for RAG & Agents with Blockify IdeaBlocks**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9593

---

# Optimize Technical Manuals for RAG & Agents with Blockify IdeaBlocks


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger2 | 定时触发器 |
| Initiate PDF Extraction | HTTP Request |
| PDF Status Polling | HTTP Request |
| Wait | 等待 |
| Extract IdeaBlocks from API Response | 数据设置 |
| Convert to File | 转换为文件 |
| Technical Manual Prompt Payload Assembly | Code |
| Technical Manual Split Chunks | Code |
| Strip and Clean to Aggregate XML | 数据设置 |
| Upload Blockified Manual | Google Drive |
| Blockify Technical Ingest API | HTTP Request |
| If Completed Poller | IF 判断 |
| Search files and folders | Google Drive |
| Loop over Documents to Blockify | 分批处理 |
| Download Document to Blockify | Google Drive |
| Upload a Document to S3 | awsS3 |
| Get AWS Signed URL | Code |
| Download Final PDF Extracted Text Output | HTTP Request |
| Extract Raw Markdown from PDF Text | 数据设置 |
| Loop Over Chunks for Blockify | 分批处理 |
| Aggregate all Manual Sections | 数据聚合 |

## 触发方式
- Schedule Trigger2 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：16
- 输出节点：4
- 分类：knowledge-rag
