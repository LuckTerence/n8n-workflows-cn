## 简介
**Auto-Send Vtiger Support Tickets to Telegram (with Status Update)**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6329

---

# Auto-Send Vtiger Support Tickets to Telegram (with Status Update)


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger Every n Minutes | 定时触发器 |
| VtigerCRM get Tickets | vtigerNode |
| If there's a data returned | IF 判断 |
| Send a Ticket detail to Telegram | Telegram |
| VtigerCRM Update Ticket Status | vtigerNode |
| No Operation, do nothing | 空操作 |



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

- 节点总数：6
- 触发方式：定时触发

## 触发方式
- Schedule Trigger Every n Minutes 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：4
- 输出节点：1
- 分类：workflow-automation
