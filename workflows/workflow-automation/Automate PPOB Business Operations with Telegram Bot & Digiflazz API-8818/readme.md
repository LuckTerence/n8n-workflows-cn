## 简介
**Automate PPOB Business Operations with Telegram Bot & Digiflazz API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8818

---

# Automate PPOB Business Operations with Telegram Bot & Digiflazz API


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Main Command Router | Switch 路由 |
| Welcome Message | Telegram |
| Main Menu | Telegram |
| Generate Balance Signature | Code |
| Check Balance API | HTTP Request |
| Format Balance Response | Code |
| Send Balance Result | Telegram |
| Generate Product Signature | Code |
| Get Products API | HTTP Request |
| Format Product List | Code |
| Send Product Categories | Telegram |
| Deposit Information | Telegram |
| Topup Menu | Telegram |
| Check Bill Menu | Telegram |
| Pay Bill Menu | Telegram |
| Process Topup Selection | Code |
| Process Check Bill Selection | Code |
| Process Pay Bill Selection | Code |
| Send Topup Input Prompt | Telegram |
| Send Check Bill Input Prompt | Telegram |
| Send Pay Bill Input Prompt | Telegram |
| Transaction History | Telegram |
| Process Deposit Information | Code |
| Send Deposit Information | Telegram |
| Process Trancation History Information | Code |
| Send Transaction Information | Telegram |
| Process Menu | Code |
| Send Menu Information | Telegram |
| Process Welcome | Code |
| Send Welcome | Telegram |
| Execute Transaction API | HTTP Request |
| Bill Inquiry API | HTTP Request |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：33
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：33
- 触发节点：1
- 处理节点：12
- 输出节点：20
- 分类：workflow-automation
