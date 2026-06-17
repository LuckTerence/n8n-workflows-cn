## 简介
**Complete AI Safety Suite: Test 9 Guardrail Layers with Groq LLM**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11141

---

# Complete AI Safety Suite: Test 9 Guardrail Layers with Groq LLM


## 节点清单

| 节点 | 类型 |
|------|------|
| Start - Manual Trigger | 手动触发 |
| Test Cases Data | 数据设置 |
| Split Test Cases | 数据拆分 |
| Format Data | 数据设置 |
| Case 1 - Keyword Blocking | guardrails |
| Case 2 - Jailbreak Detection | guardrails |
| Case 3 - NSFW Content | guardrails |
| Case 4 - PII Detection (Sanitize) | guardrails |
| Case 5 - Secret Key Detection | guardrails |
| Case 6 - Topical Alignment | guardrails |
| Case 7 - URL Whitelisting | guardrails |
| Case 8 - Block URLs with Credentials | guardrails |
| Case 9 - Custom Regex | guardrails |
| Format Results | 数据设置 |
| Groq Chat Model | Groq Chat Model |



## 功能说明

Complete AI Safety Suite- Test 9 Guardrail Layers （AI 增强)手动触发，通过 n8n 内置节点实现自动化。

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

- 节点总数：15
- 触发方式：手动触发

## 触发方式
- Start - Manual Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：14
- 输出节点：0
- 分类：workflow-automation
