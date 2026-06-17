## 简介
**Qwen-Max: Journal Paper Generation from Title-Abstract**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10314

---

# Qwen-Max: Journal Paper Generation from Title-Abstract


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Extract Input Data | 数据设置 |
| Search CrossRef | HTTP Request |
| Search Semantic Scholar | HTTP Request |
| Search OpenAlex | HTTP Request |
| Merge Reference Sources | 数据合并 |
| Process References | Code |
| Prepare AI Context | 数据设置 |
| AI - Introduction | AI Agent |
| AI - Literature Review | AI Agent |
| AI - Methodology | AI Agent |
| AI - Results | AI Agent |
| AI - Discussion | AI Agent |
| AI - Conclusion | AI Agent |
| Merge All Sections | 数据合并 |
| Compile Document | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |



## 功能说明

Qwen-Max- Journal Paper Generation from Title-Abst（AI 增强)Webhook 触发，通过 HTTP API 实现自动化。

Webhook触发，通过 HTTP API 实现自动化。

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

- 节点总数：17
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：17
- 触发节点：1
- 处理节点：13
- 输出节点：3
- 分类：workflow-automation
