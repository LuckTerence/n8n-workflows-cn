## 简介
**Automate Testing and Collect Responses via Telegram in Postgres (Module "Quiz")**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3612

---

# Automate Testing and Collect Responses via Telegram in Postgres (Module "Quiz")


## 节点清单

| 节点 | 类型 |
|------|------|
| For Tests | Switch 路由 |
| Test | Telegram |
| Randomize questions | 数据排序 |
| Wait | 等待 |
| Variables | 数据设置 |
| Merge | 数据合并 |
| Question | Telegram |
| Commands | Switch 路由 |
| Buttons | Switch 路由 |
| Switch | Switch 路由 |
| List tests | Telegram |
| Main Menu | Telegram |
| Update Bot Status on start | PostgreSQL |
| Telegram Trigger | Telegram 触发器 |
| Initialization | 数据设置 |
| Any questions? | IF 判断 |
| Delete message | Telegram |
| Code | Code |
| Get Questions AND Answers | PostgreSQL |
| Update Answer | PostgreSQL |
| Get Non-Answered Questions | PostgreSQL |
| Get Tests | PostgreSQL |
| Union Number with Question | 数据设置 |
| Union list | 文本摘要 |
| Get Test | PostgreSQL |
| Result Test | Telegram |
| Calculate answers | PostgreSQL |
| Upsert pred Answer | PostgreSQL |
| Variables TG | 数据设置 |
| Is Start? | IF 判断 |
| Welcome Message | Telegram |
| Error | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：32
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：32
- 触发节点：1
- 处理节点：23
- 输出节点：8
- 分类：workflow-automation
