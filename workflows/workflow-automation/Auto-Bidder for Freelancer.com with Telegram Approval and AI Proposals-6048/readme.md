## 简介
**Auto-Bidder for Freelancer.com with Telegram Approval and AI Proposals**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6048

---

# Auto-Bidder for Freelancer.com with Telegram Approval and AI Proposals


## 节点清单

| 节点 | 类型 |
|------|------|
| create a bid | HTTP Request |
| If | IF 判断 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| ExtractDate | 数据设置 |
| SetInputs | 数据设置 |
| If1 | IF 判断 |
| Send Succuss | Telegram |
| Search | HTTP Request |
| GetProjects | 数据拆分 |
| Loop Over Items | 分批处理 |
| checkBidding | HTTP Request |
| Split Out | 数据拆分 |
| Edit Fields | 数据设置 |
| Aggregate | 数据聚合 |
| If2 | IF 判断 |
| GetApproval | Telegram |
| Canceled | Telegram |
| When Executed by Another Workflow | 执行工作流触发器 |
| AlreadyBid | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Execute Workflow | 执行工作流 |
| Schedule Trigger | 定时触发器 |
| Edit Fields1 | 数据设置 |
| Split Out1 | 数据拆分 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：25
- 触发方式：手动触发, 定时触发

## 触发方式
- When Executed by Another Workflow 触发
- When clicking ‘Execute workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：25
- 触发节点：3
- 处理节点：16
- 输出节点：6
- 分类：workflow-automation
