## 简介
**AI Model Usage Dashboard: Track Token Metrics and Costs for LLM Workflows**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9497

---

# AI Model Usage Dashboard: Track Token Metrics and Costs for LLM Workflows


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Simple Memory | 记忆缓冲区 |
| OpenAI Chat Model | OpenAI Chat Model |
| Get Excution ID | 数据设置 |
| Model/Token Info | 数据设置 |
| Insert row2 | 数据表 |
| Get an execution | n8n |
| Schedule Trigger | 定时触发器 |
| Get row(s) | 数据表 |
| Update row(s) | 数据表 |
| Edit Fields | 数据设置 |
| Insert row1 | 数据表 |
| Get row(s)1 | 数据表 |
| Edit Fields1 | 数据设置 |
| Loop Over Items | 分批处理 |
| No Operation, do nothing | 空操作 |
| Webhook | Webhook |
| Get row(s)3 | 数据表 |
| Merge1 | 数据合并 |
| Code in JavaScript1 | Code |
| No Operation, do nothing1 | 空操作 |
| Code in JavaScript | Code |
| Respond to Webhook | 响应 Webhook |



## 功能说明

n8n 工作流管理工具，编排控制工作流的启停，定时执行。

定时触发、Webhook触发、Chat 消息触发，通过 HTTP API 实现自动化。

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
- 触发方式：Chat 消息触发, 定时触发, Webhook 触发

## 触发方式
- When chat message received 触发
- Schedule Trigger 触发
- Webhook 触发

## 统计
- 节点总数：24
- 触发节点：3
- 处理节点：20
- 输出节点：1
- 分类：workflow-automation
