## 简介
**Monitor Commercial Real Estate Opportunities from LoopNet with ScrapeGraphAI & Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6625

---

# Monitor Commercial Real Estate Opportunities from LoopNet with ScrapeGraphAI & Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily CRE Scanner | 定时触发器 |
| CRE Data Collector | HTTP Request |
| CRE Analyzer & Dashboard | Code |
| Check for Opportunities | IF 判断 |
| Send Opportunity Alert | Telegram |
| Log to Google Sheets | Google Sheets |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

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

- 节点总数：6
- 触发方式：定时触发

## 触发方式
- Daily CRE Scanner 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
