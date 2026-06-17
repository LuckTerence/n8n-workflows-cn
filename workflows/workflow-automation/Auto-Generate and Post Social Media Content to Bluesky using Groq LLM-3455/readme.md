## 简介
**Auto-Generate and Post Social Media Content to Bluesky using Groq LLM**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3455

---

# Auto-Generate and Post Social Media Content to Bluesky using Groq LLM


## 节点清单

| 节点 | 类型 |
|------|------|
| Create Bluesky Session | HTTP Request |
| Post to Bluesky | HTTP Request |
| Define Credentials | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Groq Chat Model | Groq Chat Model |
| HTTP error | HTTP Request |
| Wait | 等待 |
| Stop and Error | 停止并报错 |
| LLM Chain | LLM Chain |
| Execution Count Code | Code |
| Execution Count Check | IF 判断 |
| Check if JSON is Valid | IF 判断 |
| Code code to cap posts at 300 characters | Code |
| Execution Count Code 2 | Code |
| Execution Count Check 2 | IF 判断 |



## 功能说明

社交媒体管理，多平台内容发布和监听，定时执行。

定时触发，通过 HTTP API 实现自动化。

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
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
