## 简介
**Safely Update n8n with Version Checks and Telegram Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9792

---

# Safely Update n8n with Version Checks and Telegram Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Get Current Version | 执行命令 |
| Get Latest Version | HTTP Request |
| Compare Versions | Code |
| Merge Versions | 数据合并 |
| If Update Available? | IF 判断 |
| Get Executions | n8n |
| Check Running Workflows | Function |
| If Can Update? | IF 判断 |
| Notify Update Start | Telegram |
| Notify Latest Version | Telegram |
| Notify Update Available | Telegram |
| Execute Update | 执行命令 |
| Daily Trigger | 定时触发器 |
| n8n Startup Trigger | n8nTrigger |
| Wait | 等待 |



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

- 节点总数：15
- 触发方式：定时触发

## 触发方式
- Daily Trigger 触发
- n8n Startup Trigger 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：9
- 输出节点：4
- 分类：workflow-automation
