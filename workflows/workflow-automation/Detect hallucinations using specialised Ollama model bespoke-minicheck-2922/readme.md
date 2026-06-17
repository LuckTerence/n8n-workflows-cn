## 简介
**Detect hallucinations using specialised Ollama model bespoke-minicheck**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2922

---

# Detect hallucinations using specialised Ollama model bespoke-minicheck


## 节点清单

| 节点 | 类型 |
|------|------|
| Code | Code |
| Split Out1 | 数据拆分 |
| Basic LLM Chain4 | LLM Chain |
| Ollama Chat Model | Ollama Chat Model |
| When clicking ‘Test workflow’ | 手动触发 |
| Edit Fields | 数据设置 |
| Merge | 数据合并 |
| Filter | 过滤器 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Aggregate | 数据聚合 |
| Merge1 | 数据合并 |
| Basic LLM Chain | LLM Chain |
| Ollama Model | lmOllama |



## 功能说明

Detect hallucinations using specialised Ollama mod（AI 增强)手动触发，通过 n8n 内置节点实现自动化。

手动触发，通过 工作流编排 实现自动化。

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

- 节点总数：13
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
