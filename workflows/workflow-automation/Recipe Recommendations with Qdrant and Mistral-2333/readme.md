## 简介
**Recipe Recommendations with Qdrant and Mistral**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2333

---

# Recipe Recommendations with Qdrant and Mistral


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Test workflow" | 手动触发 |
| Get This Week's Menu | HTTP Request |
| Extract Available Courses | Code |
| Extract Server Data | HTML |
| Get Course Metadata | 数据设置 |
| Get Recipe | HTTP Request |
| Embeddings Mistral Cloud | embeddingsMistralCloud |
| Default Data Loader | 文档加载器 |
| Merge Course & Recipe | 数据合并 |
| Prepare Documents | 数据设置 |
| Recursive Character Text Splitter | 文本分割器 |
| Chat Trigger | Chat 触发器 |
| Extract Recipe Details | HTML |
| Qdrant Recommend API | 工作流工具 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| Get Tool Response | 数据设置 |
| Wait for Rate Limits | 等待 |
| Get Mistral Embeddings | HTTP Request |
| Use Qdrant Recommend API | HTTP Request |
| Get Recipes From DB | Code |
| Save Recipes to DB | Code |
| AI Agent | AI Agent |
| Qdrant Vector Store | Qdrant 向量存储 |



## 功能说明

Recipe Recommendations with Qdrant and Mistral（AI 增强)手动触发、Chat 消息触发，通过 HTTP API 实现自动化。

Chat 消息触发、手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：手动触发, Chat 消息触发

## 触发方式
- When clicking "Test workflow" 触发
- Chat Trigger 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：24
- 触发节点：3
- 处理节点：17
- 输出节点：4
- 分类：workflow-automation
