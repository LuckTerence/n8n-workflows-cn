## 简介
**Chat with News Articles using AI Analysis in Telegram with Vector Search**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10996

---

# Chat with News Articles using AI Analysis in Telegram with Vector Search


## 节点清单

| 节点 | 类型 |
|------|------|
| Send a document | Telegram |
| Structured Output Parser1 | 结构化输出解析器 |
| VLM Agent2 | OpenAI Chat Model |
| VLM Agent3 | OpenAI Chat Model |
| Split Out | 数据拆分 |
| HTTP Request1 | HTTP Request |
| No Operation, do nothing1 | 空操作 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Insert Data to Store | vectorStoreInMemory |
| Query Data Tool | vectorStoreInMemory |
| AI Agent | AI Agent |
| Code | Code |
| Check Whether URL | IF 判断 |
| Listen to Telegram for Link | Telegram 触发器 |
| Rename Link Field | 数据设置 |
| VLM Run Highlighter | AI Agent |
| Check URLs Validity | IF 判断 |
| Covert to Text File | 转换为文件 |
| OpenAI Chat Model | OpenAI Chat Model |
| Send a Reply | Telegram |
| Start Asking | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：22
- 触发方式：Telegram 消息触发

## 触发方式
- Listen to Telegram for Link 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：17
- 输出节点：4
- 分类：knowledge-rag
