## 简介
**Build an IT Support Assistant Chatbot Leveraging Existing Support Portal**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3498

---

# Build an IT Support Assistant Chatbot Leveraging Existing Support Portal


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Acuity Support Search API | HTTP Request |
| Extract Relevant Fields | 数据设置 |
| Results to Items | 数据拆分 |
| Has Results? | IF 判断 |
| Empty Response | 数据设置 |
| Aggregate Response | 数据聚合 |
| Knowledgebase Tool | 工作流工具 |
| AcuityScheduling Support Chatbot | AI Agent |
| KnowledgeBase Tool Subworkflow | 执行工作流触发器 |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答。

Chat 消息触发，通过 HTTP API 实现自动化。

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

- 节点总数：12
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发
- KnowledgeBase Tool Subworkflow 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：9
- 输出节点：1
- 分类：ai-agent
