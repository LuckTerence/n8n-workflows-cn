## 简介
**Automate Token Purchases with Dollar Cost Averaging on Uniswap V3 & 1Shot API**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8044

---

# Automate Token Purchases with Dollar Cost Averaging on Uniswap V3 & 1Shot API


## 节点清单

| 节点 | 类型 |
|------|------|
| Calculate TWAP | Code |
| Fetch Pool TWA Observations | 一次性执行 |
| Get Swap Qoute | 一次性执行 |
| Swap Tokens | 一次性同步 |
| Schedule Trigger | 定时触发器 |
| Failure Details | Telegram |
| Give Approval to Router | 一次性同步 |
| Success Details | Telegram |
| Get Remaining DCA Funds Balance | 一次性执行 |
| Swap Configs | Code |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：10
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：knowledge-rag
