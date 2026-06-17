## 简介
**Get Real-Time Security Insights with NixGuard RAG and Wazuh Integration**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4693

---

# Get Real-Time Security Insights with NixGuard RAG and Wazuh Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Send Request to NixGuard API | HTTP Request |
| Format API Response | 数据设置 |
| Prepare Final Output | Code |
| Parse NixGuard Response | Code |
| Merge Input Data | 数据合并 |
| Aggregate Security Data | 数据聚合 |
| Combine Security Data | Code |
| Prepare API Request Data | 数据设置 |



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

- 节点总数：10
- 触发方式：Chat 消息触发

## 触发方式
- When chat message received 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：7
- 输出节点：1
- 分类：knowledge-rag
