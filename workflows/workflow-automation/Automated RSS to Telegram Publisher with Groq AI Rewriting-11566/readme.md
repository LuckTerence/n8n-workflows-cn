## 简介
**Automated RSS to Telegram Publisher with Groq AI Rewriting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11566

---

# Automated RSS to Telegram Publisher with Groq AI Rewriting


## 节点清单

| 节点 | 类型 |
|------|------|
| Groq Chat Model | Groq Chat Model |
| Every 30 minutes | 定时触发器 |
| Read RSS links | RSS Feed |
| Add link | 数据表 |
| Rewrite Post | AI Agent |
| Send post to user | Telegram |
| If link not in table | 数据表 |
| For each RSS | 分批处理 |
| Finish workflow | 空操作 |
| Get RSS list | 数据表 |
| Get only latest link | 数据限制 |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Every 30 minutes 触发
- Read RSS links 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
