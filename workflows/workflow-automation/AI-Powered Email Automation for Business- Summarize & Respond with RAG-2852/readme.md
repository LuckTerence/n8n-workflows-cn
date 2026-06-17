## 简介
**AI-Powered Email Automation for Business: Summarize & Respond with RAG**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2852

---

# AI-Powered Email Automation for Business: Summarize & Respond with RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| Email Trigger (IMAP) | Email 读取 |
| Markdown | Markdown |
| DeepSeek R1 | OpenAI Chat Model |
| Send Email | Email 发送 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Email Classifier | 文本分类器 |
| Email Summarization Chain | chainSummarization |
| Write email | AI Agent |
| Review email | LLM Chain |
| When clicking ‘Test workflow’ | 手动触发 |
| Create collection | HTTP Request |
| Refresh collection | HTTP Request |
| Get folder | Google Drive |
| Download Files | Google Drive |
| Default Data Loader | 文档加载器 |
| Token Splitter | textSplitterTokenSplitter |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Do nothing | 空操作 |
| OpenAI | OpenAI Chat Model |
| DeepSeek | OpenAI Chat Model |
| OpenAI 4-o-mini | OpenAI Chat Model |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

手动触发，通过 邮箱 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：23
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：18
- 输出节点：4
- 分类：workflow-automation
