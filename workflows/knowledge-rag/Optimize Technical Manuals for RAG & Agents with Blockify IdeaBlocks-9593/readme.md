## 简介
**Optimize Technical Manuals for RAG & Agents with Blockify IdeaBlocks**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答，定时执行。

定时触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 搜索 API Key（如 SerpAPI / Brave Search）

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：定时触发

## 触发方式
- Schedule Trigger2 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：16
- 输出节点：4
- 分类：knowledge-rag
