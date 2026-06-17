## 简介
**Auto-Generate FAQ Answers in Vtiger CRM with DeepSeek LLM and LangChain**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6308

---

# Auto-Generate FAQ Answers in Vtiger CRM with DeepSeek LLM and LangChain


## 节点清单

| 节点 | 类型 |
|------|------|
| Vtiger | vtigerNode |
| Vtiger1 | vtigerNode |
| If | IF 判断 |
| AI Agent | AI Agent |
| DeepSeek Chat Model | lmChatDeepSeek |
| Simple Memory | 记忆缓冲区 |
| Schedule Trigger Every n Minutes | 定时触发器 |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发，通过 工作流编排 实现自动化。

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

- 节点总数：7
- 触发方式：定时触发

## 触发方式
- Schedule Trigger Every n Minutes 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：6
- 输出节点：0
- 分类：workflow-automation
