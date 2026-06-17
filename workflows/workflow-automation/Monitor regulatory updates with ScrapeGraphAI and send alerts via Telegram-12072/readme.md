## 简介
**Monitor regulatory updates with ScrapeGraphAI and send alerts via Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/12072

---

# Monitor regulatory updates with ScrapeGraphAI and send alerts via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow | 手动触发 |
| Define Sources | Code |
| Split Sources | 分批处理 |
| Scrape Regulatory Data | ScrapeGraph AI |
| Merge Results | 数据合并 |
| Format & Deduplicate | Code |
| New Important Update? | IF 判断 |
| Prepare Telegram Message | 数据设置 |
| Send Telegram Alert | Telegram |
| Save to Redis | Redis |
| Error Handler | Code |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：11
- 触发方式：手动触发

## 触发方式
- Start Workflow 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：9
- 输出节点：1
- 分类：workflow-automation
