## 简介
**Automated Economic Calendar PDF Reports to Telegram via RapidAPI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9025

---

# Automated Economic Calendar PDF Reports to Telegram via RapidAPI


## 节点清单

| 节点 | 类型 |
|------|------|
| Dynamically Sets the Date | Code |
| Schedule Every 7 Days | 定时触发器 |
| Set API Key for RapidAPI & Dates | 数据设置 |
| Gets Upcoming News | HTTP Request |
| Filter Medium & High Impact News | Code |
| Convert All Items Into One Array | Code |
| Edit & Update Template | HTTP Request |
| Download PDF Report | HTTP Request |
| Organize Data for API Template | Code |
| Send Economic Calendar Events PDF to Telegram | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

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
- Schedule Every 7 Days 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：5
- 输出节点：4
- 分类：workflow-automation
