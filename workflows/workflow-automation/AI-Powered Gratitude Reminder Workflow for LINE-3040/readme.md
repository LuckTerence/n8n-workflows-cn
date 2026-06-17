## 简介
**AI-Powered Gratitude Reminder Workflow for LINE**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3040

---

# AI-Powered Gratitude Reminder Workflow for LINE


## 节点清单

| 节点 | 类型 |
|------|------|
| Trigger 2100 Bear Gratitude Jar Notice | 定时触发器 |
| WriteReminder | LLM Chain |
| Reformat Output from Chat Model | 数据设置 |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Line Push Message | HTTP Request |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，定时执行。

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

- 节点总数：5
- 触发方式：定时触发

## 触发方式
- Trigger 2100 Bear Gratitude Jar Notice 触发

## 统计
- 节点总数：5
- 触发节点：1
- 处理节点：3
- 输出节点：1
- 分类：workflow-automation
