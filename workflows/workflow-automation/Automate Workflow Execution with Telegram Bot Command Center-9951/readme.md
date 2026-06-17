## 简介
**Automate Workflow Execution with Telegram Bot Command Center**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9951

---

# Automate Workflow Execution with Telegram Bot Command Center


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| format_output_as_json | Code |
| Generic Output | Telegram |
| Processing has finished | Telegram |
| Instagram post | 执行工作流 |
| Command not found | Telegram |
| Access Denied | Telegram |
| Access Control | IF 判断 |
| Seperate command and Parameter | Code |
| Valid Commands | 数据设置 |
| Switch to the Command | Switch 路由 |
| Social Analysis | 执行工作流 |
| Social Analysis Output | Telegram |
| sentimental_analysis | 执行工作流 |
| Generic Output1 | Telegram |



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

- 节点总数：15
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：8
- 输出节点：6
- 分类：workflow-automation
