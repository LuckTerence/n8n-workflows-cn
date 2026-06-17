## 简介
**Simple Eval for Legal Benchmarking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4712

---

# Simple Eval for Legal Benchmarking


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Loop Over Items | 分批处理 |
| Wait | 等待 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Extract from File | 从文件提取 |
| Google Drive | Google Drive |
| Get Tests | Google Sheets |
| Structured Output Parser | 结构化输出解析器 |
| Update Results | Google Sheets |
| LLM Judge | LLM Chain |
| Is PDF? | IF 判断 |
| Is a file? | IF 判断 |



## 功能说明

Simple Eval for Legal Benchmarking（AI 增强)手动触发，通过 HTTP API 实现自动化。

手动触发，通过 HTTP API 实现自动化。

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
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：11
- 输出节点：0
- 分类：workflow-automation
