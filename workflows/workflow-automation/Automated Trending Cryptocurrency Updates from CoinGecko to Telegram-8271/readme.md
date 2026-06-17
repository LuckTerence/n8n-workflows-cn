## 简介
**Automated Trending Cryptocurrency Updates from CoinGecko to Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8271

---

# Automated Trending Cryptocurrency Updates from CoinGecko to Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Trending | HTTP Request |
| Format Message | Function |
| Send Telegram Message | Telegram |
| When clicking ‘Execute workflow’ | 手动触发 |
| 8:30 AM/PM IST | 定时触发器 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：5
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Execute workflow’ 触发
- 8:30 AM/PM IST 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：1
- 输出节点：2
- 分类：workflow-automation
